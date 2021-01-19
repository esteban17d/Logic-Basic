"""Archivo py para wizard."""
from odoo import fields, models, api


class MathWizard(models.TransientModel):
    """Clase para practicar wizards."""

    _name = "math.wizard"
    _description = "Ventana emergente"

    state_wizard_logic = fields.Selection([('to_verify', 'To verify'),
                                           ('checked', 'Checked')]
                                          )
    spot_result = fields.Integer("Result", compute="_sum_binary")

    @api.depends("state_wizard_logic")
    def _sum_binary(self):
        logicbasic = self.env["logic.basic"]
        logic_basic_check_ids = logicbasic.search([('state',
                                                    '=',
                                                    self.state_wizard_logic
                                                    )])
        self.spot_result = sum(
            logic_basic_check_ids.mapped("binary_integer_number")
        )
