from odoo import models, fields, api


class history(models.Model):
    _name = 'managemario.history'
    _description = 'managemario.history'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del history")
    description = fields.Char(string="Descripción")
    project = fields.Many2one("managemario.project", ondelete="set null")
    tasks = fields.One2many(string="Tareas", comodel_name="managemario.task", inverse_name="history")

    used_technologies = fields.Many2many("managemario.technology", compute="_get_used_techonologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.tasks:
                if not technologies:
                    technologies = task.technologies
                else:
                    technologies = technologies + task.technologies
            history.used_technologies = technologies