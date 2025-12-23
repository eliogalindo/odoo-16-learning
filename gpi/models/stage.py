from odoo import models, fields

class ProjectStage(models.Model):
    _name = 'gpi.project.stage'
    _description = 'Etapa de proyecto'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre', required=True)
    sequence = fields.Integer(string='Secuencia', default=10)
    fold = fields.Boolean(string='Plegar en kanban', help='Columna plegada por defecto')
