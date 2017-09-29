from odoo import _, api, fields, models, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Es instructor')
    is_assistant = fields.Boolean(string='Es asistente')
    assistant_age = fields.Integer(string='Edad (Asistente)')
    sessions_as_instructor = fields.Integer(string='Sesiones', compute="_compute_sessions_as_instructor")
    sessions_as_assistant = fields.Integer(string='Sesiones', compute="_compute_sessions_as_assistant")

    @api.one
    @api.constrains('is_instructor','is_assistant')
    def _check_instructor_assistant(self):
        if self.is_instructor == True and self.is_assistant == True:
            raise exceptions.ValidationError('Solo puede ser instructor o asistente a la vez')

    @api.multi
    def open_sessions_as_instructor(self):
        return {
            'name': 'Sessions as instructor',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'openacademy.session',
            'type': 'ir.actions.act_window',
            'domain': '[("instructor_id","=",%d)]' % self.id
        }

    @api.multi
    def open_sessions_as_assistant(self):
        return {
            'name': 'Sessions as assistant',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'openacademy.session',
            'type': 'ir.actions.act_window',
            'domain': '[("assistant_ids","in",%d)]' % self.id
        }

    @api.one
    def _compute_sessions_as_instructor(self):
        if self.is_instructor == True:
            session_obj = self.env['openacademy.session']

            all_sessions = session_obj.search([('instructor_id','=',self.id)])
            self.sessions_as_instructor = len(all_sessions)

    @api.one
    def _compute_sessions_as_assistant(self):
        if self.is_assistant == True:
            session_obj = self.env['openacademy.session']

            all_sessions = session_obj.search([('assistant_ids','in',self.id)])
            self.sessions_as_assistant = len(all_sessions)