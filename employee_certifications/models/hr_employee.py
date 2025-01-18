from odoo import api, models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    #adding the certification field connected to the 'employee.certification' module to the inherited employee module
    certification = fields.One2many(string='Certification', comodel_name='employee.certification', inverse_name='name')