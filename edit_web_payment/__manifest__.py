{
    'name': 'customize client form web page',
    'version': '1.0',
    'category': 'Website',
    'summary': 'customize client form web page',
    'description': 'The integration of the company and individual radios is carried out, the identification type drop-down list.',
    'author': 'Oscar Castelblanco,Sakya',
    'website': 'https://www.sakya.co/',
    'depends': ['base','web','website','website_sale'],
    'data': [
        'views/wizard_template.xml',  # Archivo XML con la vista personalizada
    ],
    'installable': True,
    'application': True,
    # 'assets': {
    #     'web.assets_frontend': [
    #         'edit_web_payment/static/src/js/edit_name_user.js',  # Ruta al archivo JavaScript personalizado
    #     ],
    # },
 }