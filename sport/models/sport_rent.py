from odoo import _, api, fields, models

class Rent(models.Model):
    """ Rent """
    _name = 'sport.rent'
    _description = 'Rent'
    _rec_name = 'start_date'

    start_date = fields.Datetime(string='Fecha de inicio del alquiler', required=True)
    end_date = fields.Datetime(string='Fecha de fin del alquiler', required=True)
    installation_id = fields.Many2one(string='Instalacion', comodel_name='sport.installation', required=True)
    res_partner_id = fields.Many2one(string='Persona que reserva', comodel_name='res.partner', required=True, domain="[('is_sport_installation_user','=',True)]")
