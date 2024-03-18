from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_packaging_qty = fields.Float(string='Cajas', required=False)
    product_packaging_id = fields.Many2one(comodel_name='product.packaging', string='Empaquetado', required=False)
    price_reduce = fields.Float(string='Precio Final', required=False)
