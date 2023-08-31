from odoo import models, fields, api

class CustomProductItem(models.Model):
    _inherit = 'product.product'

    stock_miami = fields.Integer(string='stock_miami')
    last_updated = fields.Datetime(string='Última Actualización stock_miami', compute="compute_custom_field", store=True)
    
    @api.depends('stock_miami')
    def compute_custom_field(self):
        for record in self:
            record.last_updated = fields.Datetime.now()