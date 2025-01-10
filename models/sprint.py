from email.policy import default

from encodings.punycode import selective_find

from odoo import models, fields, api

import datetime

class sprint(models.Model):
    _name= 'managemario.sprint'
    _description='managemario.sprint'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del sprint")
    description=fields.Char(string="Descripción")
    duration = fields.Integer(default=15)
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(compute="_get_end_date", store=True)
    tasks = fields.One2many(string="Tareas", comodel_name="managemario.task", inverse_name='sprint')
    project = fields.Many2one("managemario.project")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date

    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managemario.sprint'].search([('project.id', '=', task.history.project.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint = sprint.id
                    found = True
            if not found:
                task.sprint = False

