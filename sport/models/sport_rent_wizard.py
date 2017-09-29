from odoo import _, api, fields, models, exceptions
from dateutil.relativedelta import relativedelta

class SportRentWizard(models.TransientModel):

    _name = 'sport.rent.wizard'
    _description = 'Sport Rent Wizard'

    start_date = fields.Datetime(string='Fecha de inicio', required=True)
    duration = fields.Integer(string='Duracion - Minutos', required=True)
    res_partner_id = fields.Many2one(string='Usuario que reserva', comodel_name='res.partner', domain="[('is_sport_installation_user','=',True)]", required=True)
    installation_type_id = fields.Many2one(string='Tipo de pista', comodel_name='installation.type', required=True)
    installation_id = fields.Many2one(string='Pista', comodel_name='sport.installation', domain="[('installation_type_id','=',installation_type_id)]", required=True)

    @api.one
    def new_rent_wizard(self):
        rent_obj = self.env['sport.rent']

        new_rent = rent_obj.create({
            'start_date': self.start_date,
            'end_date': ( fields.Datetime.from_string(self.start_date) + relativedelta(minutes=self.duration) ).strftime('%Y-%m-%d %H:%M:%S'),
            'installation_id': self.installation_id.id,
            'res_partner_id': self.res_partner_id.id
        })

    @api.one
    @api.constrains('duration')
    def _check_duration(self):
        if self.duration <= 0:
            raise exceptions.ValidationError('La duracion del alquiler debe ser de al menos 1 hora.')

    @api.one
    @api.constrains('installation_id')
    def _check_installations(self):
        end_date = ( fields.Datetime.from_string(self.start_date) + relativedelta(minutes=self.duration) ).strftime('%Y-%m-%d %H:%M:%S')
        for rent in self.installation_id.rent_ids:
            if (rent.start_date <= self.start_date <= rent.end_date) or (rent.start_date <= end_date <= rent.end_date):
                raise exceptions.ValidationError('Lo siento, esta pista esta ya reservada de %s a %s.' % (rent.start_date,rent.end_date))