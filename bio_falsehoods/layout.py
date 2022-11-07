"""Layout elements for bio_falsehoods"""
from dataclasses import dataclass

import dash_bootstrap_components as dbc
from dash import html


@dataclass(frozen=True, slots=True)
class Falsehood:
    """A bio-Falsehood"""

    title: str
    text: str
    ref: str


THEME = dbc.themes.MORPH

PADDING = "py-3"

NAVBAR = dbc.NavbarSimple(
    children=[
        # # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More", header=True),
                dbc.DropdownMenuItem("About", id="dropdown-button", n_clicks=0),
                # dbc.DropdownMenuItem("Action 2", href="#"),
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

FOOTER = dbc.Row(
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


def generate_card(falsey: Falsehood) -> dbc.Col:
    """Generate a bootstrap card for a Falsehood.

    Args:
        falsey (Falsehood): a bio Falsehood

    Returns:
        dbc.Col: column contaning a styled bootstrap card
    """

    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                children=[
                    html.H4(falsey.title, className="card-title"),
                    html.P(falsey.text, className="card-text"),
                    dbc.CardLink("Scientific Reference", href=falsey.ref),
                ]
            )
        ),
        width={"offset": 2, "size": 6},
    )
