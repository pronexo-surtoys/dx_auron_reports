# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, exceptions, api, _

import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    origin_dispatch = fields.Char(string='Despacho Origen y Aduana')


class ProductProduct(models.Model):
    _inherit = "product.product"

    origin_dispatch = fields.Char(string='Despacho Origen y Aduana Related', related="product_tmpl_id.origin_dispatch",
                                  readonly=False, store=True)
