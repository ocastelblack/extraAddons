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
    ],
     'web.assets_qweb': [
        'custom_inventory/static/src/xml/agregar_stock_modal.xml' 
     ],
    'installable': True,
    'application': True,
}