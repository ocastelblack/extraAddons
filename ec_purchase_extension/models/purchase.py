# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.depends('product_qty', 'qty_received',
                 'order_id', 'order_id.effective_date', 'order_id.date_planned')
    def _compute_qty(self):
        for record in self:
            days_late = 0
            record.reamining_qty = record.product_qty - record.qty_received or  0
            record.fully_received = record.qty_received ==  record.product_qty
            record.to_be_received = record.qty_received <  record.product_qty
            if record.order_id.effective_date:
                days_late = record.order_id.date_planned\
                    and (record.order_id.effective_date.date() - record.order_id.date_planned.date()).days or 0
            elif not record.order_id.effective_date:
                days_late = record.order_id.date_planned\
                    and (fields.Date.today() - record.order_id.date_planned.date()).days or 0
            record.days_late = days_late


    commodity = fields.Char(related="product_id.product_tmpl_id.commodity",string="Commodity",store=True)
    product_family_id = fields.Many2one(related="product_id.product_tmpl_id.product_family_id",string="Product Family",store=True)
    buyers_id = fields.Many2one(related="product_id.product_tmpl_id.buyers_id", string="Buyers",store=True)
    po_name = fields.Char(related='order_id.name',string="Name", store=True)
    date_approve = fields.Datetime(related='order_id.date_approve', string="Confirmation Date", store=True)
    days_late = fields.Integer(compute='_compute_qty',string="Days Late", store=True)
    dest_address_id = fields.Many2one(related='order_id.dest_address_id',string="Receipt Location", store=True)
    invoice_status = fields.Selection(related='order_id.invoice_status',string="Billing Status", store=True)
    partner_ref = fields.Char(related='order_id.partner_ref',string="Vendor Reference", store=True)
    default_code = fields.Char(related="product_id.default_code",string="Part", store=True)
    purchase_rep = fields.Many2one(related="order_id.user_id",string="Purchase Rep", store=True)
    line_effective_date = fields.Datetime(related='order_id.effective_date', string="Effective Date", store = True)
    recieved_amount = fields.Float("Dollar Value Received", compute="_compute_rec_bill_amount", store=True)
    invoiced_amount = fields.Float("Dollar Value Invoiced", compute="_compute_rec_bill_amount", store=True)
    dollar_subtotal = fields.Float("Dollar Value Subtotal", compute="_compute_rec_bill_amount", store=True)
    reamining_qty = fields.Float("Remaining Qty.", compute="_compute_qty", store=True)
    date = fields.Date("Date",default=date.today())
    fully_received = fields.Boolean("Fully Received",compute="_compute_qty", store=True)
    to_be_received = fields.Boolean("To Be Received",compute="_compute_qty", store=True)

    def purchase_transfer(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'view_mode': 'form',
                'res_id': self.order_id.id,
                'target':'current'}

    @api.depends('qty_received','price_unit','invoice_lines', 'invoice_lines.move_id', 'invoice_lines.move_id.state')
    def _compute_rec_bill_amount(self):
        for rec in self:
            recieved_amount = rec.qty_received * rec.price_unit or 0
            invoiced_amount = sum([line.price_subtotal for line in rec.invoice_lines if line.price_subtotal > 0 and line.move_id.state=='posted']) or 0.0
            rec.dollar_subtotal = rec.order_id.currency_id._convert(rec.price_subtotal, rec.order_id.company_id.currency_id, rec.order_id.company_id, rec.date) or 0
            rec.recieved_amount = rec.order_id.currency_id._convert(recieved_amount, rec.order_id.company_id.currency_id, rec.order_id.company_id, rec.date) or 0
            rec.invoiced_amount = rec.order_id.currency_id._convert(invoiced_amount, rec.order_id.company_id.currency_id, rec.order_id.company_id, rec.date) or 0
