# payment_wizard_user/models/payment_wizard.py
from odoo import models, fields, api


class PaymentWizard(models.TransientModel):
    _inherit = 'account.payment.register'

    invoice_user_id = fields.Many2one(
        'res.users',
        string='Invoice User',
        readonly=False,
        default=lambda self: self.env.user)

    @api.model
    def _create_payments(self):
        res = super(PaymentWizard, self)._create_payments()
        for wizard in self:
            for payment in res:
                if wizard.invoice_user_id:
                    payment.write({
                        'invoice_user_id': wizard.invoice_user_id.id
                    })
        return res
