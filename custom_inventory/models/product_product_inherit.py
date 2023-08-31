from odoo import models, fields

class ProductProductInherit(models.Model):
    _inherit = "product.product"
    
    def get_product_info_pos(self, price, quantity, pos_config_id):
        res = super(ProductProductInherit, self).get_product_info_pos(
            price, quantity, pos_config_id
        )
        res.update({"stock_miami": self.product_tmpl_id.stock_miami})
        return res