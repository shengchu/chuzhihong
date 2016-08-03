# -*- encoding: utf-8 -*-
from openerp.osv import osv
from openerp.report import report_sxw
from openerp import models, fields, api


class action_report_delivery_wrapped(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(action_report_delivery_wrapped, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'rmb_upper': self._rmb_upper,
        })
        self.context = context

    def _rmb_upper(self, value):
        return self.pool['res.currency'].rmb_upper(self.cr, self.uid, value)



class report_delivery(osv.AbstractModel):
    _name = 'report.print_reports.report_delivery_view'
    _inherit = 'report.abstract_report'
    _template = 'print_reports.report_delivery_view'
    _wrapped_report_class = action_report_delivery_wrapped
