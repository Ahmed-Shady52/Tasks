from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"


    expiring_products = fields.One2many(comodel_name='product.expiry', inverse_name='stock_picking', string='Expiring products')

    def button_validate(self):
        products = []

        products_records = self.env['product.expiry'].search_read()

        for product in products_records:
            products += [product['product_id'][0]]

        for record in self:
            for line in record.move_ids_without_package:
                if line.product_id.id in products:
                    if self.env['product.expiry'].search([('product_id.id','=',line.product_id.id)]).expiry_date <= fields.Date.today():
                        raise ValidationError("One or more products are expired")
                    else:
                        lines = []
                        id = self.env['product.expiry'].search([('product_id','=',line.product_id.id)])
                        lines.append((4,id.id))
                        record.expiring_products = lines


        super(StockPicking,self).button_validate()



