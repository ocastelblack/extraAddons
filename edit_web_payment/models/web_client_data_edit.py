from odoo import models, fields

class WebsiteSale(models.Model):
    _inherit = 'website.sale'

    def pruba_hola_hse(self):
        return 'Hola <odoo>'