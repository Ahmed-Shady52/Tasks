from datetime import timedelta
from odoo.addons.inventory_sales_custom.models.product_expiry import ProductExpiry

from odoo.tests.common import TransactionCase
from odoo import fields

class TestInventorySaleCustom(TransactionCase):

    def SetUp(self, *args, **kwargs):

        super(TestInventorySaleCustom, self).setUp()

        # creating new records to test data with
        self.Inventory_01_record = self.env['product.expiry'].create({
            'product_id': 16,
            'quantity': 5,
            'expiry_date': fields.Date.today()+timedelta(days=365),
        })

        self.Inventory_02_record = self.env['product.expiry'].create({
            'product_id': 32,
            'quantity': 25,
            'expiry_date': fields.Date.today() + timedelta(days=1),
        })


    def test_01_record_values(self):
        self.SetUp()
        property_id = self.Inventory_01_record

        #testing the creation of records
        self.assertRecordValues(property_id,[{
            'product_id': 16,
            'quantity': 5,
            'expiry_date': fields.Date.today()+timedelta(days=365),
        }])

    def test_02_record_values(self):
        self.SetUp()
        property_id = self.Inventory_02_record

        #testing the creation of records
        self.assertRecordValues(property_id,[{
            'product_id': 32,
            'quantity': 25,
            'expiry_date': fields.Date.today()+timedelta(days=1),
        }])

    def test_03_record_values(self):
        self.SetUp()
        property_id = self.Inventory_02_record
        ProductExpiry.reduce_product_quantity(self,[32],[3.0])

        #testing the creation of records
        self.assertRecordValues(property_id,[{
            'product_id': 32,
            'quantity': 22,
            'expiry_date': fields.Date.today()+timedelta(days=1),
        }])