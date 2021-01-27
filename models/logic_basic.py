"""Archivo principal."""
from odoo import models, fields, api
import heapq


class LogicBasic(models.Model):
    """Clase encargada del trabajo principal."""

    _name = "logic.basic"
    _description = "Awesome model"

    name = fields.Char("Name", required=True)
    binary_integer_number = fields.Integer("Insert number binary")
    number_of_bits = fields.Integer("Amount of ones",
                                    compute="_amount_of_ones"
                                    )
    number_to_reverse = fields.Integer("Insert any number:")
    number_reverse = fields.Integer("Reverse number",
                                    compute="_reverse_number"
                                    )
    numbers_ids = fields.One2many("numbers",
                                  'many_id',
                                  string="Numbers",
                                  required=True
                                  )
    amount_l_numbers = fields.Integer("How many large numbers want to show?")
    amount_s_numbers = fields.Integer("How many small numbers want to show?")
    largest_numbers = fields.Char("Largest numbers",
                                  compute="_amount_largest_numbers"
                                  )
    smallest_numbers = fields.Char("Smallest numbers",
                                   compute="_amount_smallest_numbers"
                                   )
    mathematic_operation = fields.Char("Insert here your operation:",
                                       default="1 + 1"
                                       )
    result_operation = fields.Float("Result", compute="_result_mathematic")
    insert_sentence = fields.Char("Insert here your sentence:", default="Hola")
    insert_letter = fields.Char("Insert your letter:", default="a")
    t_letter = fields.Integer("Amount of times that is repeated:",
                              compute="_total_letter"
                              )
    show_amount_ones = fields.Boolean("Show amount of ones", default=False)

    favorite = fields.Selection(
        [('0', 'Normal'), ('1', 'Favorite')], default='0'
    )

    state = fields.Selection(
        [('to_verify', 'To verify'), ('checked', 'Checked')],
        default='to_verify'
    )

    @api.depends("binary_integer_number")
    def _amount_of_ones(self):
        for record in self:
            string_binary = str(record.binary_integer_number)
            record.number_of_bits = string_binary.count("1")

    @api.depends("amount_l_numbers")
    def _amount_largest_numbers(self):
        for record in self:
            record.largest_numbers = heapq.nlargest(record.amount_l_numbers,
                                                    record.numbers_ids.mapped(
                                                        "floatt"
                                                    )
                                                    )

    @api.depends("amount_s_numbers")
    def _amount_smallest_numbers(self):
        for record in self:
            record.smallest_numbers = heapq.nsmallest(record.amount_s_numbers,
                                                      record.numbers_ids.mapped
                                                      (
                                                          "floatt"
                                                      )
                                                      )

    @api.depends("mathematic_operation")
    def _result_mathematic(self):
        for record in self:
            if not isinstance(record.mathematic_operation, bool):
                record.mathematic_operation = record.mathematic_operation\
                    .replace(
                        " ", ""
                    )
                if record.mathematic_operation != "":
                    record.result_operation = eval(record.mathematic_operation)
                else:
                    record.result_operation = ""
            else:
                record.result_operation = ""

    @api.depends("insert_letter")
    def _total_letter(self):
        for record in self:
            if not isinstance(record.insert_sentence, bool) and\
                    not isinstance(record.insert_letter, bool):
                record.t_letter = record.insert_sentence.count(
                    record.insert_letter
                )
            else:
                record.t_letter = ""

    @api.depends("number_to_reverse")
    def _reverse_number(self):
        for record in self:
            record.number_reverse = int(str(record.number_to_reverse)[::-1])

    def action_check(self):
        """Metodo para cambiar el state a checked."""
        self.write({'state': 'checked'})

    def action_back_to_edit(self):
        """Metodo para cambiar el state a to verify."""
        self.write({'state': 'to_verify'})
