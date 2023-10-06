from odoo import models, fields,api
import re
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

class WebsiteSalePruebas(models.Model):
    _inherit = 'website'

    def prueba_hola_hse(self):
        return 'Hola'
    
    def extract_identification_type_number(self,checkout):
        if checkout:
            identification_type_id = str(checkout)
            match = re.search(r'\((\d+),\)', identification_type_id)
            if match:
                extracted_number = match.group(1)
            else:
                extracted_number = 1  # Set the default value to 1 if checkout is not provided or is empty
        else:
            extracted_number = 1  # Set the default value to 1 if checkout is not provided or is empty

        return int(extracted_number)
    
    def get_identification_types(self):
        identification_types = self.env['l10n_latam.identification.type'].search([])
        return identification_types
    
    def get_city_types(self):
        city_types = self.env['res.city'].search([])
        return city_types
 
class CustomWebsiteSale(WebsiteSale):
    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):

        is_company = False
        identification_type_id_str = kw.get('identification_type_id')
        city_id_str = kw.get('city_type')
        order = request.website.sale_get_order()
        partner_id = order.partner_id.id 
        
        if identification_type_id_str:
            l10n_latam_identification_type_id = int(identification_type_id_str)
        else:
            l10n_latam_identification_type_id = False
            
        if city_id_str:
            city_id = int(city_id_str)
        else:
            city_id = False
            
        is_company_str = kw.get('radio_field')
        
        if l10n_latam_identification_type_id !=4 and is_company_str=='individual':
            # Crear el contexto con la clave 'no_vat_validation' establecida en True
            context = dict(request.env.context)
            context['no_vat_validation'] = True
            request.env.context = context

        if l10n_latam_identification_type_id:
            if partner_id:
                partner = request.env['res.partner'].sudo().browse(partner_id)
                partner.write({'l10n_latam_identification_type_id': l10n_latam_identification_type_id})
        
        if is_company_str:
            if is_company_str=='individual':
                is_company= False
            else:
                is_company= True
                
            if partner_id:
                partner = request.env['res.partner'].sudo().browse(partner_id)
                partner.write({'is_company': is_company})
                kw['is_company'] = is_company
                
        if city_id:
            if partner_id:
                partner = request.env['res.partner'].sudo().browse(partner_id)
                partner.write({'city_id': city_id})

        kw['city'] = 'Bogotá D.C.'
        result = super(CustomWebsiteSale, self).address(**kw)
        # Restablecer el contexto original si es necesario
        #context.pop('no_vat_validation', None)
        #self = self.with_context(context)
        #return super(CustomWebsiteSale, self).address(**kw)
        return result
        
    def _checkout_form_save(self, mode, checkout, all_values):
        if 'identification_type_id' in all_values:
            checkout['l10n_latam_identification_type_id'] = all_values['identification_type_id']
        if 'city_type' in all_values:
            checkout['city_id'] = all_values['city_type']
        if 'is_company' in all_values:
            checkout['is_company'] = all_values['is_company']
        result = super(CustomWebsiteSale, self)._checkout_form_save(mode, checkout, all_values)
        return result
        
    def checkout_form_validate(self, mode, all_form_values, data):

        resultck = super(CustomWebsiteSale, self).checkout_form_validate(mode, all_form_values, data)

        err = resultck[0]
        msg = resultck[1]

        if err and err["vat"] == "error":
            if(data["radio_field"]=="individual"):
                if(data["identification_type_id"] !=4):
                    error = dict()
                    error_message = []
                    patron = r'^[0-9]+$'
                    cedula = data["vat"]
                    if not re.match(patron, cedula):
                        error["vat"] = 'error'
                        error_message.append('Solo se aceptan números, no se admiten puntos ni espacios ni caracteres especiales. Por favor, ingrese un número de documento válido.')
                        return error, error_message
                    else:      
                        return error, error_message
        
        return resultck

# class CustomResPartner(models.Model):
#     _inherit = 'res.partner'

#     def _build_vat_error_message(self, country_code, wrong_vat, record_label):
#         if self.env.context.get('company_id'):
#             company = self.env['res.company'].browse(self.env.context['company_id'])
#         else:
#             company = self.env.company

#         id_tipo = ("l10n_latam_identification_type_id")
#         is_company = ("is_company")

#         if id_tipo != "4":
#             if is_company:
#                 return ""