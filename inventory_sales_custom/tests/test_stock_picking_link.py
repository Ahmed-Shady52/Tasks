# from datetime import timedelta
# from odoo import fields
# from odoo.tests import TransactionCase
# from odoo.addons.inventory_sales_custom.models.stock_picking import StockPicking
#
#
# class TestStockPickingLink(TransactionCase):
#
#     def SetUp(self, *args, **kwargs):
#
#         super(TestStockPickingLink, self).setUp()
#
#         product = self.env['product.product'].create({
#             'name': 'Product [TEST - Change Company]',
#             'type': 'consu',
#         })
#         # print("created product id: ",product.id)
#         self.expiry_product = self.env['product.expiry'].create({
#             'product_id':product.id,
#             'quantity':5,
#             'expiry_date':fields.Date.today()+timedelta(days=10),
#         })
#         # print("product id in expiry: ",self.expiry_product['product_id'].id)
#         # print("expiry product id: ",self.expiry_product)
#         #
#         prod = self.env['stock.move'].create({
#             'name': 'test',
#             'location_id': self.env.ref('stock.stock_location_customers').id,
#             'location_dest_id': self.env.ref('stock.stock_location_stock').id,
#             'product_id': product.id,
#             'product_uom_qty': 20,
#         })
#         # print("product in stock move on2many: ",prod['product_id'].id)
#         # self.extra_prod = self.env['stock.move'].create({
#         #     'name': 'test',
#         #     'location_id': self.env.ref('stock.stock_location_customers').id,
#         #     'location_dest_id': self.env.ref('stock.stock_location_stock').id,
#         #     'product_id': product.id,
#         #     'product_uom_qty': 1,
#         # })
#         # print("extra product in stock move on2many: ", self.extra_prod['product_id'].id)
#         # self.picking = self.env['stock.picking'].create({
#         #     'location_id': self.env.ref('stock.stock_location_customers').id,
#         #     'location_dest_id': self.env.ref('stock.stock_location_stock').id,
#         #     'picking_type_id': self.ref('stock.picking_type_in'),
#         #     'move_ids_without_package':prod,
#         # })
#         # print(self.picking)
#         # print("product inside the on2many in stock picking: ",self.picking['move_ids_without_package'].product_id.id)
#         # print("product quantity inside the on2many in stock picking: ",self.picking['move_ids_without_package'].product_uom_qty)
#
#         self.stock_record_01 = self.env['stock.picking'].create({
#             'partner_id':5,
#             # 'location_id':1,
#             # 'location_dest_id':1,
#             'picking_type_id':self.ref('stock.picking_type_in'),
#             'move_ids_without_package':prod,
#         })
#         print(product)
#         print("expiry product: ",self.expiry_product)
#         print(self.stock_record_01['move_ids_without_package'].product_id)
#
#
#
#     def test_stock_picking_link(self):
#
#         self.SetUp()
#
#         property_id = self.stock_record_01
#
#         self.stock_record_01.button_validate()
#         expiry_product = self.expiry_product
#         # extra_prod = self.extra_prod
#         print("prop id product:",property_id['expiring_products'])
#         print(expiry_product)
#
#         self.assertRecordValues(property_id,{
#             'partner_id': 5,
#             # 'location_id': 1,
#             # 'location_dest_id': 1,
#             # 'picking_type_id': self.ref('stock.picking_type_in'),
#             'expiring_products': expiry_product,
#         })
#
#
#
