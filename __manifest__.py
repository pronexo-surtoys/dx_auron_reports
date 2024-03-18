# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Auron Reports.',
    'version': '16.0.0.0',
    'sequence': 4,
    'summary': 'Auron Reports.',
    'price': 84,
    'currency': 'EUR',
    'category': 'Extra Tools',
    'description': """
    
    """,
    'author': 'Pronexo',
    'license': 'OPL-1',
    'website': 'https://www.pronexo.ar',
    'depends': ['base', 'contacts','sale_management', 'account', 'l10n_ar_sale', 'l10n_ar'],
    'data': [

        # security
        # "security/import_security.xml",
        # 'security/ir.model.access.csv',

        # views
        "views/sale_order_view.xml",
        "views/account_move_view.xml",
        "views/stock_move_view.xml",
        "views/res_partner.xml",
        "views/product_product.xml",

        # reports
        "reports/report_saleorder_document_features.xml",
        "reports/report_delivery_document_extended.xml",
        "reports/report_purchaseorder_document_inherit.xml",
        "reports/report_remito.xml",
        "reports/report_invoice_document_inherit.xml",
    ],
    'qweb': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
