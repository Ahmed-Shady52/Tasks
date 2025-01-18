# -*- coding: utf-8 -*-
{
    'name': "employee_certifications",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','xlsx_reporting'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/employee_certification_views.xml',
        'views/hr_employee_views.xml',
        'views/menu.xml',
        'views/server_actions.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}

