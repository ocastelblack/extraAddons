from odoo import models, fields

class query_lots_sales_order(models.Model):
    _inherit = 'sale.order'

    def get_lots_sales_order(self,sale_order_name,product_id):
        product_id_numeric = int(product_id.split('(')[1].split(')')[0])

        results = []  # Properly indented

        stock_move_lines = self.env['stock.move.line'].search([
            ('picking_id.origin', '=', sale_order_name),
            ('picking_id.state', '=', 'done'),
            ('product_id', '=', product_id_numeric)
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
        
        # return 'Hola'
        
    def funcion_lots_sales_order(self,product_id):
    
        return product_id
    