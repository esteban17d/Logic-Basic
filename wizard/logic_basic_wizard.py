"""Archivo py para wizard."""
from odoo import fields, models, api


class MathWizard(models.TransientModel):
    """Clase para practicar wizards."""

    _name = "math.wizard"
    _description = "Ventana emergente"
    _inherit = "logic.basic"

    state_wizard_logic = fields.Selection([('to_verify', 'To verify'),
                                           ('checked', 'Checked')]
                                          )
    spot_result = fields.Char("Result", compute="_sum_binary")

    @api.depends("state_wizard_logic")
    def _sum_binary(self):
        logicbasic = self.env["logic.basic"]
        logic_basic_check_ids = logicbasic.search([('state', '=', 'to_verify')])
        logic_basic_verify_ids = logicbasic.search([('state', '=', 'checked')])
        for record in self:
            if record.state_wizard_logic == 'to_verify':
                record.spot_result = sum(logic_basic_verify_ids.mapped("binary_integer_number"))
            else:
                record.spot_result = sum(logic_basic_check_ids.mapped("binary_integer_number"))
