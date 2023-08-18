from odoo import models, fields

class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    Stock_Miami = fields.Integer(string='Stock Miami')