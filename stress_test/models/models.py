# -*- coding: utf-8 -*-

from odoo import models, fields, api
# import time
from datetime import datetime

# class stress_test(models.Model):
#     _name = 'stress_test.stress_test'
#     _description = 'stress_test.stress_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class StressTest(models.Model):
    _name = 'stress_test.stress_test'
    _description = 'stress_test.stress_test'
    _rec = "Stress Test"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    test_one = fields.Boolean(default=False, string="Test 1")
    test_two = fields.Boolean(default=False, string="Test 2")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def stress_test_one(self):
        # sale_order_obj = self.env['sale.order'].search([('state', 'not in', ('draft', 'sent', 'cancel'))], order='id')
        # invoice_obj = self.env['account.move']
        #
        # start_time = time.time()
        # order_list_name = []
        #
        # for order in sale_order_obj:
        #     order_list_name.append(order.name)
        #
        # invoice_recs = invoice_obj.search([('invoice_payment_ref', 'in', order_list_name)])
        #
        # end_time = time.time()
        # print("---Total time to execute %s seconds ---" % round(end_time - start_time, 30))

        start_time = datetime.now()

        order_list_name = []

        sale_order = self.env['sale.order'].search([('state', '=', 'sale')])
        for order in sale_order:
            order_list_name.append(order.name)

        account_pay_rec = self.env['account.move'].search([('invoice_origin', 'in', order_list_name)])

        print("--- 1st code %s  seconds ---" % (datetime.now() - start_time))

    def stress_test_two(self):
        # 2nd Method
        start_time2 = datetime.now()

        sale_order2 = self.env['sale.order'].search([('state', '=', 'sale')])
        for order in sale_order2:
            account_pay_rec2 = self.env['account.move'].search([('invoice_origin', '=', order.name)])

        print("--- 2nd code   %s   seconds ---" % (datetime.now() - start_time2))

    def run_both_tests_in_order(self):
        self.stress_test_one()
        self.stress_test_two()

    def run_both_tests_reverse_order(self):
        self.stress_test_two()
        self.stress_test_one()
