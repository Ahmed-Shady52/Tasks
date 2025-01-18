# -*- coding: utf-8 -*-
{
    'name': "inventory_sales_custom",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/product_expiry_view.xml',
        'views/stock_picking_view.xml',
        'views/menu.xml',
        # 'views/server_actions.xml',
        'wizard/wizard_view.xml',
        'report/pdf_report.xml',
        'report/report_expiry_product_pdf.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}

