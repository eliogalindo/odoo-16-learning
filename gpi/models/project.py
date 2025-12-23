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
        group_expand='_read_group_stage_ids',
    )

    # Estado del proyecto
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', default='nuevo')

    # función para expandir todas las etapas en el kanban
    def _read_group_stage_ids(self, stages, domain, order):
        # stages es un recordset de gpi.project.stage
        # domain y order son parámetros de agrupación
        return stages.search([])
