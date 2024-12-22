
from odoo import models, fields, api


class task(models.Model):
    _name = 'managemario.task'
    _description = 'managemario.task'

    code = fields.Char(compute="_get_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")  # Name
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha inicio")
    end_date = fields.Datetime(string="Fecha fin")
    is_paused = fields.Boolean(string="¿Pausado?")
    sprint = fields.Many2one("managemario.sprint")
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
