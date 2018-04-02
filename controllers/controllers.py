# -*- coding: utf-8 -*-
from odoo import http

# class BradooCielo(http.Controller):
#     @http.route('/bradoo_cielo/bradoo_cielo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bradoo_cielo/bradoo_cielo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bradoo_cielo.listing', {
#             'root': '/bradoo_cielo/bradoo_cielo',
#             'objects': http.request.env['bradoo_cielo.bradoo_cielo'].search([]),
#         })

#     @http.route('/bradoo_cielo/bradoo_cielo/objects/<model("bradoo_cielo.bradoo_cielo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bradoo_cielo.object', {
#             'object': obj
#         })