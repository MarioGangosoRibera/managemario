from odoo import models, fields, api


class history(models.Model):
    _name= 'managemario.technology'
    _description='managemario.technology'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del technology")
    description=fields.Char(string="Descripción")
    image = fields.Image(string="Imagen")

    tasks = fields.Many2many(comodel_name="managemario.task",
                             relation="technologies_tasks",
                             column1="technology_id",
                             column2="task_id")