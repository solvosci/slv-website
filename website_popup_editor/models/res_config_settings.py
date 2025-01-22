# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields
from markupsafe import Markup

class ResCompany(models.Model):
    _inherit = "res.company"

    popup_html_code = fields.Text(
            string="Popup HTML Code",
        )
    
    def get_popup_html_code(self):
        self.ensure_one()
        return Markup(self.popup_html_code)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    popup_html_code = fields.Text(
        related='company_id.popup_html_code',
        help="Insert custom HTML code for the popup. This will replace the default popup content.",
        readonly=False
    )
