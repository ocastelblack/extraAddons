from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def funcion(self,product_id):
        order_id = self.env["sale.order"].search([("id","=",7)],limit=1)
        result = product_id
        return result