

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductExpiry(models.Model):
    _name = "product.expiry"

    product_id = fields.Many2one(comodel_name='product.product', string='Product ID')
    expiry_date = fields.Date(string='Expiry Date')
    quantity = fields.Float(string='Quantity')
    stock_picking = fields.Many2one(comodel_name='stock.picking')

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError("Quantity must be positive")

    @api.constrains('expiry_date')
    def _check_expiry_date(self):
        for record in self:
            if not record.expiry_date:
                raise ValidationError("No Expiry Date Entered")
            elif record.expiry_date <= fields.Date.today():
                raise ValidationError("Expiry date can't be in the past")


    def reduce_product_quantity(self,product_list, value_list):

        if len(product_list) == 0:

            return

        domain = []
        n = len(product_list) - 1

        for i in range(n):
            domain += ['|']

        for product in product_list:
            domain += [('product_id','=',product)]


        products = self.env['product.expiry'].search(domain)


        n=0
        for product in products:

            product.quantity = product.quantity - value_list[n]

            n+=1






