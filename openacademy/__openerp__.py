# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Openacademy",  # Nombre del modulo al buscar
    "summary": "Modulo de Cursos",  # Descripcion pequeña
    "version": "9.0.1.0.0",
    "category": "Cursos",  # Agrupar por modulos
    "website": "https://gila.com.mx/",
    "author": "Gabriel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "view/some_model_view.xml",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
    ],
}
