# -*- coding: utf-8 -*-
# from odoo import http


# class StressTest(http.Controller):
#     @http.route('/stress_test/stress_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stress_test/stress_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stress_test.listing', {
#             'root': '/stress_test/stress_test',
#             'objects': http.request.env['stress_test.stress_test'].search([]),
#         })

#     @http.route('/stress_test/stress_test/objects/<model("stress_test.stress_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stress_test.object', {
#             'object': obj
#         })
