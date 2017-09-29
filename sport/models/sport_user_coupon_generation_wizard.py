from odoo import _, api, fields, models, exceptions
import random
import string
from datetime import date

class UserCouponGenerationWizard(models.TransientModel):

    _name = 'user.coupon.generation.wizard'
    _description = 'User Coupon Generation Wizard'

    expiration_date = fields.Date(string='Fecha de validez', required=True, help="A partir de esta fecha, el cupon ya no sera valido para su uso.")

    def get_random_code(self, max_length):
        """ Given a max length, it returns a random string of uppercase characters and numbers """
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(max_length))

    @api.one
    def generate_user_coupon_wizard(self):
        user_coupon_obj = self.env['user.coupon']

        generated_user_coupon = user_coupon_obj.create({
            'code': self.get_random_code(12),
            'expiration_date': self.expiration_date
        })

    @api.one
    @api.constrains('expiration_date')
    def _check_expiration_date(self):
        if fields.Date.from_string(self.expiration_date) <= date.today():
            raise exceptions.ValidationError('La fecha de validez tiene que estar en el futuro.')