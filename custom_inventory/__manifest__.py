{
    'name': 'Custom Product Items',
    'version': '1.0',
    'summary': 'Agrega un campo "items" a la plantilla producto',
    'description': """
        Este modulo agrega un campo personalizado "items" a la vista de l plantilla producto.
    """,
    'author': 'Oscar Castelblanco',
    'category': 'Inventory',
    'depends': ['base', 'product','stock','point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_Items_views.xml',
        'views/product_info_popup_extension.xml'
    ],
    'qweb': ['static/src/xml/extended_product_info_popup.xml'],
    'installable': True,
    'application': True,
}