# -*- coding: utf-8 -*-

{
    'name': 'auth_partner_form_birthdate',
    'summary': '''Auth Partner form without required birthdate''',
    'description': '''
auth_partner_form_birthdate
================================
Removes the birthdate as required field.
    ''',
    'author': 'DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'auth_partner_form',
    ],
    'data': [
        'views/templates.xml',
    ],
}