from odoo import _, api, fields, models, exceptions

class Course(models.Model):
    """ Course """
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Nombre', size=50)
    description = fields.Text(string='Descripcion', size=1000)
    session_ids = fields.One2many(string='Sesiones', comodel_name='openacademy.session', inverse_name='course_id', readonly=True)
    state = fields.Selection(string='Estado', selection=[('por_empezar','Por empezar'),('activo','Activo'),('finalizado','Finalizado')], default='por_empezar')
    min_assitants = fields.Integer(string='Minimo de participantes')

    @api.one
    def activate(self):
        activar = True
        if len(self.session_ids) > 0:
            for session in self.session_ids:
                if len(session.assistant_ids) < self.min_assitants:
                    activar = False
        else:
            activar = False

        if activar == True:
            self.state = 'activo'
        else:
            raise exceptions.Warning('El curso no tiene el minimo de asistenes para poder activarse.')

    @api.one
    def finalize(self):
        self.state = 'finalizado'

    @api.multi
    def open_create_session_wizard(self):
        return {
            'name': 'Create Session Wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'openacademy.course.create.session.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }