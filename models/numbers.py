"""Aqui coloque las cosas del One2many."""
from odoo import models, fields


class Numbers(models.Model):
    """Clase numbers que es la relacion del one2many."""

    _name = "numbers"
    _description = "Numbers"

    name_numbers = fields.Char("Name", required=True)
    floatt = fields.Float("Float", required=True)
    many_id = fields.Many2one("logic.basic", string="Many ID")
