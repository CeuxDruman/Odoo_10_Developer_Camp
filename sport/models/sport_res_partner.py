from odoo import _, api, fields, models

class User(models.Model):
    """ User """
    _inherit = 'res.partner'

    is_sport_installation_user = fields.Boolean(string='Usuario de las instalaciones deportivas')
    rent_ids = fields.One2many(string='Alquileres efectuados', comodel_name='sport.rent', inverse_name='res_partner_id')
