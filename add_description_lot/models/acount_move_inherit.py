from datetime import datetime, timedelta
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def get_stock_info(self,invoice_origin,product_id):
        
        if not product_id:
            return 'N'
        
        product_id_numeric = int(product_id.split('(')[1].split(')')[0])
        results = []
        
        stock_move_lines = self.env['stock.move.line'].search([
            ('picking_id.origin', '=', invoice_origin),
            ('product_id', '=', product_id_numeric)  # Filtrar por ID del producto
        ])
        
        for line in stock_move_lines:
            if line.lot_id:
                expiration_date = line.lot_id.expiration_date
                
                if expiration_date:
                    # Restar 5 horas de la fecha de caducidad
                    new_expiration_date = expiration_date - timedelta(hours=5)
                    
                    result = {
                        'product_name': line.product_id.name,
                        'lot_name': line.lot_id.name,
                        'expiration_date': new_expiration_date
                    }
                    results.append(result)
        
        return results