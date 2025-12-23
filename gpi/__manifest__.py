{
    'name': 'Gestión de Proyectos Internos',
    'version': '16.0.1.0.0',
    'summary': 'Un módulo para la gestión de proyectos internos',
    'description': 'Proyectos con pipeline kanban, integrados a contactos y usuarios.',
    'author': 'Elio',
    'category': 'Operations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/stages.xml',
        'views/project_views.xml',
    ],
    'installable': True,
    'application': True,
}
