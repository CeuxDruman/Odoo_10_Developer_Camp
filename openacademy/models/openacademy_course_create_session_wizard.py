from odoo import _, api, fields, models, exceptions

class OpenacademyCourseCreateSessionWizard(models.TransientModel):

    _name = 'openacademy.course.create.session.wizard'
    _description = 'Openacademy Course Create Session Wizard'

    title = fields.Char(string='Titulo', size=50)
    instructor_id = fields.Many2one(string='Instructor', comodel_name='res.partner')
    start_moment = fields.Datetime(string='Fecha de comienzo')
    duration = fields.Integer(string='Duracion')
    seats = fields.Integer(string='Plazas')

    @api.one
    def create_session_wizard(self):
        session_obj = self.env['openacademy.session']

        new_session = session_obj.create({
            'title':self.title,
            'instructor_id':self.instructor_id.id,
            'start_moment':self.start_moment,
            'duration':self.duration,
            'seats':self.seats,
            'course_id':self._context.get('active_id')
        })