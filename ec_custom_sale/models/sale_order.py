# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2021 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoiced_amount = fields.Float("Invoiced Amount", compute="_compute_invoice_amount")
    to_invoice_amount = fields.Float(
        "Remaining to Invoice", compute="_compute_invoice_amount"
    )

    def _compute_invoice_amount(self):
        for rec in self:
            rec.invoiced_amount = (
                rec.invoice_ids
                and sum(
                    rec.invoice_ids.filtered(lambda l: l.state == "posted").mapped(
                        "amount_total"
                    )
                )
                or 0.00
            )
            rec.to_invoice_amount = rec.amount_total - rec.invoiced_amount
