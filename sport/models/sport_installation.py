from odoo import _, api, fields, models

class Installation(models.Model):
    """ Installation """
    _name = 'sport.installation'
    _description = 'Installation'

    name = fields.Char(string='Nombre', size=50, required=True)
    location = fields.Char(string='Ubicacion', size=100)
    installation_type_id = fields.Many2one(string='Tipo de Pista', comodel_name='installation.type', required=True)
    rent_ids = fields.One2many(string='Alquileres', comodel_name='sport.rent', inverse_name='installation_id')