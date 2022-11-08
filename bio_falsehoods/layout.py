"""Layout elements for bio_falsehoods"""

import dash_bootstrap_components as dbc
from dash import html

THEME = dbc.themes.MORPH

SIZING = {"xs": {"size": 12}, "sm": {"size": 10}, "md": {"size": 8}, "lg": {"size": 6}}

PADDING = "py-3"

NAVBAR = dbc.Row(
    dbc.Col(
        dbc.NavbarSimple(
            children=[
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("More", header=True),
                        dbc.DropdownMenuItem("About", id="dropdown-button", n_clicks=0),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="More",
                ),
            ],
            brand="Bio-Falsehoods",
            brand_href="#",
            color="primary",
            dark=True,
            class_name="pb-3 rounded",
        )
    ),
    class_name="pt-3",
)

FOOTER = dbc.Row(
    dbc.Col(
        dbc.CardFooter(
            dbc.Row(
                children=[
                    dbc.Col(
                        html.P(
                            children=[
                                "Visit ",
                                html.A(
                                    "Bonham Lab",
                                    href="http://www.bonhamlab.com",
                                    className="card-text",
                                ),
                            ],
                            className="card-text",
                        ),
                    ),
                    dbc.Col(
                        html.P(
                            children=[
                                "Designed by ",
                                html.A(
                                    "Dr. Andrew J. Bonham",
                                    href="https://github.com/Paradoxdruid",
                                    className="card-text",
                                ),
                            ],
                            className="card-text text-right",
                        ),
                    ),
                ],
                justify="between",
            )
        )
    ),
    class_name=PADDING,
)

MODAL = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("About")),
                dbc.ModalBody(
                    (
                        "A list of common misconceptions and falsehoods about biology, "
                        "compiled by Dr. Andrew J. Bonham"
                    )
                ),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-button", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)
