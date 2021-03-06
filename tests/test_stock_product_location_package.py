# This file is part of the stock_product_location_package module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockProductLocationPackageTestCase(ModuleTestCase):
    'Test Stock Product Location Package module'
    module = 'stock_product_location_package'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockProductLocationPackageTestCase))
    return suite
