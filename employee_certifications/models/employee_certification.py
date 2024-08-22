from datetime import timedelta


from odoo import api, fields, models






class EmployeeCertification(models.Model):
    _name = "employee.certification"

    # fields for user data
    name = fields.Char(string='Certification Name', help='The name of the certification')
    employee_id = fields.Many2one(string='Employee ID', comodel_name='hr.employee')
    certification_date = fields.Date(string='Certification Date', help='The date when the certification was obtained')
    expiry_date = fields.Date(string='Expiry Date', help='The date when the certification will expire')
    status = fields.Selection(selection=[('valid','Valid'),('expired','Expired')], string='Certification Status')
    notes = fields.Text(string='Notes',help='Additional notes or comments about this certification', default='None')



    #python action to be used in the server action to print the report
    def action_print_xlsx(self):

        #date in 30 days
        today_extra = fields.Date.today() + timedelta(days=30)

        #filtering the records where they wouldn't expire in the 30 days
        certifications = self.env['employee.certification'].search_read([('expiry_date', '>', today_extra)])

        #saving the records in a dictionary to be used in printing the report
        data = {
            'certifications': certifications
        }

        #calling the report method
        return self.env.ref('employee_certifications.action_report_certifications_xlsx').report_action(self,data=data)









