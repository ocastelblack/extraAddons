{
    'name': 'Custom Product Items',
    'version': '1.0',
    'summary': 'Agrega un campo "items" a la plantilla producto',
    'description': """
        Este modulo agrega un campo personalizado "items" a la vista de l plantilla producto.
    """,
    'author': 'Oscar Castelblanco,Sakya Tech',
    'category': 'Inventory',
    'depends': ['base', 'product','stock','point_of_sale'],
    'data': [
        'views/product_Items_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
      "point_of_sale.assets":[
          "custom_inventory/static/src/xml/extended_product_info_popup.xml"
      ],  
    },
}