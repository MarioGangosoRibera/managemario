
from odoo import models, fields, api

import datetime

class task(models.Model):
    _name = 'managemario.task'
    _description = 'managemario.task'

    def _get_definition_date(self):
        return datetime.datetime.now()

    project = fields.Many2one('managemario.project', related='history.project', readonly=True)
    code = fields.Char(compute="_get_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")  # Name
    description = fields.Text(string="Descripción")
    definition_date = fields.Datetime(default=_get_definition_date)
    start_date = fields.Datetime(string="Fecha inicio")
    end_date = fields.Datetime(string="Fecha fin")
    is_paused = fields.Boolean(string="¿Pausado?")
    sprint = fields.Many2one("managemario.sprint", compute = "_get_sprint", store=True)
    history = fields.Many2one("managemario.history", ondelete="set null", help="Historia relacionada")
    technologies = fields.Many2many(comodel_name="managemario.technology",
                                    relation="technologies_tasks",
                                    column1="task_id",
                                    column2="technology_id")

    # @api.one
    def _get_code(self):
        for task in self:
            # try:
            task.code = "TSK_" + str(task.id)
            # _logger.info("Código generado: "+task.code)
        # except:
        # raise ValidationError(_("Generación de código errónea"))
