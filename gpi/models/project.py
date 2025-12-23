from odoo import models, fields

class Project(models.Model):
    _name = 'gpi.project'
    _description = 'Gestión de proyectos'

    name = fields.Char(string='Nombre del Proyecto', required=True)
    description = fields.Text(string='Descripción')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')

    # Representa al cliente(Contacto) asociado al proyecto
    client_id = fields.Many2one('res.partner', string='Cliente', required=True)

    # Representa al usuario responsable del proyecto
    responsible_id = fields.Many2one('res.users', string='Responsable', required=True)

    # Etapa del proyecto que representa el estado del mismo con una relación con el modelo stage
    stage_id = fields.Many2one(
        'gpi.project.stage',
        string='Etapa',
        ondelete='restrict',
        index=True,
        tracking=True,
    )

    # Estado del proyecto
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', default='nuevo')
