from odoo import _, api, fields, models, exceptions
from datetime import date

class NewUserWizard(models.TransientModel):

    _name = 'new.user.wizard'
    _description = 'New User Wizard'

    name = fields.Char(string='Nombre de usuario', required=True, size=128)
    phone_number = fields.Char(string='Telefono de contacto', size=64)
    email = fields.Char(string='Email de contacto', size=240)
    coupon_code = fields.Char(string='Codigo de Alta', size=12, required=True)

    @api.one
    def register_new_user_wizard(self):
        user_coupon_obj = self.env['user.coupon']
        res_partner_obj = self.env['res.partner']

        for coupon in user_coupon_obj.search([]):
            if coupon.code == self.coupon_code:
                if coupon.is_used == True and fields.Date.from_string(coupon.expiration_date) <= date.today():
                    raise exceptions.ValidationError('Este cupon esta caducado y ademas ya ha sido usado.')
                elif coupon.is_used:
                    raise exceptions.ValidationError('Este cupon ya ha sido usado.')
                elif fields.Date.from_string(coupon.expiration_date) <= date.today():
                    raise exceptions.ValidationError('Este cupon esta caducado.')
                else :
                    new_res_partner = res_partner_obj.create({
                        'name': self.name,
                        'phone': self.phone_number,
                        'email': self.email,
                        'is_sport_installation_user': True
                    })

                    coupon.is_used = True

                    return

        raise exceptions.ValidationError('Este cupon no existe.')
