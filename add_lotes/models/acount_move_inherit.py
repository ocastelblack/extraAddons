from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def extract_product_id(self, product_id):
        # El parámetro product_id viene en el formato product.product(9,)
        # Aquí lo parseamos para obtener el valor numérico
        String = product_id
        return int(String.split('(')[1].split(')')[0])
    
    def get_stock_info(self,invoice_origin,product_id):
        # order_id = self.env["sale.order"].search([("id","=",7)],limit=1)
        # result = product_id
        product_id_numeric = int(product_id.split('(')[1].split(')')[0])
        results = []
        
        stock_move_lines = self.env['stock.move.line'].search([
            ('picking_id.origin', '=', invoice_origin),
            ('product_id', '=', product_id_numeric)  # Filtrar por ID del producto
        ])
        
        for line in stock_move_lines:
            if line.lot_id:
                result = {
                    'product_name': line.product_id.name,
                    'lot_name': line.lot_id.name,
                    'expiration_date': line.lot_id.expiration_date
                }
                results.append(result)
        
        return results
        # return result