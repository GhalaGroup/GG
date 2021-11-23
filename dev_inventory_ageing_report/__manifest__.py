# -*- coding: utf-8 -*-

{
    'name': 'Inventory Aging Report',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Warehouse',
    'summary': 'odoo Apps will print Stock Aging Report by Company, Warehouse, Location, Product Category, and Product | stock expiry report | inventory expiry report | inventory aging report | Stock Aging Report | Inventory Age Report & Break Down Report | Stock Aging Excel Report',
    'description': """
        odoo Apps will print Stock Aging Report by Compnay, Warehoouse, Location, Product Category and Product.

    """,
    'author': 'Stephen Ngailo', 
    'depends': ['base','purchase','stock','account','sale_stock',],
    'data': [
        'security/ir.model.access.csv',
        'wizard/inventory_wizard_view.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
 
}

