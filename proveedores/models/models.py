# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proveedores(models.Model):
#     _name = 'proveedores.proveedores'
#     _description = 'proveedores.proveedores'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models ,fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class proveedores(models.Model):
    _name = 'proveedores.proveedores'
    _description = 'Define los atributos'

    #Atributos
    dniSupp = fields.Char(string='DNI', required=True)
    nombreSupp = fields.Char(string='Nombre del proveedor')
    telefonoSupp = fields.Char(string='Telefono')
    emailSupp = fields.Char(string='Email')

class repartos(models.Model):
    _name = 'proveedores.repartos'
    _description = 'Define los atributos'

    #Atributos
    cod = fields.Char(string='Codigo')
    fecha = fields.Date(string='Fecha de reparto', default = fields.date.today())