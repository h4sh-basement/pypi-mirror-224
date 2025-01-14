# -*- coding: utf-8 -*-
# © 2017 Acsone SA/NV (<https://www.acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.tools.misc import formatLang


class AccountPaymentOrderReport(models.AbstractModel):
    _name = 'report.account_payment_order.print_account_payment_order_main'

    @api.model
    def render_html(self, docids, data=None):
        AccountPaymentOrderObj = self.env['account.payment.order']
        docs = AccountPaymentOrderObj.browse(docids)

        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.payment.order',
            'docs': docs,
            'data': data,
            'env': self.env,
            'get_bank_account_name': self.get_bank_account_name,
            'get_invoice_ref': self.get_invoice_ref,
            'formatLang': formatLang,
        }
        return self.env['report'].render(
            'account_payment_order.print_account_payment_order_main', docargs)

    @api.model
    def get_bank_account_name(self, partner_bank):
        """

        :param partner_bank:
        :return:
        """
        if partner_bank:
            name = ''
            if partner_bank.bank_name:
                name = '%s: ' % partner_bank.bank_id.name
            if partner_bank.acc_number:
                name = '%s %s' % (name, partner_bank.acc_number)
                if partner_bank.bank_bic:
                    name = '%s - ' % (name)
            if partner_bank.bank_bic:
                name = '%s BIC %s' % (name, partner_bank.bank_bic)
            return name
        else:
            return False

    @api.model
    def get_invoice_ref(self, line):
        value = (line.move_line_id.invoice_id.number or
                 line.move_line_id.move_id.name)
        return value or ''
