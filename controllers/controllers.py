# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderAudric14(http.Controller):
#     @http.route('/booking_order_audric_14/booking_order_audric_14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_audric_14/booking_order_audric_14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_audric_14.listing', {
#             'root': '/booking_order_audric_14/booking_order_audric_14',
#             'objects': http.request.env['booking_order_audric_14.booking_order_audric_14'].search([]),
#         })

#     @http.route('/booking_order_audric_14/booking_order_audric_14/objects/<model("booking_order_audric_14.booking_order_audric_14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_audric_14.object', {
#             'object': obj
#         })
