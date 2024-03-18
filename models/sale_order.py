# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    origin_dispatch_product = fields.Text(string="Despacho Origen y Aduana")

    @api.onchange('product_id', 'product_template_id')
    def onchange_product_template_dispatch(self):
        for line in self:            
            line.origin_dispatch_product = line.product_template_id.origin_dispatch
