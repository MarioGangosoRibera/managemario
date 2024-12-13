from odoo import models, fields, api


class developer(models.Model):
    _name= 'res.partner'
    _inherit='res.partner'

    technologies = fields.Many2many(comodel_name="managemario.technology",
                             relation="developer_technologies",
                             column1="developer_id",
                             column2="technologies_id")