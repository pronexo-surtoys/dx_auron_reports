from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_packaging_qty = fields.Float("Cajas", related="sale_line_id.product_packaging_qty")
    origin_dispatch_product = fields.Text("Despacho Origen y Aduana", related="sale_line_id.origin_dispatch_product")
