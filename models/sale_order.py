from odoo import api, fields, models


class saleOrder(models.Model):
    _name = 'booking.saleorder'
    _description = 'Sale Order'

    name = fields.Char(string='Name')
    is_booking_order = fields.Boolean(
        string='Is Booking Order',
        default=True)
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
        required=True,
        compute='_compute_team_name')
    booking_start = fields.Datetime('Booking Start', required=True)
    booking_end = fields.Datetime('Booking End', required=True)

    @api.depends('team')
    def _compute_team_name(self):
        for record in self:
            record.team_leader = record.team.team_leader
            record.team_members = record.team.team_members

    # info = fields.Selection([
    #     ('over', 'Team already has work order during that period on'),
    #     ('available', 'Team is available for booking.')
    # ], string='Info')

    # leader_id = fields.Many2one(
    #     comodel_name='booking.workorder', string='Leader')

    # @api.model
    # def check(self, vals):
    #     record = super(saleOrder, self).create(vals)
    #     lead = self.env['booking.workorder'].search(
    #         [('team_leader', '=', record.leader_id.team_leader)])
    #     member = self.env['booking.workorder'].search(
    #         [('team_members', '=', record.leader_id.team_members)])
    #     start = self.env['booking.workorder'].search(
    #         [('team_leader', '=', record.leader_id.planned_start)])
    #     end = self.env['booking.workorder'].search(
    #         [('team_members', '=', record.leader_id.planned_end)])

    #     if lead != None & member != None:
    #         if start < self.booking_start > end:
    #             info =
    def check(self, vals):
        pass
