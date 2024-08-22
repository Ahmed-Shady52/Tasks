from odoo import models

class CertificationsXLSX(models.AbstractModel):
    _name = 'report.employee_certifications.report_certifications_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):

        # creating a font format and sheet to write data on
        bold = workbook.add_format({'bold': True})
        sheet = workbook.add_worksheet('Certifications')

        #deciding start row and column
        col = 3
        row = 3
        num = 0

        #writting titles on the document
        sheet.write(row,col-1,'No#',bold)
        sheet.write(row,col,'Employee',bold)
        sheet.write(row,col+1,'Certification',bold)
        sheet.write(row,col+2,'Certificate Creation Date',bold)
        sheet.write(row,col+3,'Certificate Expiry Date',bold)
        sheet.write(row,col+4,'Certificate Validity',bold)
        sheet.write(row,col+5,'Notes',bold)

        #looping on each record and parsing the data in the right spot then incrementing the row for the next record to be parsed until all are done
        for certification in data['certifications']:
            row += 1
            num += 1
            sheet.write(row,col-1,'#'+str(num))
            sheet.write(row,col,certification['employee_id'][1])
            sheet.write(row,col+1,certification['name'])
            sheet.write(row,col+2,certification['certification_date'])
            sheet.write(row,col+3,certification['expiry_date'])
            sheet.write(row,col+4,certification['status'])
            sheet.write(row,col+5,certification['notes'])







