from odoo.addons.inventory_sales_custom.models.product_expiry import ProductExpiry
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_confirm(self):

        product_list = []
        value_list = []
        products = []
        products_records = self.env['product.expiry'].search_read()



        for product in products_records:
            products += [product['product_id'][0]]



        for record in self:
            for line in record.order_line:
                if line.product_id.id in products:
                    product_list += [line.product_id.id]
                    value_list += [line.product_uom_qty]


        ProductExpiry.reduce_product_quantity(self,product_list, value_list)
        super(SaleOrder,self).action_confirm()

