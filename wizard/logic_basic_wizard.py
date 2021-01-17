"""Archivo py para wizard."""
from odoo import fields, models, api


class MathWizard(models.TransientModel):
    """Clase para practicar wizards."""

    _name = "math.wizard"
    _description = "Ventana emergente"

    num_1 = fields.Float("Number º1")
    num_2 = fields.Float("Number º2")
    spot_result = fields.Float("Result", compute="_sum_two_numbers")

    @api.depends("num_2")
    def _sum_two_numbers(self):
        for record in self:
            record.spot_result = record.num_1 + record.num_2
