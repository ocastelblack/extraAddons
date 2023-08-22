from odoo import models, fields

class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    stock_miami = fields.Integer(string='stock_miami')