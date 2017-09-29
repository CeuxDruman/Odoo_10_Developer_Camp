from odoo import _, api, fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Session(models.Model):
    """ Session """
    _name = 'openacademy.session'
    _description = 'Session'
    _rec_name = 'title'


    title = fields.Char(string='Titulo', size=50)
    course_id = fields.Many2one(string='Curso', comodel_name='openacademy.course')
    instructor_id = fields.Many2one(string='Instructor', comodel_name='res.partner')
    start_moment = fields.Datetime(string='Fecha de comienzo')
    duration = fields.Integer(string='Duracion')
    end_moment = fields.Datetime(string='Fecha de finalizacion', compute='_compute_end_moment')
    available_seats = fields.Integer(string='Plazas disponibles')
    assistant_ids = fields.Many2many(string='Asistentes', comodel_name='res.partner', domain=[('is_assistant','=',True)])
    assistance_percentage = fields.Float(string='Porcentaje de asistencia', compute='_compute_assistance_percentage')

    @api.one
    @api.depends('start_moment', 'duration')
    def _compute_end_moment(self):
        if self.start_moment and self.duration:
            self.end_moment = ( datetime.strptime(self.start_moment, '%Y-%m-%d %H:%M:%S') + relativedelta(days=self.duration) ).strftime('%Y-%m-%d %H:%M:%S')  # fields.Datetime.from_string(self.start_moment) = datetime.strptime(self.start_moment, '%Y-%m-%d %H:%M:%S')

    @api.one
    @api.depends('available_seats', 'assistant_ids')
    def _compute_assistance_percentage(self):
        if self.available_seats and self.assistant_ids:
            self.assistance_percentage = (len(self.assistant_ids) * 100.0) / self.available_seats
