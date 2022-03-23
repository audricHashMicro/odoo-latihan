from email.policy import default
from datetime import datetime
from odoo import api, fields, models


class workOrder(models.Model):
    _name = 'booking.workorder'
    _description = 'Work Order Information'

    name = fields.Char(string='Work Order', readonly=True,
                       required=True, copy=False, default='New')
    bo_reference = fields.Many2one(
        comodel_name='booking.saleorder',
        string='Booking Order Reference',
        readonly=True,
        default=lambda self: self.env['booking.saleorder'].search([]))
    team = fields.Many2one(
        comodel_name='booking.serviceteam',
        string='Team Name',
        required=True)
    team_leader = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader',
        required=True,
        compute='_compute_team_name')
    team_members = fields.Many2many(
        comodel_name='res.users',
        string='Team Members',
        compute='_compute_team_name')
    planned_start = fields.Datetime('Planned Start', required=True)
    planned_end = fields.Datetime('Planned End', required=True)
    date_start = fields.Datetime('Date Start', readonly=True)
    date_end = fields.Datetime('Date End', readonly=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='State', default="pending")
    notes = fields.Text('Notes', trim=False)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'booking.workorder.sequence') or 'New'
        result = super(workOrder, self).create(vals)
        return result

    @api.depends('team')
    def _compute_team_name(self):
        for record in self:
            record.team_leader = record.team.team_leader
            record.team_members = record.team.team_members

    def action_start(self):
        self.state = 'progress'
        self.date_start = datetime.now()

    def action_end(self):
        self.state = 'done'
        self.date_end = datetime.now()

    def action_reset(self):
        self.state = 'pending'
        self.date_start = None

    def action_cancel(self):
        self.state = 'cancel'

# as
