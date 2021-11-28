from odoo import models, fields

class RumahsakitPasien(models.Model):
    _name = 'registration.form'
    _description = 'Registration Form'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    address = fields.Text(string='Address', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')