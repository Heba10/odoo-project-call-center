# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime

class Calls(models.Model):
    _name = 'first.adoon.calls'
    _description = 'CRD'

    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    source = fields.Char()
    destination = fields.Char()
    duration = fields.Float(compute='_compute_duration',store=True)
    name = fields.Char(default='New')

    station=fields.Many2one(comodel_name='first_adoon.station')
    tags=fields.Many2many(comodel_name='first_adoon.station')

    state=fields.Selection([
        ('draft','Draft'),
        ('invoiced', 'Invoiced'),
    ], default="draft", string="Status")

    @api.constrains('stop_time')
    def check_stop_time(self):
        for rec in self:
            if rec.stop_time < rec.start_time:
                raise ValidationError('Stop time should be bigger than start time!')
    
    @api.depends('start_time', 'stop_time')
    def _compute_duration(self):
        for rec in self:
            rec.duration=0.0
            if rec.stop_time and rec.start_time:
                rec.duration = (rec.stop_time - rec.start_time).seconds / 60

class station(models.Model):
    _name='first_adoon.station'
    name=fields.Char()
    calls=fields.One2many(comodel_name='first.adoon.calls', inverse_name='station')

class tags(models.Model):
    _name='first_adoon.tags'
    name=fields.Char()