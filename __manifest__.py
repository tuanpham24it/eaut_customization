{
    "name": "EAUT Customization",
    "version": "1.0",
    "category": "Customization",
    "summary": "Customizations for EAUT",
    "description": """
        Module để tùy chỉnh các tính năng của EAUT, bao gồm:
        - fields
        - models
        - reports
        - ...
    """,
    "author": "tuanpham24",
        "depends": [
        "helpdesk",
        "portal",
        "website",
    ],
    "data": [
        "views/helpdesk_portal_templates.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}