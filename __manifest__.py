# -*- coding: utf-8 -*-
{
    'name': "bradooCielo",

    'summary': """
        Aplicativo criado para realizar pagamentos com a nova API 3.0 		da Cielo""",

    'description': """
        Aplicativo criado para realizar pagamentos com a nova API 3.0 		da Cielo.
	Será implementado novas melhorias como:

		- Agendamento Pagamento Recursivo

    		- Gerar Boleto

    		- Pagamento Cartão de Crédito

    		- Pagamento Recursivo com Cartão de Crédito
    """,

    'author': "Bradoo Tech",
    'website': "bradootech.com:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'account',
        'payment',
        'website_sale',
        'br_base',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
