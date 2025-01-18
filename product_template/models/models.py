# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):

    _inherit = "product.template"

    commercial_product_name = fields.Char(string='Commercial Name')
    size_measurement = fields.Char(string='Size/Measurement')
    store_entry_type = fields.Char(string='Entry Type', compute='_compute_entry_type')
    brand = fields.Char(string='Brand') #should be many2one from new model
    country = fields.Many2one(string='Country',comodel_name='res.country')
    main_classification = fields.Char(string='Main Classification',compute='_compute_main_classification')
    calc_method = fields.Char(string='Calculation Method ',compute='_compute_calc_method')


    def _compute_calc_method(self):
        self.calc_method = self.env['product.category'].search_read([('id','=',self.categ_id.id)])[0]['property_cost_method']

    def _compute_main_classification(self):
        self.main_classification = self.env['product.category'].search_read([('id','=',self.categ_id.id)])[0]['parent_id']

    def _compute_entry_type(self):
        # self.store_entry_type = self.env['product.category'].search_read([('id','=',self.categ_id.id)])[0]['valuation']
        self.store_entry_type = 'test'