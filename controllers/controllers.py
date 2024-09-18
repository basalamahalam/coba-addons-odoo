# -*- coding: utf-8 -*-
# from odoo import http


# class FitsOdooTechnical(http.Controller):
#     @http.route('/fits_odoo_technical/fits_odoo_technical', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fits_odoo_technical/fits_odoo_technical/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fits_odoo_technical.listing', {
#             'root': '/fits_odoo_technical/fits_odoo_technical',
#             'objects': http.request.env['fits_odoo_technical.fits_odoo_technical'].search([]),
#         })

#     @http.route('/fits_odoo_technical/fits_odoo_technical/objects/<model("fits_odoo_technical.fits_odoo_technical"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fits_odoo_technical.object', {
#             'object': obj
#         })

