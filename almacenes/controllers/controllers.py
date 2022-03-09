# -*- coding: utf-8 -*-
# from odoo import http


# class Almacenes(http.Controller):
#     @http.route('/almacenes/almacenes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almacenes/almacenes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('almacenes.listing', {
#             'root': '/almacenes/almacenes',
#             'objects': http.request.env['almacenes.almacenes'].search([]),
#         })

#     @http.route('/almacenes/almacenes/objects/<model("almacenes.almacenes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almacenes.object', {
#             'object': obj
#         })
