# Copyright (C) 2022 Abdulrahman Elsadany
# Copyright (C) 2022 Abdulrahman Elsadany
{
    "name": "Theme Rebranding",
    "version": "14.0.1.1.2",
    "author": "Abdulrhman Mohamed Hafeza",
    "category": "Themes/Backend",
    "summary": """ change odoo logo from pos product screen into logo of company
    change shape of basic theme as whole and colors branding odoo standard
    responsive with odoo enterprise
    """,
    "description""""
    change odoo logo from pos product screen into logo of company
    change shape of basic theme as whole and colors branding odoo standard
    """
    "price": '10.0',
    "Currency": "USD",
    "maintainer": "Abdulrhman Mohamed Hafeza",
    "website": "https://github.com/Abdul-rahmanMohamed",
    "depends": ["mail", "hr_holidays", 'web_enterprise', 'point_of_sale'],
    "data": ['views/hide_conversation_from_nav_bar.xml'],
    "demo": [],
    "qweb": ["static/src/xml/point_of_sale_logo.xml"],
    "images": ["static/src/xml/icon.png",
               "static/description/background2.gif"
              ],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
