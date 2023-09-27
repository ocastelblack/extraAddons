{
    'name': 'customize client form web page',
    'version': '1.0',
    'category': 'Website',
    'summary': 'customize client form web page',
    'description': 'The integration of the company and individual radios is carried out, the identification type drop-down list.',
    'author': 'Oscar Castelblanco,Sakya',
    'website': 'https://www.sakya.co/',
    'depends': ['base','website','website_sale'],
    'data': [
        'views/wizard_template.xml',  # Archivo XML con la vista personalizada
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/custom_validation.js',  # Ruta a tu archivo JavaScript personalizado.
    ],
}