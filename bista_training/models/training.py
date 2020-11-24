# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

#This is main class of Bista Training Module
class BistaTraining(models.Model):
    _name = 'bista_training.bista_training'
    _description = 'Bista Training'

    name = fields.Char('Name')
    value = fields.Integer('Score')
    date = fields.Date("Date of Exam",required=1)
    trainee_ids = fields.One2many('bista.trainee','training_batch_id',string="Trainee")

class Trainee(models.Model):
    _name = 'bista.trainee'
    _description = 'Trainee Master'


    #def create(self,vals):
    #def write(self, vals):
    #def unlink(self):

    @api.model
    def create(self,vals):
        print("@@@@@@",vals)
        #custom acctions or function
        return super(Trainee,self).create(vals)
    #

    def write(self,vals):
        print("This is from write method",vals)
        return super(Trainee, self).write(vals)

    # def unlink(self):
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            email=_("%s (copy)") % (self.email or ''))

        return super(Trainee, self).copy(default)

    # def unlink(self):
    #     # #Check what value to be checked. if that checke is true
    #     # if true
    #     # else:
    #     #     ee

    def action_employed(self):
        #Actions
        import pdb;
        pdb.set_trace()
        for rec in self:
            rec.state = 'employed'
        return True


    @api.constrains('email_2')
    def _check_email_2_values(self):
        if self.email_2 == 'lithin@gmail.com':
            raise ValidationError(_('You are not allowed to enter this value'))

    name = fields.Char('Name' , required=1)
    email = fields.Char('Email')
    email_2 = fields.Char('Email2')
    trainee_id = fields.Char(string='Trainee ID', default=lambda self: self.env['ir.sequence'].next_by_code('trainee.id'))
    training_batch_id = fields.Many2one('bista_training.bista_training',string="Batch",
                                        help='This field is to fill up Batch details')

    image_1920 = fields.Image(string="Image")
    state = fields.Selection([('new','New'),('employed','Employed'),('rejected','Rejected')],string="State",default='new')

    _sql_constraints = [
        ('email_uniq','unique(email)','Email ID should be unique')
    ]