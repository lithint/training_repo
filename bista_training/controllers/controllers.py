# -*- coding: utf-8 -*-
# from odoo import http


# class BistaTraining(http.Controller):
#     @http.route('/bista_training/bista_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bista_training/bista_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bista_training.listing', {
#             'root': '/bista_training/bista_training',
#             'objects': http.request.env['bista_training.bista_training'].search([]),
#         })

#     @http.route('/bista_training/bista_training/objects/<model("bista_training.bista_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bista_training.object', {
#             'object': obj
#         })
