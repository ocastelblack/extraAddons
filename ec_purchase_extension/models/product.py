# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductProduct(models.Model):
    _inherit = "product.template"

    commodity = fields.Char(string="Commodity")
    product_family_id = fields.Many2one("product.family",string="Product Family")
    buyers_id = fields.Many2one("res.users",string="Buyers")


class ProductFamily(models.Model):
    _name = 'product.family'
    _inherit = ['mail.thread']
    _description = 'Product Family'
    _rec_name = 'complete_name'

    name = fields.Char("Name", tracking = True)
    code = fields.Char("Code", tracking = True)
    complete_name = fields.Char('Complete Name', compute='_compute_complete_name', store=True)

    _sql_constraints = [
    ('code_uniq', 'unique(code)', ' Please enter Unique Code.')
    ]

    @api.depends('name', 'code')
    def _compute_complete_name(self):
        for category in self:
            if category.code:
                category.complete_name = '%s - %s' % (category.code, category.name)
            else:
                category.complete_name = category.name
