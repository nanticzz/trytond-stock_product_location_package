# This file is part of stock_product_location_package module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .location import *


def register():
    Pool.register(
        ProductLocation,
        module='stock_product_location_package', type_='model')
