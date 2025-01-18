from itertools import product

from odoo import api, fields, models


class ExpiryProductPdfReport(models.TransientModel):
    _name = 'expiry_product.report.wizard'

    start_date = fields.Date(string='From')
    end_date = fields.Date(string='To')

    def action_report_pdf(self):

        domain = []

        start_date = self.start_date
        end_date = self.end_date
        if self.start_date:
            domain += [('expiry_date','>=',start_date)]
        if self.end_date:
            domain += [('expiry_date', '<=', end_date)]


        products = self.env['product.expiry'].search_read(domain)

        data= {
            'products': products,
            'form_data': self.read()[0],
        }

        # print(products[0]['product_id'])
        return self.env.ref('inventory_sales_custom.action_report_expiry_product_pdf').report_action(self, data=data)

