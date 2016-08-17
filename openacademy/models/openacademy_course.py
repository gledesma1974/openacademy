# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
