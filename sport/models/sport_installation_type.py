from odoo import _, api, fields, models

class InstallationType(models.Model):
    """ Installation Type """
    _name = 'installation.type'
    _description = 'Installation Type'

    name = fields.Char(string='Nombre', size=50, required=True)
    installation_ids = fields.One2many(string='Instalaciones', comodel_name='sport.installation', inverse_name='installation_type_id')
