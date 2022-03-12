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
from odoo import models, fields, api, exceptions
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
    
    @api.constrains('dniSupp')
    def _checkdni(self):
        for proveedores in self:
            if(len(proveedores.dniSupp) > 9):
                raise exceptions.ValidationError("El DNI no puede ser superior a 9 caracteres")
            if(len(proveedores.dniSupp) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos de 9 caracteres")
    
    #Relacion entre tablas
    reparto_cod = fields.One2many('proveedores.repartos','proveedor_id', string='Repartos')

class repartos(models.Model):
    _name = 'proveedores.repartos'
    _description = 'Define los atributos'

    #Atributos
    cod = fields.Char(string='Codigo', required=True)
    fecha = fields.Date(string='Fecha de reparto', default = fields.date.today())

    @api.constrains('fecha')
    def _checkFecha(self):
    	hoy = date.today()
    	for proyecto in self:
    		repartos.fecha
    		dias = relativedelta(hoy, repartos.fecha).days
    		if(dias > 0):
    			raise exceptions.ValidationError("Error, la fecha del reparto no puede ser anterior a la fecha actual")
    
    #Relacion entre tablas
    proveedor_id = fields.Many2one('proveedores.proveedores', string='Proveedor')
    producto_rep = fields.One2many('almacenes.productos','reparto_pro', string='Productos')
    almacen_rep = fields.Many2one('almacenes.almacenes', string='Almacenes')