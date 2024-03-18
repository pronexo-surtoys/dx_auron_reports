from odoo import fields, models, api, _
from odoo.fields import Command
from datetime import timedelta
from collections import defaultdict


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self, **optional_values):
        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        values['product_packaging_qty'] = self.product_packaging_qty
        values['product_packaging_id'] = self.product_packaging_id.id
        values['price_reduce'] = self.price_reduce
        return values
