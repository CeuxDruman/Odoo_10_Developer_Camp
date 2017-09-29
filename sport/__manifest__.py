# -*- coding: utf-8 -*-
# Copyright 2017 Carlos Alberto Mata Gil
# License AGPL-3.0 or later (http://www.gnu.org/licenses/apgl).

{
    'name': 'Sport',
    'version': '1.0',
    'category': 'Sport / Rental',
    'summary': 'Gestion de reservas de instalaciones deportivas.',
    'description': """================
 Gestion de reservas de instalaciones deportivas.
================
    
    Realiza la gestion completa de las instalaciones, asi como las reservas a las mismas y los usuarios que pueden reservar pistas.
    
* **Nueva Reserva**: Este flujo permite crear una solicitud de reserva a una pista deportiva en una fecha determinada.

* **Generar cupones de usuario**: Para dar de alta nuevos usuarios en el sistema, se usara un sistema de cupones.

* **Alta de nuevos usuarios**: Para los usuarios del sistema se filtrara aquellos usuarios que puedan reservar pistas.""",
    'author': 'Carlos Alberto Mata Gil',
    'website': 'http://www.CeuxDruman.com',
    'depends': [],
    'data': ['views/sport_installation_type_view.xml',
             'views/sport_installation_view.xml',
             'views/sport_rent_view.xml',
             'views/sport_rent_wizard_view.xml',
             'views/sport_res_partner_view.xml',
             'views/sport_user_coupon_view.xml',
             'views/sport_user_coupon_generation_wizard_view.xml',
             'views/sport_new_user_wizard_view.xml'],
    'installable': True,
    'active': False,
}