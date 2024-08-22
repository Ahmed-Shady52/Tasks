from datetime import timedelta
from odoo.tests.common import TransactionCase
from odoo import fields

class TestEmployeeCertification(TransactionCase):

    def SetUp(self, *args, **kwargs):

        super(TestEmployeeCertification, self).setUp()

        # creating new records to test data with
        self.certification_01_record = self.env['employee.certification'].create({
            'name': 'Masters Degree',
            'certification_date': fields.Date.today(),
            'expiry_date': fields.Date.today()+timedelta(days=365),
            'status': 'valid',
            'notes': 'Unit Test Case',
        })

        self.certification_02_record = self.env['employee.certification'].create({
            'name': 'Masters Degree',
            'certification_date': fields.Date.today(),
            'expiry_date': fields.Date.today() + timedelta(days=365),
            'status': 'expired',
        })

    def test_01_certifications_values(self):
        self.SetUp()
        property_id = self.certification_01_record

        #testing the creation of records
        self.assertRecordValues(property_id,[{
            'name': 'Masters Degree',
            'certification_date': fields.Date.today(),
            'expiry_date': fields.Date.today() + timedelta(days=365),
            'status': 'valid',
            'notes': 'Unit Test Case',
        }])

    def test_02_certifications_values(self):
        self.SetUp()
        property_id = self.certification_02_record

        #testing the notes field default value
        self.assertRecordValues(property_id,[{
            'name': 'Masters Degree',
            'certification_date': fields.Date.today(),
            'expiry_date': fields.Date.today() + timedelta(days=365),
            'status': 'expired',
            'notes': 'None',
        }])






