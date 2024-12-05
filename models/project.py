from odoo import models, fields, api


class project(models.Model):
    _name= 'managemario.project'
    _description='managemario.project'

    name=fields.Char(string='Name', readonly=False, required=True, help="Introduce el nombre del proyecto")
    description=fields.Char(string="Descripción")
    histories = fields.One2many(comodel_name="managemario.history", inverse_name="project")
    sprints = fields.One2many(comodel_name="managemario.sprint", inverse_name="project")