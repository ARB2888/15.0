# -*- coding: utf-8 -*-
# from odoo import http


# class DarkMode(http.Controller):
#     @http.route('/dark_mode/dark_mode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dark_mode/dark_mode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dark_mode.listing', {
#             'root': '/dark_mode/dark_mode',
#             'objects': http.request.env['dark_mode.dark_mode'].search([]),
#         })

#     @http.route('/dark_mode/dark_mode/objects/<model("dark_mode.dark_mode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dark_mode.object', {
#             'object': obj
#         })
