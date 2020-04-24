# -*- coding: utf-8 -*-
# from odoo import http


# class FirstAdoon(http.Controller):
#     @http.route('/first_adoon/first_adoon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first_adoon/first_adoon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_adoon.listing', {
#             'root': '/first_adoon/first_adoon',
#             'objects': http.request.env['first_adoon.first_adoon'].search([]),
#         })

#     @http.route('/first_adoon/first_adoon/objects/<model("first_adoon.first_adoon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_adoon.object', {
#             'object': obj
#         })
