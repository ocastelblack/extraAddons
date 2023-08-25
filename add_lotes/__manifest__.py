{
    'name': 'Add batches to invoice',
    'version': '1.0',
    'summary': 'Add lotes/series, expiration date to the sales invoice',
    'description': """
        This module adds a batch/series field and its expiration date.
    """,
    'author': 'Oscar Castelblanco,Sakya Tech',
    'category': 'Inventory',
    'depends': ['base', 'product','stock_account','account'],
    'data': [
        'report/invoice_line_extension.xml',
    ],
    'installable': True,
    'application': True,
}