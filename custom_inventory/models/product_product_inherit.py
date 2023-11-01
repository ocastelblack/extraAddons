from odoo import models, fields

class ProductProductInherit(models.Model):
    _inherit = "product.product"
    
    def get_product_info_pos(self, price, quantity, pos_config_id):
        res = super(ProductProductInherit, self).get_product_info_pos(
            price, quantity, pos_config_id
        )
        # res.update({"stock_miami": self.stock_miami})
        res.update({
            "stock_miami": self.stock_miami,
            "last_updated": self.last_updated.strftime("%d/%m/%Y"),  # Agregar last_updated al diccionario
        })
        return res