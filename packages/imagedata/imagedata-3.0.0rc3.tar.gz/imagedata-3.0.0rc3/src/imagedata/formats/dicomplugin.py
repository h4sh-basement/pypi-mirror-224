"""Read/Write DICOM files
"""

# Copyright (c) 2013-2022 Erling Andersen, Haukeland University Hospital, Bergen, Norway

import os
import sys
import logging
import traceback
import warnings
import math
from datetime import date, datetime, timedelta
import numpy as np
import pydicom
import pydicom.valuerep
import pydicom.config
import pydicom.errors
import pydicom.uid
from pydicom.datadict import tag_for_keyword

from ..formats import CannotSort, NotImageError, INPUT_ORDER_FAULTY, input_order_to_dirname_str, \
    SORT_ON_SLICE, \
    INPUT_ORDER_NONE, INPUT_ORDER_TIME, INPUT_ORDER_B, INPUT_ORDER_FA, INPUT_ORDER_TE, \
    INPUT_ORDER_AUTO
from ..axis import VariableAxis, UniformLengthAxis
from .abstractplugin import AbstractPlugin
from ..header import Header

logger = logging.getLogger(__name__)
try:
    # pydicom >= 2.3
    pydicom.config.settings.reading_validation_mode = pydicom.config.IGNORE
    # pydicom.config.settings.writing_validation_mode = pydicom.config.IGNORE
    pydicom.config.settings.writing_validation_mode = pydicom.config.WARN
    # pydicom.config.settings.writing_validation_mode = pydicom.config.RAISE
except AttributeError:
    # pydicom < 2.3
    pydicom.config.enforce_valid_values = True


class FilesGivenForMultipleURLs(Exception):
    pass


class NoDICOMAttributes(Exception):
    pass


class UnevenSlicesError(Exception):
    pass


class ValueErrorWrapperPrecisionError(Exception):
    pass


class UnknownTag(Exception):
    pass


# noinspection PyPep8Naming
class DICOMPlugin(AbstractPlugin):
    """Read/write DICOM files.

    Attributes:
        input_order
        DicomHeaderDict
        instanceNumber
        today
        now
        serInsUid
        input_options
        output_sort
        output_dir
        seriesTime
    """

    name = "dicom"
    description = "Read and write DICOM files."
    authors = "Erling Andersen"
    version = "1.3.0"
    url = "www.helse-bergen.no"

    root = "2.16.578.1.37.1.1.4"
    smallint = ('bool8', 'byte', 'ubyte', 'ushort', 'uint16', 'int8', 'uint8', 'int16')
    keep_uid = False

    def __init__(self):
        super(DICOMPlugin, self).__init__(self.name, self.description,
                                          self.authors, self.version, self.url)
        self.input_order = None
        self.DicomHeaderDict = None
        self.instanceNumber = 0
        self.today = date.today().strftime("%Y%m%d")
        self.now = datetime.now().strftime("%H%M%S.%f")
        self.serInsUid = None
        self.input_options = {}
        self.output_sort = None
        self.output_dir = None
        self.seriesTime = None

    def getOriginForSlice(self, dictionary, slice):
        """Get origin of given slice.

        Args:
            self: DICOMPlugin instance
            dictionary: image dictionary
            slice: slice number (int)
        Returns:
            z,y,x: coordinate for origin of given slice (np.array)
        """

        origin = self.getDicomAttribute(dictionary, tag_for_keyword("ImagePositionPatient"), slice)
        if origin is not None:
            x = float(origin[0])
            y = float(origin[1])
            z = float(origin[2])
            return np.array([z, y, x])
        return None

    def extractDicomAttributes(self, dictionary, hdr):
        """Extract DICOM attributes

        Args:
            self: DICOMPlugin instance
            dictionary: image dictionary
            hdr: header
        Returns:
            hdr: header
                - seriesNumber
                - seriesDescription
                - imageType
                - spacing
                - orientation
                - imagePositions
                - axes
                - modality, laterality, protocolName, bodyPartExamined
                - seriesDate, seriesTime, patientPosition
        """
        attributes = [
            'patientName', 'patientID', 'patientBirthDate',
            'studyInstanceUID', 'studyID',
            'seriesInstanceUID', 'frameOfReferenceUID',
            'seriesDate', 'seriesTime', 'seriesNumber', 'seriesDescription',
            'imageType', 'accessionNumber',
            'modality', 'laterality',
            'protocolName', 'bodyPartExamined', 'patientPosition',
            'SOPClassUID'
        ]
        for attribute in attributes:
            dicom_attribute = attribute[0].upper() + attribute[1:]
            setattr(hdr, attribute,
                    self.getDicomAttribute(dictionary, tag_for_keyword(dicom_attribute))
                    )

        hdr.spacing = self.__get_voxel_spacing(dictionary)

        # Image position (patient)
        # Reverse orientation vectors from (x,y,z) to (z,y,x)
        iop = self.getDicomAttribute(dictionary, tag_for_keyword("ImageOrientationPatient"))
        if iop is not None:
            hdr.orientation = np.array((iop[2], iop[1], iop[0],
                                        iop[5], iop[4], iop[3]))

        # Extract imagePositions
        hdr.imagePositions = {}
        for _slice in dictionary:
            hdr.imagePositions[_slice] = self.getOriginForSlice(dictionary, _slice)

    def __get_voxel_spacing(self, dictionary):
        # Spacing
        pixel_spacing = self.getDicomAttribute(dictionary, tag_for_keyword("PixelSpacing"))
        dy = 1.0
        dx = 1.0
        if pixel_spacing is not None:
            # Notice that DICOM row spacing comes first, column spacing second!
            dy = float(pixel_spacing[0])
            dx = float(pixel_spacing[1])
        try:
            dz = float(self.getDicomAttribute(dictionary, tag_for_keyword("SpacingBetweenSlices")))
        except TypeError:
            try:
                dz = float(self.getDicomAttribute(dictionary, tag_for_keyword("SliceThickness")))
            except TypeError:
                dz = 1.0
        return np.array([dz, dy, dx])

    # noinspection PyPep8Naming
    def setDicomAttribute(self, dictionary, tag, value):
        """Set a given DICOM attribute to the provided value.

        Ignore if no real dicom header exists.

        Args:
            self: DICOMPlugin instance
            dictionary: image dictionary
            tag: DICOM tag of addressed attribute.
            value: Set attribute to this value.
        """
        if dictionary is not None:
            for _slice in dictionary:
                for tg, fname, im in dictionary[_slice]:
                    if tag not in im:
                        VR = pydicom.datadict.dictionary_VR(tag)
                        im.add_new(tag, VR, value)
                    else:
                        im[tag].value = value

    def getDicomAttribute(self, dictionary, tag, slice=0):
        """Get DICOM attribute from first image for given slice.

        Args:
            self: DICOMPlugin instance
            dictionary: image dictionary
            tag: DICOM tag of requested attribute.
            slice: which slice to access. Default: slice=0
        """
        # logger.debug("getDicomAttribute: tag", tag, ", slice", slice)
        assert dictionary is not None, "dicomplugin.getDicomAttribute: dictionary is None"
        tg, fname, im = dictionary[slice][0]
        if tag in im:
            return im[tag].value
        else:
            return None

    def removePrivateTags(self, dictionary):
        """Remove private DICOM attributes.

        Ignore if no real dicom header exists.

        Args:
            self: DICOMPlugin instance
            dictionary: image dictionary
        """
        if dictionary is not None:
            for _slice in dictionary:
                for tg, fname, im in dictionary[_slice]:
                    im.remove_private_tags()

    def read(self, sources, pre_hdr, input_order, opts):
        """Read image data

        Args:
            self: DICOMPlugin instance
            sources: list of sources to image data
            pre_hdr: Pre-filled header dict. Can be None
            input_order: sort order
            opts: input options (dict)
        Returns:
            Tuple of
                - hdr: Header
                    - input_format
                    - input_order
                    - slices
                    - sliceLocations
                    - DicomHeaderDict
                    - keep_uid
                    - tags
                    - seriesNumber
                    - seriesDescription
                    - imageType
                    - spacing
                    - orientation
                    - imagePositions
                - si[tag,slice,rows,columns]: multi-dimensional numpy array
        """

        self.input_order = input_order

        skip_pixels = False
        if 'headers_only' in opts and opts['headers_only']:
            skip_pixels = True

        # Read DICOM headers
        logger.debug('DICOMPlugin.read: sources %s' % sources)
        # pydicom.config.debug(True)
        try:
            hdr, si = self.read_files(sources, input_order, opts, skip_pixels=skip_pixels)
        except CannotSort:
            raise
        except Exception as e:
            logger.debug('DICOMPlugin.read: exception\n%s' % e)
            raise NotImageError('{}'.format(e))
        # pydicom.config.debug(False)

        # logger.debug("SOPClassUID: {}".format(
        #     self.getDicomAttribute(hdr.DicomHeaderDict, tag_for_keyword("SOPClassUID"))))
        # logger.debug("TransferSyntaxUID: {}".format(
        #     self.getDicomAttribute(hdr.DicomHeaderDict, tag_for_keyword("TransferSyntaxUID"))))

        if 'correct_acq' in opts and opts['correct_acq']:
            si = self.correct_acqtimes_for_dynamic_series(hdr, si)

        # Add any DICOM template
        if pre_hdr is not None:
            hdr.update(pre_hdr)

        return hdr, si

    @staticmethod
    def _get_pixels_with_shape(im, shape):
        """Get pixels from image object. Reshape image to given shape

        Args:
            im: dicom image
            shape: requested image shape
        Returns:
            si: numpy array of given shape
        """

        _use_float = False
        try:
            # logger.debug("Set si[{}]".format(idx))
            if 'RescaleSlope' in im and 'RescaleIntercept' in im:
                _use_float = abs(im.RescaleSlope - 1) > 1e-4 or abs(im.RescaleIntercept) > 1e-4
            if _use_float:
                pixels = float(im.RescaleSlope) * im.pixel_array.astype(float) +\
                         float(im.RescaleIntercept)
            else:
                pixels = im.pixel_array
            if shape != pixels.shape:
                # This happens only when images in a series have varying shape
                # Place the pixels in the upper left corner of the matrix
                assert len(shape) == len(pixels.shape), \
                    "Shape of matrix ({}) differ from pixel shape ({})".format(
                        shape, pixels.shape)
                # Assume that pixels can be expanded to match si shape
                si = np.zeros(shape, pixels.dtype)
                roi = []
                for d in pixels.shape:
                    roi.append(slice(d))
                roi = tuple(roi)
                si[roi] = pixels
            else:
                si = pixels
        except UnboundLocalError:
            # A bug in pydicom appears when reading binary images
            if im.BitsAllocated == 1:
                logger.debug(
                    "Binary image, image.shape={}, image shape=({},{},{})".format(
                        im.shape, im.NumberOfFrames, im.Rows, im.Columns))
                # try:
                #    image.decompress()
                # except NotImplementedError as e:
                #    logger.error("Cannot decompress pixel data: {}".format(e))
                #    raise
                _myarr = np.frombuffer(im.PixelData, dtype=np.uint8)
                # Reverse bit order, and copy the array to get a
                # contiguous array
                bits = np.unpackbits(_myarr).reshape(-1, 8)[:, ::-1].copy()
                si = np.fliplr(
                    bits.reshape(
                        1, im.NumberOfFrames, im.Rows, im.Columns))
                if _use_float:
                    si = float(im.RescaleSlope) * si + float(im.RescaleIntercept)
            else:
                raise
        # Delete pydicom's pixel data to save memory
        # image._pixel_array = None
        # if 'PixelData' in image:
        #    image[0x7fe00010].value = None
        #    image[0x7fe00010].is_undefined_length = True
        return si

    def _read_image(self, f, opts, hdr):
        """Read image data from given file handle

        Args:
            self: format plugin instance
            f: file handle or filename (depending on self._need_local_file)
            opts: Input options (dict)
            hdr: Header
        Returns:
            Tuple of
                - hdr: Header
                    Return values:
                    - info: Internal data for the plugin
                          None if the given file should not be included (e.g. raw file)
                - si: numpy array (multi-dimensional)
        """

        pass

    def _set_tags(self, image_list, hdr, si):
        """Set header tags.

        Args:
            self: format plugin instance
            image_list: list with (info,img) tuples
            hdr: Header
            si: numpy array (multi-dimensional)
        Returns:
            hdr: Header
        """

        pass

    def read_files(self, sources, input_order, opts, skip_pixels=False):
        """Read DICOM objects

        Args:
            self: DICOMPlugin instance
            sources: list of sources to image data
            input_order: sort order
            opts: input options (dict)
            skip_pixels: Do not read pixel data (default: False)
        Returns:
            Tuple of
                - hdr: header
                - si: numpy pixel matrix
        """

        logger.debug('DICOMPlugin.read_files: sources %s' % sources)
        try:
            image_dict, hdr, shape = self.get_dicom_files(sources, input_order, opts,
                                                          skip_pixels=skip_pixels)
        except Exception as e:
            logger.debug(
                'DICOMPlugin.read_files: exception get_dicom_files: {} {}'.format(
                    type(e), e))
            # import traceback
            # traceback.print_exc()
            raise
        # image_dict: full dataset with headers and full pixel data
        # hdr: most of dataset, excluding pixel data
        # shape: expected shape of pixel matrix

        if 'separate_series' in opts and opts['separate_series']:
            hdr = {}
            si = {}
            for imdict, h, shape in image_dict:
                self.extractDicomAttributes(imdict, h)
                setattr(h, 'keep_uid', True)
                hdr[h.seriesInstanceUID] = h
                if skip_pixels:
                    si[h.seriesInstanceUID] = None
                else:
                    # Extract pixel data
                    si[h.seriesInstanceUID] = self.construct_pixel_array(
                        imdict, h, shape, opts=opts)

                del imdict
        else:
            if skip_pixels:
                si = None
            else:
                # Extract pixel data
                si = self.construct_pixel_array(image_dict, hdr, shape, opts=opts)

            self.extractDicomAttributes(image_dict, hdr)
            setattr(hdr, 'keep_uid', True)
            del image_dict

        return hdr, si

    def construct_pixel_array(self, image_dict, hdr, shape, opts=None):
        opts = {} if opts is None else opts
        # Look-up first image to determine pixel type
        # tag, member_name, im = hdr.DicomHeaderDict[0][0]
        tag, member_name, im = image_dict[0][0]
        # print('read: im 0: refcount {}'.format(sys.getrefcount(im)))
        hdr.photometricInterpretation = 'MONOCHROME2'
        if 'PhotometricInterpretation' in im:
            hdr.photometricInterpretation = im.PhotometricInterpretation
        matrix_dtype = np.uint16
        if 'PixelRepresentation' in im:
            if im.PixelRepresentation == 1:
                matrix_dtype = np.int16
        if 'RescaleSlope' in im and 'RescaleIntercept' in im and \
                (abs(im.RescaleSlope - 1) > 1e-4 or abs(im.RescaleIntercept) > 1e-4):
            matrix_dtype = float
        elif im.BitsAllocated == 8:
            matrix_dtype = np.uint8
        logger.debug("DICOMPlugin.read: matrix_dtype %s" % matrix_dtype)
        _color = 1 if hdr.color else 0

        # Load DICOM image data
        logger.debug('DICOMPlugin.read: shape {}'.format(shape))
        si = np.zeros(shape, matrix_dtype)

        for _slice in image_dict:
            # noinspection PyUnusedLocal
            # _done = [False for x in range(len(hdr.DicomHeaderDict[_slice]))]
            _done = [False for x in range(len(image_dict[_slice]))]
            # for tag, member_name, im in hdr.DicomHeaderDict[_slice]:
            for tag, member_name, im in image_dict[_slice]:
                # print('read: im 1: refcount {}'.format(sys.getrefcount(im)))
                tgs = hdr.tags[_slice]
                idx = np.where(tgs == tag)[0][0]
                if _done[idx] and \
                        'AcceptDuplicateTag' in opts and \
                        opts['AcceptDuplicateTag'] == 'True':
                    while _done[idx]:
                        idx += 1
                _done[idx] = True
                if 'NumberOfFrames' in im:
                    if im.NumberOfFrames == 1:
                        idx = (idx, _slice)
                else:
                    idx = (idx, _slice)
                # Simplify index when image is 3D, remove tag index
                if si.ndim == 3 + _color:
                    idx = idx[1:]
                # Do not read file again
                # with archive.open(member, mode='rb') as f:
                #     if issubclass(type(f), pydicom.dataset.Dataset):
                #         im = f
                #     else:
                #         im = pydicom.filereader.dcmread(f)
                try:
                    im.decompress()
                except NotImplementedError as e:
                    logger.error("Cannot decompress pixel data: {}".format(e))
                    raise
                try:
                    si[idx] = self._get_pixels_with_shape(im, si[idx].shape)
                except Exception as e:
                    logger.warning("Cannot read pixel data: {}".format(e))
                    raise
                del im

        # Simplify shape
        self._reduce_shape(si, hdr.axes)
        logger.debug('DICOMPlugin_read_files.construct_pixel_array: si {}'.format(si.shape))

        return si

    def get_dicom_files(self, sources, input_order, opts=None, skip_pixels=False):
        """Get DICOM objects.

        Args:
            self: DICOMPlugin instance
            sources: list of sources to image data
            input_order: Determine how to sort the input images
            opts: options (dict)
            skip_pixels: Do not read pixel data (default: False)
        Returns:
            Tuple of
                - sorted_headers: dict where sliceLocations are keys
                - hdr: Header
                - shape: tuple
        """
        logger.debug("DICOMPlugin.get_dicom_files: sources: {} {}".format(
            type(sources), sources))

        image_dict = {}
        for source in sources:
            archive = source['archive']
            scan_files = source['files']
            logger.debug("DICOMPlugin.get_dicom_files: archive: {}".format(archive))
            # if scan_files is None or len(scan_files) == 0:
            #     scan_files = ['*']
            logger.debug("get_dicom_files: source: {} {}".format(type(source), source))
            logger.debug("get_dicom_files: scan_files: {}".format(scan_files))
            for path in archive.getnames(scan_files):
                logger.debug("get_dicom_files: member: {}".format(path))
                if os.path.basename(path) == "DICOMDIR":
                    continue
                # logger.debug("get_dicom_files: calling archive.getmembers: {}".format(
                #     len(path)))
                member = archive.getmembers([path, ])
                # logger.debug("get_dicom_files: returned from archive.getmembers: {}".format(
                #     len(member)))
                if len(member) != 1:
                    raise IndexError('Should not be multiple files for a filename')
                member = member[0]
                try:
                    with archive.open(member, mode='rb') as f:
                        logger.debug('DICOMPlugin.get_dicom_files: process_member {}'.format(
                            member))
                        self.process_member(image_dict, archive, path, f, opts,
                                            skip_pixels=skip_pixels)
                except Exception as e:
                    logger.debug('DICOMPlugin.get_dicom_files: Exception {}'.format(e))
                    # raise
        if 'separate_series' in opts and opts['separate_series']:
            sorted_list = []
            for uid in image_dict:
                try:
                    sorted_list.append(self.sort_images(image_dict[uid], input_order, opts))
                except Exception as e:
                    print('WARNING: Skipping {}: {}'.format(uid, e))
                    pass
            return sorted_list, None, None
        else:
            return self.sort_images(image_dict, input_order, opts)

    def sort_images(self, header_dict, input_order, opts):
        """Sort DICOM images.

        Args:
            self: DICOMPlugin instance
            header_dict: dict where sliceLocations are keys
            input_order: determine how to sort the input images
            opts: options (dict)
        Returns:
            Tuple of
                - hdr
                    - input_format
                    - input_order
                    - slices
                    - sliceLocations
                    - DicomHeaderDict
                    - tags
                - shape
        """

        def _copy_headers(sorted_headers):
            def all_except_pixeldata_callback(dataset, data_element):
                if data_element.tag.group == 0x7fe0:
                    pass
                else:
                    ds[data_element.tag] = dataset[data_element.tag]

            headers = {}
            for s in sorted(sorted_headers):
                headers[s] = []
                for tg, member_name, im in sorted_headers[s]:
                    ds = self.construct_basic_dicom()
                    im.walk(all_except_pixeldata_callback)
                    headers[s].append((tg, member_name, ds))
            return headers

        hdr = Header()
        hdr.input_format = 'dicom'
        # hdr.input_order = input_order
        sliceLocations = sorted(header_dict)
        # hdr.slices = len(sliceLocations)
        hdr.sliceLocations = sliceLocations

        # Verify same number of images for each slice
        if len(header_dict) == 0:
            raise ValueError("No DICOM images found.")
        count = np.zeros(len(header_dict), dtype=int)
        islice = 0
        for sloc in sorted(header_dict):
            count[islice] += len(header_dict[sloc])
            islice += 1
        logger.debug("sort_images: tags per slice: {}".format(count))
        accept_uneven_slices = accept_duplicate_tag = False
        if 'accept_uneven_slices' in opts and \
                opts['accept_uneven_slices'] == 'True':
            accept_uneven_slices = True
        if 'accept_duplicate_tag' in opts and \
                opts['accept_duplicate_tag'] == 'True':
            accept_duplicate_tag = True
        if min(count) != max(count) and accept_uneven_slices:
            logger.error("sort_images: tags per slice: {}".format(count))
            raise UnevenSlicesError("Different number of images in each slice.")

        if input_order == INPUT_ORDER_AUTO:
            input_order = self.auto_sort(header_dict, opts)

        hdr.input_order = input_order

        # Extract all tags and sort them per slice
        tag_list = {}
        islice = 0
        for sloc in sorted(header_dict):
            tag_list[islice] = []
            i = 0
            for archive, filename, im in sorted(header_dict[sloc]):
                try:
                    tag = self._get_tag(im, input_order, opts)
                except KeyError:
                    if input_order == INPUT_ORDER_FAULTY:
                        tag = i
                    else:
                        raise CannotSort('Tag not found in dataset')
                except CannotSort:
                    raise
                except Exception:
                    raise
                if tag is None:
                    raise CannotSort("Tag {} not found in data".format(input_order))
                if tag not in tag_list[islice] or accept_duplicate_tag:
                    tag_list[islice].append(tag)
                else:
                    raise CannotSort("Duplicate tag ({}): {}".format(input_order, tag))
                i += 1
            islice += 1
        for islice in range(len(header_dict)):
            tag_list[islice] = sorted(tag_list[islice])
        # Sort images based on position in tag_list
        sorted_headers = {}
        islice = 0
        # Allow for variable sized slices
        frames = None
        rows = columns = 0
        i = 0
        for sloc in sorted(header_dict):
            # Pre-fill sorted_headers
            sorted_headers[islice] = [False for _ in range(count[islice])]
            for archive, filename, im in sorted(header_dict[sloc]):
                if input_order == INPUT_ORDER_FAULTY:
                    tag = i
                else:
                    try:
                        tag = self._get_tag(im, input_order, opts)
                    except CannotSort:
                        raise
                idx = tag_list[islice].index(tag)
                if sorted_headers[islice][idx]:
                    # Duplicate tag
                    if accept_duplicate_tag:
                        while sorted_headers[islice][idx]:
                            idx += 1
                    else:
                        print("WARNING: Duplicate tag", tag)
                # sorted_headers[islice].insert(idx, (tag, (archive,filename), image))
                # noinspection PyTypeChecker
                sorted_headers[islice][idx] = (tag, (archive, filename), im)
                rows = max(rows, im.Rows)
                columns = max(columns, im.Columns)
                if 'NumberOfFrames' in im:
                    frames = im.NumberOfFrames
                i += 1
            islice += 1
        hdr.DicomHeaderDict = _copy_headers(sorted_headers)
        # hdr.seriesInstanceUID = self.getDicomAttribute(hdr.DicomHeaderDict, 'SeriesInstanceUID')
        # hdr.SOPClassUID = self.getDicomAttribute(hdr.DicomHeaderDict, 'SOPClassUID')
        hdr.tags = {}
        for _slice in range(len(tag_list)):
            hdr.tags[_slice] = np.array(tag_list[_slice])
        nz = len(header_dict)
        if frames is not None and frames > 1:
            nz = frames
        if len(tag_list[0]) > 1:
            shape = (len(tag_list[0]), nz, rows, columns)
        else:
            shape = (nz, rows, columns)
        spacing = self.__get_voxel_spacing(sorted_headers)
        ipp = self.getDicomAttribute(hdr.DicomHeaderDict, tag_for_keyword('ImagePositionPatient'))
        if ipp is not None:
            ipp = np.array(list(map(float, ipp)))[::-1]  # Reverse xyz
        else:
            ipp = np.array([0, 0, 0])
        axes = list()
        if len(tag_list[0]) > 1:
            axes.append(
                VariableAxis(
                    input_order_to_dirname_str(input_order),
                    tag_list[0])
            )
        axes.append(UniformLengthAxis(
            'slice',
            ipp[0],
            nz,
            spacing[0]))
        axes.append(UniformLengthAxis(
            'row',
            ipp[1],
            rows,
            spacing[1]))
        axes.append(UniformLengthAxis(
            'column',
            ipp[2],
            columns,
            spacing[2]))
        hdr.color = False
        if 'SamplesPerPixel' in im and im.SamplesPerPixel == 3:
            hdr.color = True
            shape = shape + (im.SamplesPerPixel,)
            axes.append(
                VariableAxis(
                    'rgb',
                    ['r', 'g', 'b']
                )
            )
        hdr.axes = axes
        return sorted_headers, hdr, shape

    def auto_sort(self, header_dict, opts):
        def _single_slice_over_time(tags):
            """If time and slice both varies, the time stamps address slices of a single volume
            """
            count_time = {}
            count_sloc = {}
            for time, sloc in tags:
                if time not in count_time:
                    count_time[time] = 0
                if sloc not in count_sloc:
                    count_sloc[sloc] = 0
                count_time[time] += 1
                count_sloc[sloc] += 1
            max_time = max(count_time.values())
            max_sloc = max(count_sloc.values())
            return max_time == 1 and max_sloc == 1

        extended_tags = {}
        found_tags = {}
        for sloc in sorted(header_dict):
            for archive, filename, im in sorted(header_dict[sloc]):
                for order in ['time', 'b', 'fa', 'te']:
                    try:
                        tag = self._get_tag(im, order, opts)
                        if tag is None:
                            continue
                        if order not in found_tags:
                            found_tags[order] = []
                            extended_tags[order] = []
                        if tag not in found_tags[order]:
                            found_tags[order].append(tag)
                            extended_tags[order].append((tag, sloc))
                    except (KeyError, TypeError, CannotSort):
                        pass

        # Determine how to sort
        actual_order = None
        for order in found_tags:
            if len(found_tags[order]) > 1:
                if actual_order == 'time' and order in ['b', 'te']:
                    # DWI images will typically have varying time.
                    # Let b values override time stamps.
                    actual_order = order
                elif actual_order is None:
                    actual_order = order
                else:
                    raise CannotSort('Cannot auto-sort: {}'.format(extended_tags))
        if actual_order is None:
            actual_order = INPUT_ORDER_NONE
        elif actual_order == INPUT_ORDER_TIME and _single_slice_over_time(extended_tags['time']):
            actual_order = INPUT_ORDER_NONE
        return actual_order

    def process_member(self, image_dict, archive, member_name, member, opts, skip_pixels=False):
        if issubclass(type(member), pydicom.dataset.Dataset):
            im = member
        else:
            try:
                im = pydicom.filereader.dcmread(member, stop_before_pixels=skip_pixels)
            except pydicom.errors.InvalidDicomError:
                return

        if 'input_serinsuid' in opts and opts['input_serinsuid']:
            if im.SeriesInstanceUID != opts['input_serinsuid']:
                return
        if 'input_echo' in opts and opts['input_echo']:
            if int(im.EchoNumbers) != int(opts['input_echo']):
                return

        try:
            sloc = float(im.SliceLocation)
        except AttributeError:
            logger.debug('DICOMPlugin.process_member: Calculate SliceLocation')
            try:
                sloc = self._calculate_slice_location(im)
            except ValueError:
                sloc = 0
        logger.debug('DICOMPlugin.process_member: {} SliceLocation {}'.format(member, sloc))

        if 'separate_series' in opts and opts['separate_series']:
            # Catalog images with uids as key
            uids = (im.PatientName, im.PatientID, im.StudyInstanceUID, im.SeriesInstanceUID)
            if uids not in image_dict:
                image_dict[uids] = {}
            my_dict = image_dict[uids]
        else:
            my_dict = image_dict
        if sloc not in my_dict:
            my_dict[sloc] = []
        my_dict[sloc].append((archive, member_name, im))
        # logger.debug("process_member: added sloc {} {}".format(sloc, member_name))
        # logger.debug("process_member: image_dict len: {}".format(len(image_dict)))
        del im

    def correct_acqtimes_for_dynamic_series(self, hdr, si):
        # si[t,slice,rows,columns]

        # Extract acqtime for each image
        slices = len(hdr.sliceLocations)
        timesteps = self._count_timesteps(hdr)
        logger.info(
            "Slices: %d, apparent time steps: %d, actual time steps: %d" % (
                slices, len(hdr.tags), timesteps))
        new_shape = (timesteps, slices, si.shape[2], si.shape[3])
        newsi = np.zeros(new_shape, dtype=si.dtype)
        acq = np.zeros([slices, timesteps])
        for _slice in hdr.DicomHeaderDict:
            t = 0
            for tg, fname, im in hdr.DicomHeaderDict[_slice]:
                # logger.debug(_slice, tg, fname)
                acq[_slice, t] = tg
                t += 1

        # Correct acqtimes by setting acqtime for each slice of a volume to
        # the smallest time
        for t in range(acq.shape[1]):
            min_acq = np.min(acq[:, t])
            for _slice in range(acq.shape[0]):
                acq[_slice, t] = min_acq

        # Set new acqtime for each image
        for _slice in hdr.DicomHeaderDict:
            t = 0
            for tg, fname, im in hdr.DicomHeaderDict[_slice]:
                im.AcquisitionTime = "%f" % acq[_slice, t]
                newsi[t, _slice, :, :] = si[t, _slice, :, :]
                t += 1

        # Update taglist in hdr
        hdr.tags = {}
        for _slice in hdr.DicomHeaderDict:
            hdr.tags[_slice] = np.empty((acq.shape[1],))
            for t in range(acq.shape[1]):
                hdr.tags[_slice][t] = acq[0, t]
        return newsi

    # noinspection PyArgumentList
    @staticmethod
    def _count_timesteps(hdr):
        slices = len(hdr.sliceLocations)
        timesteps = np.zeros([slices], dtype=int)
        for _slice in hdr.DicomHeaderDict:
            # for tg, fname, image in hdr.DicomHeaderDict[_slice]:
            # for _ in hdr.DicomHeaderDict[_slice]:
            #    timesteps[_slice] += 1
            timesteps[_slice] = len(hdr.DicomHeaderDict[_slice])
            if timesteps.min() != timesteps.max():
                raise ValueError("Number of time steps ranges from %d to %d." % (
                    timesteps.min(), timesteps.max()))
        return timesteps.max()

    def write_3d_numpy(self, si, destination, opts):
        """Write 3D Series image as DICOM files

        Args:
            self: DICOMPlugin instance
            si: Series array (3D or 4D)
            destination: dict of archive and filenames
            opts: Output options (dict)
        """

        logger.debug('DICOMPlugin.write_3d_numpy: destination {}'.format(destination))
        archive = destination['archive']
        filename_template = 'Image_%05d.dcm'
        logger.debug('DICOMPlugin.write_3d_numpy: destination files {}'.format(
            destination['files']))
        if len(destination['files']) > 0 and len(destination['files'][0]) > 0:
            filename_template = destination['files'][0]
        logger.debug('DICOMPlugin.write_3d_numpy: filename_template={}'.format(filename_template))
        self.keep_uid = False if 'keep_uid' not in opts else opts['keep_uid']

        self.instanceNumber = 0

        _ndim = si.ndim
        try:
            if si.color:
                _ndim -= 1
        except AttributeError:
            pass
        logger.debug('DICOMPlugin.write_3d_numpy: orig shape {}, slices {} len {}'.format(
            si.shape, si.slices, _ndim))
        assert _ndim == 2 or _ndim == 3, \
            "write_3d_series: input dimension %d is not 2D/3D." % _ndim

        self._calculate_rescale(si)
        logger.info("Smallest pixel value in series: {}".format(self.smallestPixelValueInSeries))
        logger.info("Largest  pixel value in series: {}".format(self.largestPixelValueInSeries))
        self.today = date.today().strftime("%Y%m%d")
        self.now = datetime.now().strftime("%H%M%S.%f")
        # Set series instance UID when writing
        if not self.keep_uid:
            si.header.seriesInstanceUID = si.header.new_uid()
        self.serInsUid = si.header.seriesInstanceUID
        logger.debug("write_3d_series {}".format(self.serInsUid))
        self.input_options = opts

        if pydicom.uid.UID(si.SOPClassUID).keyword == 'EnhancedMRImageStorage' or \
                pydicom.uid.UID(si.SOPClassUID).keyword == 'EnhancedCTImageStorage':
            # Write Enhanced CT/MR
            self.write_enhanced(si, archive, filename_template)
        else:
            # Either legacy CT/MR, or another modality
            ifile = 0
            if _ndim < 3:
                logger.debug('DICOMPlugin.write_3d_numpy: write 2D ({})'.format(_ndim))
                try:
                    filename = filename_template % 0
                except TypeError:
                    filename = filename_template
                self.write_slice(0, 0, si, archive, filename, ifile)
            else:
                logger.debug('DICOMPlugin.write_3d_numpy: write 3D slices {}'.format(si.slices))
                for _slice in range(si.slices):
                    try:
                        # Interpret parameter substitution in filename_template
                        filename = filename_template % _slice
                    except TypeError:
                        filename = filename_template + "_{}".format(_slice)
                    try:
                        self.write_slice(0, _slice, si[_slice], archive, filename, ifile)
                    except Exception as e:
                        print('DICOMPlugin.write_slice Exception: {}'.format(e))
                        traceback.print_exc(file=sys.stdout)
                        raise
                    ifile += 1

    def write_4d_numpy(self, si, destination, opts):
        """Write 4D Series image as DICOM files

        si.series_number is inserted into each dicom object

        si.series_description is inserted into each dicom object

        si.image_type: Dicom image type attribute

        opts['output_sort']: Which tag will sort the output images (slice or tag)

        opts['output_dir']: Store all images in a single or multiple directories

        Args:
            self: DICOMPlugin instance
            si: Series array si[tag,slice,rows,columns]
            destination: dict of archive and filenames
            opts: Output options (dict)

        """

        logger.debug('DICOMPlugin.write_4d_numpy: destination {}'.format(destination))
        archive = destination['archive']
        filename_template = 'Image_%05d.dcm'
        if len(destination['files']) > 0 and len(destination['files'][0]) > 0:
            filename_template = destination['files'][0]
        self.keep_uid = False if 'keep_uid' not in opts else opts['keep_uid']

        self.DicomHeaderDict = si.DicomHeaderDict

        # Defaults
        self.output_sort = SORT_ON_SLICE
        if 'output_sort' in opts:
            self.output_sort = opts['output_sort']
        self.output_dir = 'single'
        if 'output_dir' in opts:
            self.output_dir = opts['output_dir']

        self.instanceNumber = 0

        _ndim = si.ndim
        try:
            if si.color:
                _ndim -= 1
        except AttributeError:
            pass
        logger.debug('DICOMPlugin.write_4d_numpy: orig shape {}, len {}'.format(si.shape, _ndim))
        assert _ndim == 4, "write_4d_series: input dimension %d is not 4D." % _ndim

        steps = si.shape[0]
        self._calculate_rescale(si)
        logger.info("Smallest pixel value in series: {}".format(
            self.smallestPixelValueInSeries))
        logger.info("Largest  pixel value in series: {}".format(
            self.largestPixelValueInSeries))
        self.today = date.today().strftime("%Y%m%d")
        self.now = datetime.now().strftime("%H%M%S.%f")
        # Not used # self.seriesTime = obj.getDicomAttribute(tag_for_keyword("AcquisitionTime"))
        # Set series instance UID when writing
        if not self.keep_uid:
            si.header.seriesInstanceUID = si.header.new_uid()
        self.serInsUid = si.header.seriesInstanceUID
        self.input_options = opts

        if pydicom.uid.UID(si.SOPClassUID).keyword == 'EnhancedMRImageStorage' or \
                pydicom.uid.UID(si.SOPClassUID).keyword == 'EnhancedCTImageStorage':
            # Write Enhanced CT/MR
            self.write_enhanced(si, archive, filename_template)
        else:
            # Either legacy CT/MR, or another modality
            if self.output_sort == SORT_ON_SLICE:
                ifile = 0
                digits = len("{}".format(steps))
                for tag in range(steps):
                    for _slice in range(si.slices):
                        if self.output_dir == 'single':
                            # Interpret parameter substitution in filename_template
                            filename = filename_template % ifile
                        else:  # self.output_dir == 'multi'
                            dirn = "{0}{1:0{2}}".format(
                                input_order_to_dirname_str(si.input_order),
                                tag, digits)
                            if _slice == 0:
                                # Restart file number in each subdirectory
                                ifile = 0
                            filename = os.path.join(dirn,
                                                    filename_template % ifile)
                        try:
                            self.write_slice(tag, _slice, si[tag, _slice],
                                             archive, filename, ifile)
                        except Exception as e:
                            print('DICOMPlugin.write_slice Exception: {}'.format(e))
                            traceback.print_exc(file=sys.stdout)
                            raise
                        ifile += 1
            else:  # self.output_sort == SORT_ON_TAG:
                ifile = 0
                digits = len("{}".format(si.slices))
                for _slice in range(si.slices):
                    for tag in range(steps):
                        if self.output_dir == 'single':
                            # Interpret parameter substitution in filename_template
                            filename = filename_template % ifile
                        else:  # self.output_dir == 'multi'
                            dirn = "slice{0:0{1}}".format(_slice, digits)
                            if tag == 0:
                                # Restart file number in each subdirectory
                                ifile = 0
                            filename = os.path.join(dirn,
                                                    filename_template % ifile)
                        try:
                            self.write_slice(tag, _slice, si[tag, _slice],
                                             archive, filename, ifile)
                        except Exception as e:
                            print('DICOMPlugin.write_slice Exception: {}'.format(e))
                            traceback.print_exc(file=sys.stdout)
                            raise
                        ifile += 1

    def write_enhanced(self, si, archive, filename_template, opts):
        """Write enhanced CT/MR object to DICOM file

        Args:
            self: DICOMPlugin instance
            si: Series instance, including these attributes:
            archive: archive object
            filename_template: file name template, possible without '.dcm' extension
            opts: Output options (dict)
        Raises:

        """
        filename = 'dummy'
        logger.debug("write_enhanced {} {}".format(filename, self.serInsUid))

        # if np.issubdtype(si.dtype, np.floating):
        if si.dtype.kind == 'f':
            safe_si = np.nan_to_num(si)
        else:
            safe_si = si

        try:
            tg, member_name, im = si.DicomHeaderDict[0][0]
        except (KeyError, IndexError):
            raise IndexError("Cannot address dicom_template.DicomHeaderDict[0][0]")
        except ValueError:
            raise NoDICOMAttributes("Cannot write DICOM object when no DICOM attributes exist.")
        logger.debug("write_enhanced member_name {}".format(member_name))
        self.keep_uid = False if 'keep_uid' not in opts else opts['keep_uid']
        if not self.keep_uid:
            si.header.seriesInstanceUID = si.header.new_uid()
        self.serInsUid = si.header.seriesInstanceUID

        ds = self.construct_enhanced_dicom(filename_template, im, safe_si)

        # Add header information
        try:
            ds.SliceLocation = si.sliceLocations[0]
        except (AttributeError, ValueError):
            # Dont know the SliceLocation, attempt to calculate from image geometry
            try:
                ds.SliceLocation = self._calculate_slice_location(im)
            except ValueError:
                # Dont know the SliceLocation, so will set this to be the slice index
                ds.SliceLocation = slice
        try:
            dz, dy, dx = si.spacing
        except ValueError:
            dz, dy, dx = 1, 1, 1
        ds.PixelSpacing = [str(dy), str(dx)]
        ds.SliceThickness = str(dz)
        try:
            ipp = si.imagePositions
            if len(ipp) > 0:
                ipp = ipp[0]
            else:
                ipp = np.array([0, 0, 0])
        except ValueError:
            ipp = np.array([0, 0, 0])
        if ipp.shape == (3, 1):
            ipp.shape = (3,)
        z, y, x = ipp[:]
        ds.ImagePositionPatient = [str(x), str(y), str(z)]
        # Reverse orientation vectors from zyx to xyz
        try:
            ds.ImageOrientationPatient = [
                si.orientation[2], si.orientation[1], si.orientation[0],
                si.orientation[5], si.orientation[4], si.orientation[3]]
        except ValueError:
            ds.ImageOrientationPatient = [0, 0, 1, 0, 1, 0]
        try:
            ds.SeriesNumber = si.seriesNumber
        except ValueError:
            ds.SeriesNumber = 1
        try:
            ds.SeriesDescription = si.seriesDescription
        except ValueError:
            ds.SeriesDescription = ''
        try:
            ds.ImageType = "\\".join(si.imageType)
        except ValueError:
            ds.ImageType = 'DERIVED\\SECONDARY'
        try:
            ds.FrameOfReferenceUID = si.frameOfReferenceUID
        except ValueError:
            pass

        ds.SmallestPixelValueInSeries = np.uint16(self.smallestPixelValueInSeries)
        ds.LargestPixelValueInSeries = np.uint16(self.largestPixelValueInSeries)
        ds[0x0028, 0x0108].VR = 'US'
        ds[0x0028, 0x0109].VR = 'US'
        ds.WindowCenter = self.center
        ds.WindowWidth = self.width
        if safe_si.dtype in self.smallint or np.issubdtype(safe_si.dtype, np.bool_):
            ds.SmallestImagePixelValue = np.uint16(safe_si.min().astype('uint16'))
            ds.LargestImagePixelValue = np.uint16(safe_si.max().astype('uint16'))
            if 'RescaleSlope' in ds:
                del ds.RescaleSlope
            if 'RescaleIntercept' in ds:
                del ds.RescaleIntercept
        else:
            ds.SmallestImagePixelValue = np.uint16((safe_si.min().item() - self.b) / self.a)
            ds.LargestImagePixelValue = np.uint16((safe_si.max().item() - self.b) / self.a)
            try:
                ds.RescaleSlope = "%f" % self.a
            except OverflowError:
                ds.RescaleSlope = "%d" % int(self.a)
            ds.RescaleIntercept = "%f" % self.b
        ds[0x0028, 0x0106].VR = 'US'
        ds[0x0028, 0x0107].VR = 'US'
        # General Image Module Attributes
        ds.InstanceNumber = 1
        ds.ContentDate = self.today
        ds.ContentTime = self.now
        # ds.AcquisitionTime = self.add_time(self.seriesTime, timeline[tag])
        ds.Rows = si.rows
        ds.Columns = si.columns
        self._insert_pixeldata(ds, safe_si)
        # logger.debug("write_enhanced: filename {}".format(filename))

        # Set tag
        # safe_si will always have only the present tag
        self._set_dicom_tag(ds, safe_si.input_order, safe_si.tags[0])

        if len(os.path.splitext(filename)[1]) > 0:
            fn = filename
        else:
            fn = filename + '.dcm'
        logger.debug("write_enhanced: filename {}".format(fn))
        # if archive.transport.name == 'dicom':
        #     # Store dicom set ds directly
        #     archive.transport.store(ds)
        # else:
        #     # Store dicom set ds as file
        #     with archive.open(fn, 'wb') as f:
        #         ds.save_as(f, write_like_original=False)
        raise ValueError("write_enhanced: to be implemented")

    # noinspection PyPep8Naming,PyArgumentList
    def write_slice(self, tag, slice, si, archive, filename, ifile):
        """Write single slice to DICOM file

        Args:
            self: DICOMPlugin instance
            tag: tag index
            slice: slice index
            si: Series instance, including these attributes:
            -   slices
            -   sliceLocations
            -   DicomHeaderDict
            -   tags (not used)
            -   seriesNumber
            -   seriesDescription
            -   imageType
            -   frame
            -   spacing
            -   orientation
            -   imagePositions
            -   photometricInterpretation

            archive: archive object
            filename: file name, possible without '.dcm' extension
            ifile: instance number in series
        """

        logger.debug("write_slice {} {}".format(filename, self.serInsUid))

        # if np.issubdtype(si.dtype, np.floating):
        if si.dtype.kind == 'f':
            safe_si = np.nan_to_num(si)
        else:
            safe_si = si

        try:
            logger.debug("write_slice slice {}, tag {}".format(slice, tag))
            # logger.debug("write_slice {}".format(si.DicomHeaderDict))
            tg, member_name, im = si.DicomHeaderDict[0][0]
            # tg,member_name,image = si.DicomHeaderDict[slice][tag]
        except (KeyError, IndexError, TypeError):
            print('DICOMPlugin.write_slice: DicomHeaderDict: {}'.format(si.DicomHeaderDict))
            raise IndexError("Cannot address dicom_template.DicomHeaderDict[slice=%d][tag=%d]"
                             % (slice, tag))
        # except AttributeError:
        except ValueError:
            raise NoDICOMAttributes("Cannot write DICOM object when no DICOM attributes exist.")
        logger.debug("write_slice member_name {}".format(member_name))
        ds = self.construct_dicom(filename, im, safe_si)
        # self._copy_dicom_group(0x21, im, ds)
        # self._copy_dicom_group(0x29, im, ds)

        # Add header information
        try:
            ds.SliceLocation = pydicom.valuerep.format_number_as_ds(float(si.sliceLocations[0]))
        except (AttributeError, ValueError):
            # Dont know the SliceLocation, attempt to calculate from image geometry
            try:
                ds.SliceLocation =\
                    pydicom.valuerep.format_number_as_ds(self._calculate_slice_location(im))
            except ValueError:
                # Dont know the SliceLocation, so will set this to be the slice index
                ds.SliceLocation = slice
        try:
            dz, dy, dx = si.spacing
        except ValueError:
            dz, dy, dx = 1, 1, 1
        ds.PixelSpacing = [pydicom.valuerep.format_number_as_ds(float(dy)),
                           pydicom.valuerep.format_number_as_ds(float(dx))]
        ds.SliceThickness = pydicom.valuerep.format_number_as_ds(float(dz))
        try:
            ipp = si.imagePositions
            if len(ipp) > 0:
                ipp = ipp[0]
            else:
                ipp = np.array([0, 0, 0])
        except ValueError:
            ipp = np.array([0, 0, 0])
        if ipp.shape == (3, 1):
            ipp.shape = (3,)
        z, y, x = ipp[:]
        ds.ImagePositionPatient = [pydicom.valuerep.format_number_as_ds(float(x)),
                                   pydicom.valuerep.format_number_as_ds(float(y)),
                                   pydicom.valuerep.format_number_as_ds(float(z))]
        # Reverse orientation vectors from zyx to xyz
        try:
            ds.ImageOrientationPatient = [
                pydicom.valuerep.format_number_as_ds(float(si.orientation[2])),
                pydicom.valuerep.format_number_as_ds(float(si.orientation[1])),
                pydicom.valuerep.format_number_as_ds(float(si.orientation[0])),
                pydicom.valuerep.format_number_as_ds(float(si.orientation[5])),
                pydicom.valuerep.format_number_as_ds(float(si.orientation[4])),
                pydicom.valuerep.format_number_as_ds(float(si.orientation[3]))]
        except ValueError:
            ds.ImageOrientationPatient = [0, 0, 1, 0, 0, 1]
        try:
            ds.SeriesNumber = si.seriesNumber
        except ValueError:
            ds.SeriesNumber = 1
        try:
            ds.SeriesDescription = si.seriesDescription
        except ValueError:
            ds.SeriesDescription = ''
        try:
            ds.ImageType = "\\".join(si.imageType)
        except ValueError:
            ds.ImageType = 'DERIVED\\SECONDARY'
        try:
            ds.FrameOfReferenceUID = si.frameOfReferenceUID
        except ValueError:
            pass

        self._set_pixel_rescale(ds, si)

        # General Image Module Attributes
        ds.InstanceNumber = ifile + 1
        ds.ContentDate = self.today
        ds.ContentTime = self.now
        # ds.AcquisitionTime = self.add_time(self.seriesTime, timeline[tag])
        ds.Rows = si.rows
        ds.Columns = si.columns
        self._insert_pixeldata(ds, safe_si)
        # logger.debug("write_slice: filename {}".format(filename))

        # Set tag
        # safe_si will always have only the present tag
        self._set_dicom_tag(ds, safe_si.input_order, safe_si.tags[0])

        if len(os.path.splitext(filename)[1]) > 0:
            fn = filename
        else:
            fn = filename + '.dcm'
        logger.debug("write_slice: filename {}".format(fn))
        if archive.transport.name == 'dicom':
            # Store dicom set ds directly
            archive.transport.store(ds)
        else:
            # Store dicom set ds as file
            with archive.open(fn, 'wb') as f:
                ds.save_as(f, write_like_original=False)

    def construct_basic_dicom(self, template=None, filename='NA', sop_ins_uid=None):

        # Populate required values for file meta information
        file_meta = pydicom.dataset.FileMetaDataset()
        if template is not None:
            file_meta.MediaStorageSOPClassUID = template.SOPClassUID
        if sop_ins_uid is not None:
            file_meta.MediaStorageSOPInstanceUID = sop_ins_uid
        file_meta.ImplementationClassUID = "%s.1" % self.root
        file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

        # Create the FileDataset instance
        # (initially no data elements, but file_meta supplied)
        ds = pydicom.dataset.FileDataset(
            filename,
            {},
            file_meta=file_meta,
            preamble=b"\0" * 128)
        return ds

    def construct_dicom(self, filename, template, si):

        self.instanceNumber += 1
        if not self.keep_uid:
            si.setDicomAttribute('SOPInstanceUID', si.header.new_uid())
        sop_ins_uid = si.getDicomAttribute('SOPInstanceUID')

        # Populate required values for file meta information
        file_meta = pydicom.dataset.FileMetaDataset()
        file_meta.MediaStorageSOPClassUID = template.SOPClassUID
        file_meta.MediaStorageSOPInstanceUID = sop_ins_uid
        file_meta.ImplementationClassUID = "%s.1" % self.root
        file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        # file_meta.FileMetaInformationVersion = int(1).to_bytes(2,'big')
        # file_meta.FileMetaInformationGroupLength = 160

        # print("Setting dataset values...")

        # Create the FileDataset instance
        # (initially no data elements, but file_meta supplied)
        ds = pydicom.dataset.FileDataset(
            filename,
            {},
            file_meta=file_meta,
            preamble=b"\0" * 128)

        # Add the data elements
        # -- not trying to set all required here. Check DICOM standard
        # copy_general_dicom_attributes(template, ds)
        for element in template.iterall():
            if element.tag == 0x7fe00010:
                continue  # Do not copy pixel data, will be added later
            ds.add(element)

        ds.StudyInstanceUID = si.header.studyInstanceUID
        ds.StudyID = si.header.studyID
        # ds.SeriesInstanceUID = si.header.seriesInstanceUID
        ds.SeriesInstanceUID = self.serInsUid
        ds.SOPClassUID = template.SOPClassUID
        ds.SOPInstanceUID = sop_ins_uid

        ds.AccessionNumber = si.header.accessionNumber
        ds.PatientName = si.header.patientName
        ds.PatientID = si.header.patientID
        ds.PatientBirthDate = si.header.patientBirthDate

        # Set the transfer syntax
        ds.is_little_endian = True
        ds.is_implicit_VR = True

        return ds

    @staticmethod
    def _copy_dicom_group(groupno, ds_in, ds_out):
        sub_dataset = ds_in.group_dataset(groupno)
        for data_element in sub_dataset:
            if data_element.VR != "SQ":
                ds_out[data_element.tag] = ds_in[data_element.tag]

    def _insert_pixeldata(self, ds, arr):
        """Insert pixel data into dicom object

        If float array, scale to uint16
        """

        # logger.debug('DICOMPlugin.insert_pixeldata: arr.dtype %s' % arr.dtype)
        # logger.debug('DICOMPlugin.insert_pixeldata: arr.itemsize  %s' % arr.itemsize)

        ds.SamplesPerPixel = 1
        ds.PixelRepresentation = 1 if np.issubdtype(arr.dtype, np.signedinteger) else 0
        try:
            ds.PhotometricInterpretation = arr.photometricInterpretation
            if arr.photometricInterpretation == 'RGB':
                ds.SamplesPerPixel = 3
                ds.PlanarConfiguration = 0
        except ValueError:
            ds.PhotometricInterpretation = 'MONOCHROME2'

        if arr.dtype in self.smallint:
            # No scaling of pixel values
            ds.PixelData = arr.tobytes()
            if arr.itemsize == 1:
                ds[0x7fe0, 0x0010].VR = 'OB'
                ds.BitsAllocated = 8
                ds.BitsStored = 8
                ds.HighBit = 7
            elif arr.itemsize == 2:
                ds[0x7fe0, 0x0010].VR = 'OW'
                ds.BitsAllocated = 16
                ds.BitsStored = 16
                ds.HighBit = 15
            else:
                raise TypeError('Cannot store {} itemsize {} without scaling'.format(
                    arr.dtype, arr.itemsize))
        elif np.issubdtype(arr.dtype, np.bool_):
            # No scaling. Pack bits in 16-bit words
            ds.PixelData = arr.astype('uint16').tobytes()
            ds[0x7fe0, 0x0010].VR = 'OW'
            ds.BitsAllocated = 16
            ds.BitsStored = 16
            ds.HighBit = 15
        else:
            # Other high precision data type, like float:
            # rescale to uint16
            rescaled = (arr - self.b) / self.a
            ds.PixelData = rescaled.astype('uint16').tobytes()
            ds[0x7fe0, 0x0010].VR = 'OW'
            ds.BitsAllocated = 16
            ds.BitsStored = 16
            ds.HighBit = 15

    def _calculate_rescale(self, arr):
        """Calculate rescale parameters for series.

        y = ax + b
        x in 0:65535 correspond to y in ymin:ymax
        2^16 = 65536 possible steps in 16 bits dicom
        Returns:
            self.a: Rescale slope
            self.b: Rescale intercept
            self.center: Window center
            self.width: Window width
            self.smallestPixelValueInSeries: arr.min()
            self.largestPixelValueInSeries: arr.max()
            self.range_VR: The VR to use for DICOM elements (SS or US)
        """
        self.range_VR = 'SS' if np.issubdtype(arr.dtype, np.signedinteger) else 'US'
        self.range_VR = 'US' if arr.color else self.range_VR
        # Window center/width
        ymin = np.nanmin(arr).item()
        ymax = np.nanmax(arr).item()
        self.center = (ymax - ymin) / 2
        self.width = max(1, ymax - ymin)
        # y = ax + b,
        if arr.dtype in self.smallint or np.issubdtype(arr.dtype, np.bool_):
            # No need to rescale
            self.a = None
            self.b = None
            # self.smallestPixelValueInSeries = arr.min().astype('int16')
            # self.largestPixelValueInSeries = arr.max().astype('int16')
        else:
            # Other high precision data type, like float
            # Must rescale data
            self.b = ymin
            if math.fabs(ymax - ymin) > 1e-6:
                self.a = (ymax - ymin) / 65535.
            else:
                self.a = 1.0
            logger.debug("Rescale slope %f, rescale intercept %s" % (self.a, self.b))
        self.smallestPixelValueInSeries = ymin
        self.largestPixelValueInSeries = ymax

    def _set_pixel_rescale(self, ds, arr):
        """Set pixel rescale elements:
        - RescaleSlope
        - RescaleIntercept
        - WindowCenter
        - WindowWidth
        - SmallestPixelValueInSeries
        - LargestPixelValueInSeries
        Args:
            self.a: Rescale slope
            self.b: Rescale intercept
            self.center: Window center
            self.width: Window width
            self.smallestPixelValueInSeries: arr.min()
            self.largestPixelValueInSeries: arr.max()
            self.range_VR: The VR to use for DICOM elements (SS or US)
            ds: DICOM dataset
            arr: pixel series
        """
        ds.WindowCenter = pydicom.valuerep.format_number_as_ds(float(self.center))
        ds.WindowWidth = pydicom.valuerep.format_number_as_ds(float(self.width))
        # Remove existing elements
        for element in ['SmallestImagePixelValue', 'LargestImagePixelValue',
                        'SmallestPixelValueInSeries', 'LargestPixelValueInSeries',
                        'RescaleSlope', 'RescaleIntercept']:
            if element in ds:
                del ds[element]
        if self.a is None:
            # No rescale slope
            _min = 0 if arr.color else arr.min()
            _max = 255 if arr.color else arr.max()
            _series_min = 0 if arr.color else self.smallestPixelValueInSeries
            _series_max = 255 if arr.color else self.largestPixelValueInSeries
        else:
            try:
                ds.RescaleSlope = pydicom.valuerep.format_number_as_ds(self.a)
            except OverflowError:
                ds.RescaleSlope = "%d" % int(self.a)
            ds.RescaleIntercept = pydicom.valuerep.format_number_as_ds(self.b)
            _min = np.array((arr.min() - self.b) / self.a).astype('uint16')
            _max = np.array((arr.max() - self.b) / self.a).astype('uint16')
            _series_min = np.array(
                (self.smallestPixelValueInSeries - self.b) / self.a).astype('uint16')
            _series_max = np.array(
                (self.largestPixelValueInSeries - self.b) / self.a).astype('uint16')
        ds.add_new(tag_for_keyword('SmallestImagePixelValue'), self.range_VR, _min)
        ds.add_new(tag_for_keyword('LargestImagePixelValue'), self.range_VR, _max)
        ds.add_new(tag_for_keyword('SmallestPixelValueInSeries'), self.range_VR, _series_min)
        ds.add_new(tag_for_keyword('LargestPixelValueInSeries'), self.range_VR, _series_max)

    @staticmethod
    def _add_time(now, add):
        """Add time to present time now

        Args:
            now: string hhmmss.ms
            add: float [s]
        Returns:
            newtime: string hhmmss.ms
        """
        tnow = datetime.strptime(now, "%H%M%S.%f")
        s = int(add)
        ms = (add - s) * 1000.
        tadd = timedelta(seconds=s, milliseconds=ms)
        tnew = tnow + tadd
        return tnew.strftime("%H%M%S.%f")

    def _get_tag(self, im, input_order, opts):

        if input_order is None:
            return 0
        if input_order == INPUT_ORDER_NONE:
            return 0
        elif input_order == INPUT_ORDER_TIME:
            time_tag = self._choose_tag('time', 'AcquisitionTime')
            # if 'TriggerTime' in opts:
            #    return(float(image.TriggerTime))
            # elif 'InstanceNumber' in opts:
            #    return(float(image.InstanceNumber))
            # else:
            if im.data_element(time_tag).VR == 'TM':
                time_str = im.data_element(time_tag).value
                try:
                    if '.' in time_str:
                        tm = datetime.strptime(time_str, "%H%M%S.%f")
                    else:
                        tm = datetime.strptime(time_str, "%H%M%S")
                except ValueError:
                    raise CannotSort("Unable to extract time value from header.")
                td = timedelta(hours=tm.hour,
                               minutes=tm.minute,
                               seconds=tm.second,
                               microseconds=tm.microsecond)
                return td.total_seconds()
            else:
                try:
                    return float(im.data_element(time_tag).value)
                except ValueError:
                    raise CannotSort("Unable to extract time value from header.")
        elif input_order == INPUT_ORDER_B:
            b_tag = self._choose_tag('b', 'DiffusionBValue')
            try:
                return float(im.data_element(b_tag).value)
            except (KeyError, TypeError):
                pass
            b_tag = self._choose_tag('b', 'csa_header')
            if b_tag == 'csa_header':
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=UserWarning)
                    import nibabel.nicom.csareader as csa
                csa_head = csa.get_csa_header(im)
                try:
                    value = csa.get_b_value(csa_head)
                except TypeError:
                    raise CannotSort("Unable to extract b value from header.")
            else:
                try:
                    value = float(im.data_element(b_tag).value)
                except ValueError:
                    raise CannotSort("Unable to extract b value from header.")
            return value
        elif input_order == INPUT_ORDER_FA:
            fa_tag = self._choose_tag('fa', 'FlipAngle')
            try:
                return float(im.data_element(fa_tag).value)
            except ValueError:
                raise CannotSort("Unable to extract FA value from header.")
        elif input_order == INPUT_ORDER_TE:
            te_tag = self._choose_tag('te', 'EchoTime')
            try:
                return float(im.data_element(te_tag).value)
            except ValueError:
                raise CannotSort("Unable to extract TE value from header.")
        elif input_order == INPUT_ORDER_AUTO:
            pass
        else:
            # User-defined tag
            if input_order in opts:
                _tag = opts[input_order]
                try:
                    return float(im.data_element(_tag).value)
                except ValueError:
                    raise CannotSort("Unable to extract {} value from header.".format(input_order))
        raise (UnknownTag("Unknown input_order {}.".format(input_order)))

    def _choose_tag(self, tag, default):
        # Example: _tag = choose_tag('b', 'csa_header')
        if tag in self.input_options:
            return self.input_options[tag]
        else:
            return default

    def _set_dicom_tag(self, im, input_order, value):
        if input_order is None:
            pass
        elif input_order == INPUT_ORDER_NONE:
            pass
        elif input_order == INPUT_ORDER_TIME:
            # AcquisitionTime
            time_tag = self._choose_tag("time", "AcquisitionTime")
            if time_tag not in im:
                VR = pydicom.datadict.dictionary_VR(time_tag)
                if VR == 'TM':
                    im.add_new(time_tag, VR,
                               datetime.utcfromtimestamp(float(0.0)).strftime("%H%M%S.%f")
                               )
                else:
                    im.add_new(time_tag, VR, 0.0)
                # elem = pydicom.dataelem.DataElement(time_tag, 'TM', 0)
                # im.add(elem)
            if im.data_element(time_tag).VR == 'TM':
                time_str = datetime.utcfromtimestamp(float(value)).strftime("%H%M%S.%f")
                im.data_element(time_tag).value = time_str
            else:
                im.data_element(time_tag).value = float(value)
        elif input_order == INPUT_ORDER_B:
            # b_tag = opts['b'] if 'b' in opts else b_tag = 'csa_header'
            b_tag = self._choose_tag('b', "csa_header")
            if b_tag == "csa_header":
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=UserWarning)
                    import nibabel.nicom.csareader as csa
                csa_head = csa.get_csa_header(im)
                try:
                    if csa.get_b_value(csa_head) != float(value):
                        raise ValueError(
                            'Replacing b value in CSA header has not been implemented.')
                except Exception:
                    raise ValueError('Replacing b value in CSA header has not been implemented.')
            else:
                im.data_element(b_tag).value = float(value)
        elif input_order == INPUT_ORDER_FA:
            fa_tag = self._choose_tag('fa', 'FlipAngle')
            im.data_element(fa_tag).value = float(value)
        elif input_order == INPUT_ORDER_TE:
            te_tag = self._choose_tag('te', 'EchoTime')
            im.data_element(te_tag).value = float(value)
        else:
            # User-defined tag
            if input_order in self.input_options:
                _tag = self.input_options[input_order]
                im.data_element(_tag).value = float(value)
            else:
                raise (UnknownTag("Unknown input_order {}.".format(input_order)))

    def simulateAffine(self):
        # shape = (
        #     self.getDicomAttribute(tag_for_keyword('Rows')),
        #     self.getDicomAttribute(tag_for_keyword('Columns')))
        iop = self.getDicomAttribute(tag_for_keyword('ImageOrientationPatient'))
        if iop is None:
            return
        iop = np.array(list(map(float, iop)))
        iop = np.array(iop).reshape(2, 3).T
        logger.debug('simulateAffine: iop\n{}'.format(iop))
        s_norm = np.cross(iop[:, 1], iop[:, 0])
        # Rotation matrix
        R = np.eye(3)
        R[:, :2] = np.fliplr(iop)
        R[:, 2] = s_norm
        if not np.allclose(np.eye(3), np.dot(R, R.T), atol=5e-5):
            raise ValueErrorWrapperPrecisionError('Rotation matrix not nearly orthogonal')

        pix_space = self.getDicomAttribute(tag_for_keyword('PixelSpacing'))
        zs = self.getDicomAttribute(tag_for_keyword('SpacingBetweenSlices'))
        if zs is None:
            zs = self.getDicomAttribute(tag_for_keyword('SliceThickness'))
            if zs is None:
                zs = 1
        zs = float(zs)
        pix_space = list(map(float, pix_space))
        vox = tuple(pix_space + [zs])
        logger.debug('simulateAffine: vox {}'.format(vox))

        ipp = self.getDicomAttribute(tag_for_keyword('ImagePositionPatient'))
        if ipp is None:
            return
        ipp = np.array(list(map(float, ipp)))
        logger.debug('simulateAffine: ipp {}'.format(ipp))

        orient = R
        logger.debug('simulateAffine: orient\n{}'.format(orient))

        aff = np.eye(4)
        aff[:3, :3] = orient * np.array(vox)
        aff[:3, 3] = ipp
        logger.debug('simulateAffine: aff\n{}'.format(aff))

    def create_affine(self, hdr):
        """Function to generate the affine matrix for a dicom series
        This method was based on
        (http://nipy.org/nibabel/dicom/dicom_orientation.html)
        :param hdr: list with sorted dicom files
        """

        slices = hdr.slices

        # Create affine matrix
        # (http://nipy.sourceforge.net/nibabel/dicom/dicom_orientation.html#dicom-slice-affine)
        iop = self.getDicomAttribute(tag_for_keyword('ImageOrientationPatient'))
        if iop is None:
            return
        image_orient1 = np.array(iop[0:3])
        image_orient2 = np.array(iop[3:6])

        pix_space = self.getDicomAttribute(tag_for_keyword('PixelSpacing'))
        delta_r = float(pix_space[0])
        delta_c = float(pix_space[1])

        ipp = self.getDicomAttribute(tag_for_keyword('ImagePositionPatient'))
        if ipp is None:
            return
        image_pos = np.array(ipp)

        ippn = self.getDicomAttribute(tag_for_keyword('ImagePositionPatient'),
                                      slice=slices - 1)
        if ippn is None:
            return
        last_image_pos = np.array(ippn)

        if slices == 1:
            # Single slice
            step = [0, 0, -1]
        else:
            step = (image_pos - last_image_pos) / (1 - slices)

        # check if this is actually a volume and not all slices on the same location
        if np.linalg.norm(step) == 0.0:
            raise ValueError("NOT_A_VOLUME")

        affine = np.matrix([
            [-image_orient1[0] * delta_c, -image_orient2[0] * delta_r, -step[0], -image_pos[0]],
            [-image_orient1[1] * delta_c, -image_orient2[1] * delta_r, -step[1], -image_pos[1]],
            [image_orient1[2] * delta_c, image_orient2[2] * delta_r, step[2], image_pos[2]],
            [0, 0, 0, 1]
        ])
        logger.debug('create_affine: affine\n{}'.format(affine))
        return affine

    @staticmethod
    def _calculate_slice_location(image) -> np.ndarray:
        """Function to calculate slicelocation from imageposition and orientation.

        Args:
            image: image (pydicom dicom object)
        Returns:
            calculated slice location for this slice (float)
        Raises:
            ValueError: when sliceLocation cannot be calculated
        """

        def get_attribute(im, tag):
            if tag in im:
                return im[tag].value
            else:
                raise ValueError('Tag %s not found' % tag)

        def get_normal(im):
            iop = np.array(get_attribute(im, tag_for_keyword('ImageOrientationPatient')))
            normal = np.zeros(3)
            normal[0] = iop[1] * iop[5] - iop[2] * iop[4]
            normal[1] = iop[2] * iop[3] - iop[0] * iop[5]
            normal[2] = iop[0] * iop[4] - iop[1] * iop[3]
            return normal

        try:
            ipp = np.array(get_attribute(image, tag_for_keyword('ImagePositionPatient')),
                           dtype=float)
            _normal = get_normal(image)
            return np.inner(_normal, ipp)
        except ValueError as e:
            raise ValueError('Cannot calculate slice location: %s' % e)
