from odoo import models, fields, api


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
        ('new', 'Nuevo'),
        ('in_progress', 'En Progreso'),
        ('in_checking', 'En Revisión'),
        ('done', 'Finalizado'),
    ], string='Estado', default='new')

    # función para expandir todas las etapas en el kanban
    # aunque no tengan proyectos relacionados
    def _read_group_stage_ids(self, stages, domain, order):
        # stages es un recordset de gpi.project.stage
        # domain y order son parámetros de agrupación
        return stages.search([])

    # sincroniza la etapa del proyecto con su stage_id
    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.stage_id:
            if self.stage_id.name.lower() == 'new':
                 self.state = 'new'
            elif self.stage_id.name.lower() in ['in progress', 'progress']:
                 self.state = 'in_progress'
            elif self.stage_id.name.lower() in ['in checking', 'checking']:
                 self.state = 'in_checking'
            elif self.stage_id.name.lower() == 'done':
                 self.state = 'done'