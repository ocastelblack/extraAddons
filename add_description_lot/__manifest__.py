{
    'name': 'Add batches to invoice',
    'version': '1.0',
    'summary': 'module that adds batch and batch expiration data in the description of the invoice',
    'description': """
        module that adds batch and batch expiration data in the description of the invoice
    """,
    'author': 'Oscar Castelblanco,Sakya Tech',
    'category': 'Inventory',
    'depends': ['base', 'product','stock_account','account','sale'],
    'data': [
        'report/report_description_lot.xml',
        'report/report_sale_order_add_batch.xml',
        'views/sale_lot_portal_content.xml',
    ],
    'installable': True,
    'application': True,
}