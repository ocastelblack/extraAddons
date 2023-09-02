import datetime
from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'

    @api.model
    def _format_expiration_date(self, expiration_date_str):
        # Convierte la fecha ingresada en el formato deseado
        try:
            formatted_date = datetime.datetime.strptime(expiration_date_str, '%Y-%M-%D %H:%M:%S')
        except ValueError:
            # Manejar errores si la fecha no se puede convertir correctamente
            formatted_date = None
        return formatted_date

    @api.model
    def create(self, vals):
        # Antes de crear un nuevo registro, formatea la fecha de expiration_date
        if 'expiration_date' in vals:
            formatted_date = self._format_expiration_date(vals['expiration_date'])
            if formatted_date:
                vals['expiration_date'] = formatted_date

        return super(StockLot, self).create(vals)

    def write(self, vals):
        # Antes de actualizar un registro, formatea la fecha de expiration_date
        if 'expiration_date' in vals:
            formatted_date = self._format_expiration_date(vals['expiration_date'])
            if formatted_date:
                vals['expiration_date'] = formatted_date

        return super(StockLot, self).write(vals)