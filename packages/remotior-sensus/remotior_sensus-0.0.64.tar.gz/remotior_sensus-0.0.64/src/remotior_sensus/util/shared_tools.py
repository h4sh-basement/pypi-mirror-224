# Remotior Sensus , software to process remote sensing and GIS data.
# Copyright (C) 2022-2023 Luca Congedo.
# Author: Luca Congedo
# Email: ing.congedoluca@gmail.com
#
# This file is part of Remotior Sensus.
# Remotior Sensus is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
# Remotior Sensus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Remotior Sensus. If not, see <https://www.gnu.org/licenses/>.

"""
Shared tools
"""

import os
import re
from typing import Union, Optional

import numpy as np

try:
    from scipy.ndimage import label
except Exception as error:
    str(error)

from remotior_sensus.core import configurations as cfg
from remotior_sensus.core.bandset_catalog import BandSet, BandSetCatalog
from remotior_sensus.util import files_directories, raster_vector
from remotior_sensus.core.processor_functions import region_growing


# check input path converting to the same crs if necessary
def prepare_input_list(
        band_list, reference_raster_crs=None,
        n_processes: int = None, src_nodata=None, dst_nodata=None
):
    cfg.logger.log.debug('start')
    cfg.logger.log.debug('band_list: %s' % str(band_list))
    information_list = []
    nodata_list = []
    if reference_raster_crs is None:
        reference_raster_crs = raster_vector.get_crs(band_list[0])
    # get crs from file
    elif files_directories.is_file(reference_raster_crs):
        reference_raster_crs = raster_vector.get_crs(reference_raster_crs)
    input_list = []
    name_list = []
    warped = False
    for i in range(len(band_list)):
        name_list.append(files_directories.file_name(band_list[i]))
        crs = raster_vector.get_crs(band_list[i])
        # check crs
        same_crs = raster_vector.compare_crs(crs, reference_raster_crs)
        if not same_crs:
            t_pmd = cfg.temp.temporary_raster_path(
                name=files_directories.file_name(band_list[i]),
                extension=cfg.vrt_suffix
            )
            reference_raster = cfg.multiprocess.create_warped_vrt(
                raster_path=band_list[i], output_path=t_pmd,
                output_wkt=str(reference_raster_crs), n_processes=n_processes,
                src_nodata=src_nodata, dst_nodata=dst_nodata
                )
            warped = True
        else:
            reference_raster = band_list[i]
        input_list.append(reference_raster)
        info = raster_vector.raster_info(band_list[i])
        if info is not False:
            (gt, crs, un, xy_count, nd, number_of_bands, block_size,
             scale_offset, data_type) = info
        else:
            cfg.logger.log.error('unable to get raster info: %s', band_list[i])
            return [], [], [], [], warped
        information_list.append(
            [gt, crs, un, xy_count, nd, number_of_bands, block_size,
             scale_offset, data_type]
        )
        nodata_list.append(nd)
    cfg.logger.log.debug('end; input_list: %s' % str(input_list))
    prepared = {'input_list': input_list, 'information_list': information_list,
                'nodata_list': nodata_list, 'name_list': name_list,
                'warped': warped}
    return prepared


# prepare process files
def prepare_process_files(
        input_bands: Union[list, int, BandSet], output_path: str,
        n_processes: Optional[int] = None, overwrite=False,
        bandset_catalog: Optional[BandSetCatalog] = None,
        temporary_virtual_raster=True, prefix=None, multiple_output=False,
        multiple_input=False,
        virtual_output=None, box_coordinate_list: Optional[list] = None
):
    cfg.logger.log.debug('input_bands: %s' % str(input_bands))
    if n_processes is None:
        n_processes = cfg.n_processes
    # TODO check overwrite file
    if overwrite:
        pass
    # get input list
    band_list = BandSetCatalog.get_band_list(input_bands, bandset_catalog)
    if type(input_bands) is BandSet:
        coord_list = input_bands.box_coordinate_list
        if coord_list is not None:
            box_coordinate_list = coord_list
    elif type(input_bands) is int:
        coord_list = bandset_catalog.get_bandset(
            bandset_number=input_bands).box_coordinate_list
        if coord_list is not None:
            box_coordinate_list = coord_list
    # list of inputs
    prepared_input = prepare_input_list(band_list, n_processes=n_processes)
    input_raster_list = prepared_input['input_list']
    raster_info = prepared_input['information_list']
    nodata_list = prepared_input['nodata_list']
    name_list = prepared_input['name_list']
    warped = prepared_input['warped']
    # single output path
    out_path = None
    # multiple output path list
    output_list = []
    # multiple output virtual raster check list
    vrt_list = []
    if multiple_output:
        if output_path is None:
            output_path = []
            for _r in input_raster_list:
                output_path.append(cfg.temp.temporary_raster_path(
                    name=files_directories.file_name(_r),
                    extension=cfg.vrt_suffix
                ))
        if type(output_path) is not list and files_directories.is_directory(
                output_path
        ):
            for r in input_raster_list:
                p = os.path.join(
                    output_path, '{}{}'.format(
                        prefix, files_directories.file_name(r)
                    )
                ).replace('\\', '/')
                # check output path
                out_path, vrt_r = files_directories.raster_output_path(
                    p, virtual_output
                )
                output_list.append(out_path)
                vrt_list.append(vrt_r)
        else:
            for r in output_path:
                # check output path
                out_path, vrt_r = files_directories.raster_output_path(
                    r, virtual_output
                )
                output_list.append(out_path)
                vrt_list.append(vrt_r)
    else:
        if output_path is None:
            output_path = cfg.temp.temporary_raster_path(
                extension=cfg.vrt_suffix
            )
        # check output path
        out_path, virtual_output = files_directories.raster_output_path(
            output_path, virtual_output
        )
    # create virtual raster of input
    if temporary_virtual_raster or box_coordinate_list is not None:
        if multiple_input:
            temp_list = []
            for r in input_raster_list:
                temporary_virtual_raster = (
                    raster_vector.create_temporary_virtual_raster(
                        input_raster_list=[r],
                        box_coordinate_list=box_coordinate_list
                    )
                )
                temp_list.append(temporary_virtual_raster)
            input_raster_list = temp_list
            temporary_virtual_raster = True
        else:
            temporary_virtual_raster = (
                raster_vector.create_temporary_virtual_raster(
                    input_raster_list=input_raster_list,
                    box_coordinate_list=box_coordinate_list
                )
            )
    prepared = {
        'input_raster_list': input_raster_list, 'raster_info': raster_info,
        'nodata_list': nodata_list, 'name_list': name_list, 'warped': warped,
        'output_path': out_path, 'virtual_output': virtual_output,
        'temporary_virtual_raster': temporary_virtual_raster,
        'n_processes': n_processes, 'output_list': output_list,
        'vrt_list': vrt_list
    }
    return prepared


# create base structure
def create_base_structure(size: int):
    structure = np.ones((size, size))
    return structure


# create a circular structure
def create_circular_structure(radius):
    circle = np.zeros([radius * 2 + 1, radius * 2 + 1])
    for x in range(radius * 2 + 1):
        for y in range(radius * 2 + 1):
            if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2:
                circle[x, y] = 1
    return circle


# open structure file
def open_structure(structure):
    text = open(structure, 'r')
    lines = text.readlines()
    c = None
    for b in lines:
        b = b.replace('nan', 'np.nan').replace(cfg.new_line, '')
        a = eval(b)
        i = np.array(a, dtype=np.float32)
        try:
            c = np.append(c, [i], axis=0)
        except Exception as err:
            str(err)
            try:
                c = np.append([c], [i], axis=0)
            except Exception as err:
                str(err)
                c = i
    return c


# convert data type from string to numpy
def data_type_conversion(data_type):
    data_types = {
        cfg.float64_dt: np.float64, cfg.float32_dt: np.float32,
        cfg.int32_dt: np.int32, cfg.uint32_dt: np.uint32,
        cfg.int16_dt: np.int16, cfg.uint16_dt: np.uint16,
        cfg.byte_dt: np.byte,
    }
    if data_type in data_types:
        return data_types[data_type]
    else:
        return None


# expand list of lists
def expand_list(input_list):
    expanded_list = []
    for c in input_list:
        expanded_list.extend(c)
    return expanded_list


# join path
def join_path(*argv):
    path = os.path.join(*argv)
    return path


# replace ignoring case
def replace(input_string: str, old_value: str, new_value: str):
    old_value = old_value.replace('*', '\\*').replace(
        '(', '\\('
    ).replace(')', '\\)')
    output = re.sub(old_value, new_value, input_string, flags=re.IGNORECASE)
    return output


# region growing polygon
def region_growing_polygon(
        coordinate_x, coordinate_y, input_bands: Union[list, int, BandSet],
        output_vector=None, band_number=None, max_width=None,
        max_spectral_distance=None, minimum_size=None, bandset_catalog=None,
        n_processes=None
):
    cfg.logger.log.debug('start')
    box_coordinate_list = tmp_vrt = None
    if type(input_bands) is BandSet:
        coord_list = input_bands.box_coordinate_list
        if coord_list is not None:
            box_coordinate_list = coord_list
    elif type(input_bands) is int:
        coord_list = bandset_catalog.get_bandset(
            bandset_number=input_bands).box_coordinate_list
        if coord_list is not None:
            box_coordinate_list = coord_list
    # get input list
    band_list = BandSetCatalog.get_band_list(input_bands, bandset_catalog)
    cfg.logger.log.debug('band_list: %s' % str(band_list))
    # get input files
    prepared = prepare_input_list(
        band_list=band_list, n_processes=n_processes
    )
    input_raster_list = prepared['input_list']
    temporary_virtual_raster = raster_vector.create_temporary_virtual_raster(
        input_raster_list=input_raster_list,
        box_coordinate_list=box_coordinate_list
    )
    # input_path raster extent and pixel size
    info = raster_vector.image_geotransformation(temporary_virtual_raster)
    left = info['left']
    right = info['right']
    top = info['top']
    bottom = info['bottom']
    p_x = info['pixel_size_x']
    p_y = info['pixel_size_y']
    if max_width is None:
        max_width = 3
    if max_spectral_distance is None:
        max_spectral_distance = 1
    if minimum_size is None:
        minimum_size = 1
    # seed pixel
    abs_seed_x = abs(int((abs(coordinate_x) - left) / p_x))
    seed_x_min = left + abs_seed_x * p_x
    seed_x_max = left + (abs_seed_x + 1) * p_x
    abs_seed_y = abs(int((top - abs(coordinate_y)) / p_y))
    seed_y_max = top - abs_seed_y * p_y
    seed_y_min = top - (abs_seed_y + 1) * p_y
    region_min_x = seed_x_min - int(max_width/2) * p_x
    if region_min_x < left:
        region_min_x = left
    region_max_x = seed_x_max + int(max_width/2) * p_x
    if region_max_x > right:
        region_max_x = right
    region_min_y = seed_y_min - int(max_width/2) * p_y
    if region_min_y < bottom:
        region_min_y = bottom
    region_max_y = seed_y_max + int(max_width/2) * p_y
    if region_max_y > top:
        region_max_y = top
    seed_x = abs(int((abs(coordinate_x) - region_min_x) / p_x))
    seed_y = abs(int((region_max_y - abs(coordinate_y)) / p_y))
    cfg.logger.log.debug('seed_x: %s; seed_y: %s' % (seed_x, seed_y))
    # extract each virtual band and apply extent from max_width and coordinates
    extent_list = [region_min_x, region_max_y, region_max_x, region_min_y]
    function_variable = []
    virtual_raster_list = []
    if band_number is None:
        band_number_list = list(range(1, len(band_list) + 1))
        # extract virtual band
        for i in band_number_list:
            tmp_vrt = raster_vector.create_temporary_virtual_raster(
                input_raster_list=[temporary_virtual_raster],
                box_coordinate_list=extent_list,
                band_number_list=[[i]]
            )
            virtual_raster_list.append(tmp_vrt)
            function_variable.append(
                [seed_x, seed_y, float(max_spectral_distance),
                 int(minimum_size)]
            )
    else:
        band_number_list = [[band_number]]
        # extract virtual band
        tmp_vrt = raster_vector.create_temporary_virtual_raster(
            input_raster_list=[temporary_virtual_raster],
            box_coordinate_list=extent_list, band_number_list=band_number_list
        )
        virtual_raster_list.append(tmp_vrt)
        function_variable.append(
            [seed_x, seed_y, float(max_spectral_distance), int(minimum_size)]
        )
    cfg.multiprocess.run_separated(
        raster_path_list=virtual_raster_list, function=region_growing,
        function_argument=band_number_list,
        function_variable=function_variable, any_nodata_mask=True,
        keep_output_argument=True, n_processes=n_processes,
        progress_message='region growing'
    )
    cfg.multiprocess.multiprocess_region_growing()
    regions = cfg.multiprocess.output
    if len(regions) > 0:
        region = None
        # run segmentation
        for region_array in regions:
            if region is None:
                region = region_array.astype(int)
            else:
                region = region * region_array.astype(int)
        if region[seed_y, seed_x] == 0:
            region[seed_y, seed_x] = 1
        if np.count_nonzero(region) > 0:
            try:
                region_label, num_features = label(region)
                region_seed_value = region_label[seed_y, seed_x]
                new_region = (region_label == region_seed_value).astype(int)
            except Exception as err:
                str(err)
                cfg.logger.log.error('region growing label')
                return False
        else:
            cfg.logger.log.error('region growing empty')
            return False
    else:
        new_region = regions[0]
    # create vector from region
    if np.count_nonzero(new_region) > 0 and new_region[seed_y, seed_x] == 1:
        if output_vector is None:
            output_vector = cfg.temp.temporary_file_path(
                name_suffix=cfg.gpkg_suffix
            )
        raster_vector.array_to_polygon(
            input_array=new_region, reference_raster=tmp_vrt,
            output=output_vector
        )
        cfg.logger.log.debug('end; roi vector: %s' % str(output_vector))
        return output_vector
    else:
        cfg.logger.log.error('region growing empty')
        return False
