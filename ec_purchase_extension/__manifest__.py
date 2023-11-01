# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Purchase Customization Extension',
    'summary': 'Purchase Items View',
    'description': """
    """,
    'category': 'Inventory/Purchase',
    'author': 'Entrivis Tech Pvt. Ltd.',
    'website':'http://www.entrivistech.com',
    'depends' : ['base','purchase','purchase_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_family.xml',
        'views/product_view.xml',
        'views/purchase_view.xml',
        'views/purchase_order_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
