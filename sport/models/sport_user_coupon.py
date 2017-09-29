from odoo import _, api, fields, models

class Coupon(models.Model):
    """ Coupon """
    _name = 'user.coupon'
    _description = 'Coupon'
    _rec_name = 'code'

    code = fields.Char(string='Codigo', size=12, required=True)
    is_used = fields.Boolean(string='Codigo usado', default=False, required=True)
    expiration_date = fields.Date(string='Fecha de validez', required=True, help="A partir de esta fecha, el cupon ya no sera valido para su uso.")
