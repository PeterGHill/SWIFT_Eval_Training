#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:49:16 2017

@author: eebjw
"""

import iris

def cube_extract(cube,lat_min,lat_max,lon_min,lon_max):
    cube = cube.extract(iris.Constraint(latitude=lambda cell: lat_min <= cell.point <= lat_max))
    cube = cube.extract(iris.Constraint(longitude=lambda cell: lon_min <= cell.point <= lon_max))
    return cube