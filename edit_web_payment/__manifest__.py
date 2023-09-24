{
    'name': 'Personalizar Progress Wizard',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Personalización del Progress Wizard',
    'description': 'Agrega un div y un span después del progress-wizard.',
    'depends': ['base','website','website_sale'],
    'data': [
        'views/wizard_template.xml',  # Archivo XML con la vista personalizada
    ],
    'installable': True,
     'application': True,
}