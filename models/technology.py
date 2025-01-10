from odoo import models, fields, api


class history(models.Model):
    _name= 'managemario.technology'
    _description='managemario.technology'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del technology")
    description=fields.Text(string="Descripción")
    image = fields.Image(string="Imagen", max_width=200, max_height=200)

    tasks = fields.Many2many(comodel_name="managemario.task",
                             relation="technologies_tasks",
                             column1="technology_id",
                             column2="task_id")