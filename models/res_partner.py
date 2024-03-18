from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    carrier = fields.Char(string='Transportista', required=False)
    address_carrier = fields.Text(string='Direccion del Transporte', required=False)
