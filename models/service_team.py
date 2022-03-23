from odoo import api, fields, models


class serviceTeam(models.Model):
    _name = 'booking.serviceteam'
    _description = 'Service Team Information'

    name = fields.Char(
        string='Team Name',
        required=True)
    team_leader = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader',
        required=True)
    team_members = fields.Many2many(
        comodel_name='res.users',
        string='Team Members')
