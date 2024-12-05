# -*- coding: utf-8 -*-
# from odoo import http


# class Managemario(http.Controller):
#     @http.route('/managemario/managemario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managemario/managemario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managemario.listing', {
#             'root': '/managemario/managemario',
#             'objects': http.request.env['managemario.managemario'].search([]),
#         })

#     @http.route('/managemario/managemario/objects/<model("managemario.managemario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managemario.object', {
#             'object': obj
#         })
