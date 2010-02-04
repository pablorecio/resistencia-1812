# Copyright (c) 2007-2008 by Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# This file is part of PyCha.
#
# PyCha is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCha is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with PyCha.  If not, see <http://www.gnu.org/licenses/>.

import sys

import cairo

import pycha.pie

def pieChart(output, lines):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)

    dataSet = [(line[0], [[0, line[1]]]) for line in lines]

    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=d[0]) for i, d in enumerate(lines)],
            }
        },
        'background': {
            'hide': True,
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': '#ff6600'
            },
        },
        'padding': {
            'left': 70,
            'right': 10,
            'top': 0,
            'bottom': 0,
        },
        'legend': {
            'hide': True,
        }#,
        #'colorScheme': '#ff6600'
    }
    chart = pycha.pie.PieChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'piechart.png'
    pieChart(output)
