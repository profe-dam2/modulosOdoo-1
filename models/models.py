# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models ,fields, api

class departamento(models.Model):
	_name = 'proyectos.departamento'
	_description = 'Define los atributos de un departamento'

	#atributos
	nombreDpto = fields.Char(string='Nombre departamento', required=True)

	#relacion entre tablas
	empleado_id = fields.One2many('proyectos.empleado','departamento_id', string='Departamento')


class empleado(models.Model):
	_name = 'proyectos.empleado'
	_description = 'Define los atributos de un empleado'

	#atributos
	dniEmpleado = fields.Char(string='DNI', requiered=True)
    nombreEmpleado = fields.Char(string='Nombre', requiered=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', requiered=True, default = fields.date.today())
    direccionEmpleado = fields.Char(string='Direcci�n', requiered=True)
    telefonoEmpleado = fields.Char(string='Telefono', requiered=True)
    edad = fields.Integer('Edad', compute='getEdad')

    @api.depends('fechaNacimiento')
    def getEdad(self):
        for empleado in self:
            empleado.edad = 0

	#relacion entre tablas
	departamento_id = fields.Many2one('proyectos.departamento', string='Empleados')
	proyecto_id = fields.Many2one('proyectos.proyecto', string='Proyectos')


class proyecto(models.Model):
	_name = 'proyectos.proyecto'
	_description = 'Atributos de un proyecto'

	#atributos
	nombreProyecto = fields.Char(string='Nombre proyecto', required=True)
	tipoProyecto = fields.Selection(string='Tipo de proyecto', selection=[('f','Front-End'),('b','Back-End')], help='Tipo de proyecto al que esta destinado')
	ciudadProyecto = fields.Char(string='Ciudad', required=True)
	descripcionProyecto = fields.Text(string='Descripcion del proyecto')
	fechaInicio = fields.Date(string='Fecha de inicio', required=True)
	fechaFin = fields.Date(string='Fecha de fin', required=True)

	#relacion entre tablas
	empleado_id = fields.Many2many('proyectos.empleado', string='Empleados')