import datetime

from odoo import models, fields, api


class sprint(models.Model):
    _name= 'managemario.sprint'
    _description='managemario.sprint'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del sprint")
    description=fields.Char(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de fin")
    tasks = fields.One2many(string="Tareas", comodel_name="managemario.task", inverse_name='sprint')
    project = fields.Many2one("managemario.project")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date