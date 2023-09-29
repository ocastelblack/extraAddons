from odoo import models, fields
import re
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request

class WebsiteSalePruebas(models.Model):
    _inherit = 'website'

    def prueba_hola_hse(self):
        return 'Hola'
    
    def extract_identification_type_number(self,checkout):
        # identification_type_id = str(checkout) 
        # match = re.search(r'\((\d+),\)', identification_type_id)

        # if match:
        #     extracted_number = match.group(1)
        # else:
        #     extracted_number = None

        # return extracted_number
    
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
        
        result = super(CustomWebsiteSale, self).address(**kw)
        
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
                
        if city_id:
            if partner_id:
                partner = request.env['res.partner'].sudo().browse(partner_id)
                partner.write({'city_id': city_id})
        

        #return super(CustomWebsiteSale, self).address(**kw)
        return result