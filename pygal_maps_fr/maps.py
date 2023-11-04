# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
French departments and regions maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from pygal._compat import u
from numbers import Number
import os


DEPARTMENTS = {
    '01': u("Ain"),
    '02': u("Aisne"),
    '03': u("Allier"),
    '04': u("Alpes-de-Haute-Provence"),
    '05': u("Hautes-Alpes"),
    '06': u("Alpes-Maritimes"),
    '07': u("Ardèche"),
    '08': u("Ardennes"),
    '09': u("Ariège"),
    '10': u("Aube"),
    '11': u("Aude"),
    '12': u("Aveyron"),
    '13': u("Bouches-du-Rhône"),
    '14': u("Calvados"),
    '15': u("Cantal"),
    '16': u("Charente"),
    '17': u("Charente-Maritime"),
    '18': u("Cher"),
    '19': u("Corrèze"),
    '2A': u("Corse-du-Sud"),
    '2B': u("Haute-Corse"),
    '21': u("Côte-d'Or"),
    '22': u("Côtes-d'Armor"),
    '23': u("Creuse"),
    '24': u("Dordogne"),
    '25': u("Doubs"),
    '26': u("Drôme"),
    '27': u("Eure"),
    '28': u("Eure-et-Loir"),
    '29': u("Finistère"),
    '30': u("Gard"),
    '31': u("Haute-Garonne"),
    '32': u("Gers"),
    '33': u("Gironde"),
    '34': u("Hérault"),
    '35': u("Ille-et-Vilaine"),
    '36': u("Indre"),
    '37': u("Indre-et-Loire"),
    '38': u("Isère"),
    '39': u("Jura"),
    '40': u("Landes"),
    '41': u("Loir-et-Cher"),
    '42': u("Loire"),
    '43': u("Haute-Loire"),
    '44': u("Loire-Atlantique"),
    '45': u("Loiret"),
    '46': u("Lot"),
    '47': u("Lot-et-Garonne"),
    '48': u("Lozère"),
    '49': u("Maine-et-Loire"),
    '50': u("Manche"),
    '51': u("Marne"),
    '52': u("Haute-Marne"),
    '53': u("Mayenne"),
    '54': u("Meurthe-et-Moselle"),
    '55': u("Meuse"),
    '56': u("Morbihan"),
    '57': u("Moselle"),
    '58': u("Nièvre"),
    '59': u("Nord"),
    '60': u("Oise"),
    '61': u("Orne"),
    '62': u("Pas-de-Calais"),
    '63': u("Puy-de-Dôme"),
    '64': u("Pyrénées-Atlantiques"),
    '65': u("Hautes-Pyrénées"),
    '66': u("Pyrénées-Orientales"),
    '67': u("Bas-Rhin"),
    '68': u("Haut-Rhin"),
    '69': u("Rhône"),
    '70': u("Haute-Saône"),
    '71': u("Saône-et-Loire"),
    '72': u("Sarthe"),
    '73': u("Savoie"),
    '74': u("Haute-Savoie"),
    '75': u("Paris"),
    '76': u("Seine-Maritime"),
    '77': u("Seine-et-Marne"),
    '78': u("Yvelines"),
    '79': u("Deux-Sèvres"),
    '80': u("Somme"),
    '81': u("Tarn"),
    '82': u("Tarn-et-Garonne"),
    '83': u("Var"),
    '84': u("Vaucluse"),
    '85': u("Vendée"),
    '86': u("Vienne"),
    '87': u("Haute-Vienne"),
    '88': u("Vosges"),
    '89': u("Yonne"),
    '90': u("Territoire de Belfort"),
    '91': u("Essonne"),
    '92': u("Hauts-de-Seine"),
    '93': u("Seine-Saint-Denis"),
    '94': u("Val-de-Marne"),
    '95': u("Val-d'Oise"),
    '971': u("Guadeloupe"),
    '972': u("Martinique"),
    '973': u("Guyane"),
    '974': u("Réunion"),
    '976': u("Mayotte")
}


REGIONS = {
    '11': u("Île-de-France"),
    '24': u("Centre-Val de Loire"),
    '27': u("Bourgogne-Franche-Comté"),
    '28': u("Normandie"),
    '32': u("Hauts-de-France"),
    '44': u("Grand Est"),
    '52': u("Pays de la Loire"),
    '53': u("Bretagne"),
    '75': u("Nouvelle-Aquitaine"),
    '76': u("Occitanie"),
    '84': u("Auvergne-Rhône-Alpes"),
    '93': u("Provence-Alpes-Côte d'Azur"),
    '94': u("Corse"),
    '01': u("Guadeloupe"),
    '02': u("Martinique"),
    '03': u("Guyane"),
    '04': u("Réunion"),
    '06': u("Mayotte")
}


with open(os.path.join(
        os.path.dirname(__file__),
        'fr.departments.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class Departments(IntCodeMixin, BaseMap):
    """French department map"""
    x_labels = list(DEPARTMENTS.keys())
    area_names = DEPARTMENTS
    area_prefix = 'z'
    kind = 'departement'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'fr.regions.svg')) as file:
    REG_MAP = file.read()


class Regions(IntCodeMixin, BaseMap):
    """French regions map"""
    x_labels = list(REGIONS.keys())
    area_names = REGIONS
    area_prefix = 'a'
    svg_map = REG_MAP
    kind = 'region'


DEPARTMENTS_REGIONS = {
    "01": "84",
    "02": "32",
    "03": "84",
    "04": "93",
    "05": "93",
    "06": "93",
    "07": "84",
    "08": "44",
    "09": "76",
    "10": "44",
    "11": "76",
    "12": "76",
    "13": "93",
    "14": "28",
    "15": "84",
    "16": "75",
    "17": "75",
    "18": "24",
    "19": "75",
    "21": "27",
    "22": "53",
    "23": "75",
    "24": "75",
    "25": "27",
    "26": "84",
    "27": "28",
    "28": "24",
    "29": "53",
    "2A": "94",
    "2B": "94",
    "30": "76",
    "31": "76",
    "32": "76",
    "33": "75",
    "34": "76",
    "35": "53",
    "36": "24",
    "37": "24",
    "38": "84",
    "39": "27",
    "40": "75",
    "41": "24",
    "42": "84",
    "43": "84",
    "44": "52",
    "45": "24",
    "46": "76",
    "47": "75",
    "48": "76",
    "49": "52",
    "50": "28",
    "51": "44",
    "52": "44",
    "53": "52",
    "54": "44",
    "55": "44",
    "56": "53",
    "57": "44",
    "58": "27",
    "59": "32",
    "60": "32",
    "61": "28",
    "62": "32",
    "63": "84",
    "64": "75",
    "65": "76",
    "66": "76",
    "67": "44",
    "68": "44",
    "69": "84",
    "70": "27",
    "71": "27",
    "72": "52",
    "73": "84",
    "74": "84",
    "75": "11",
    "76": "28",
    "77": "11",
    "78": "11",
    "79": "75",
    "80": "32",
    "81": "76",
    "82": "76",
    "83": "93",
    "84": "93",
    "85": "52",
    "86": "75",
    "87": "75",
    "88": "44",
    "89": "27",
    "90": "27",
    "91": "11",
    "92": "11",
    "93": "11",
    "94": "11",
    "95": "11",
    "971": "01",
    "972": "02",
    "973": "03",
    "974": "04",
    "976": "06"
}


def aggregate_regions(values):
    if isinstance(values, dict):
        values = values.items()
    regions = defaultdict(int)
    for department, value in values:
        regions[DEPARTMENTS_REGIONS[department]] += value
    return list(regions.items())
