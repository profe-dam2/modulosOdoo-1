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

class almacen(models.Model):
    _name = 'almacenes.almacen'
    _description = 'Define los atributos'

    #Atributos
    codAlm = fields.Char(string='Codigo', required=True)
    nombreAlm = fields.Char(string='Nombre del almacen', required=True)
    direccionAlm = fields.Char(string='Direccion', required=True)

    #Relacion entre tablas
    productos_codProds = fields.Many2many('almacenes.productos', string='Productos')
    id_almacen = fields.Many2many('proveedores.repartos', string='Repartos')

    def name_get(self):
        listaAlmacenes = []
        for almacen in self:
            listaAlmacenes.append((almacen.codAlm, almacen.nombreAlm))
        return listaAlmacenes


class productos(models.Model):
    _name = 'almacenes.productos'
    _description = 'Define los atributos'

    #Atributos
    codProd = fields.Char(string='Codigo', required=True)
    nombreProd = fields.Char(string='Nombre del producto', required=True)
    tipoProd = fields.Selection(string='Tipo de producto', selection=[('a','fresco'),('b','congelado'),('c','enlatado'),('d','empaquetado')], help='Estado del alimento')
    cantidadProd = fields.Integer(string='Cantidad', required=True)
    descripcionProd = fields.Text(string='Descripcion del producto')
    fechaCad = fields.Date(string='Fecha de caducidad', default = fields.date.today(), required=True)

    @api.constrains('fechaCad')
    def _checkFecha(self):
    	hoy = date.today()
    	for productos in self:
    		productos.fechaCad
    		dias = relativedelta(hoy, productos.fechaCad).days
    		if(dias >= 0):
    			raise exceptions.ValidationError("Error, la fecha de caducidad no puede ser igual o anterior a la fecha actual")

    @api.constrains('cantidadProd')
    def _checkCantidad(self):
        for productos in self:
            if(productos.cantidadProd < 1):
                raise exceptions.ValidationError("La cantidad no puede ser menor inferior a 1")
    
    #Relacion entre tablas
    almacenes_codAlms = fields.Many2many('almacenes.almacen', string='Almacenes')
    reparto_producto = fields.Many2many('proveedores.repartos', string='Repartos')

    def name_get(self):
        listaRepartos = []
        for productos in self:
            listaRepartos.append((productos.codProd, productos.nombreProd))
        return listaRepartos