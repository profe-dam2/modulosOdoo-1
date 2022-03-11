# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class almacenes(models.Model):
#     _name = 'almacenes.almacenes'
#     _description = 'almacenes.almacenes'

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

class almacenes(models.Model):
    _name = 'almacenes.almacenes'
    _description = 'Define los atributos'

    #Atributos
    nombreAlm = fields.Char(string='Nombre del almacen')
    direccionAlm = fields.Char(string='Direccion')


class productos(models.Model):
    _name = 'almacenes.productos'
    _description = 'Define los atributos'

    #Atributos
    nombreProd = fields.Char(string='Nombre del producto')
    tipoProd = fields.Selection(string='Tipo de producto', selection=[('a','fresco'),('b','congelado'),('c','enlatado'),('d','empaquetado')], help='Estado del alimento')
    cantidadProd = fields.Integer(string='Cantidad')
    descripcionProd = fields.Text(string='Descripcion del producto')