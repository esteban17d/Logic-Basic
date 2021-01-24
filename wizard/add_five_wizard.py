"""Segunda practica con wizard."""
from odoo import models, fields


class AddFive(models.TransientModel):
    """Clase."""

    _name = "add.five"
    _description = "Add five"

    state_select = fields.Selection([('to_verify', 'To verify'),
                                     ('checked', 'Checked')]
                                    )
    int_add = fields.Integer("Integer")

    def action_add_five(self):
        """Clase para anadir 5 en el final del numero binario."""
        logicbasic = self.env['logic.basic']
        logic_basic_check_ids = logicbasic.search(
            [('state', '=', self.state_select)]
        )
        logic_basic_check_ids.write({'binary_integer_number': self.int_add})
