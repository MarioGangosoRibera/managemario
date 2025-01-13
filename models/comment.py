from odoo import models, fields

class Comment(models.Model):
    _name = 'managemario.comment'
    _description = 'Comentarios para proyectos y tareas'

    name = fields.Char(string='Título', required=True)
    content = fields.Text(string='Contenido', required=True)
    task_id = fields.Many2one('managemario.task', string='Tarea relacionada', ondelete='cascade')
    project_id = fields.Many2one('managemario.project', string='Proyecto relacionado', ondelete='cascade')
    created_at = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now)