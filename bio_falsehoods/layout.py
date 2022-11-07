"""Layout elements for bio_falsehoods"""
import json
from dataclasses import dataclass
from typing import Dict, List

import dash_bootstrap_components as dbc
from dash import html


@dataclass(frozen=True)
class Falsehood:
    """A bio-Falsehood"""

    title: str
    text: str
    ref: List[Dict[str, str]]


THEME = dbc.themes.MORPH

PADDING = "py-3"

NAVBAR = dbc.NavbarSimple(
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

    links = [
        dbc.ListGroupItem(each.get("link_title"), href=each.get("link_url"))
        for each in falsey.ref
    ]

    return dbc.Col(
        dbc.Card(
            dbc.CardBody(
                children=[
                    html.H4(f"Myth: {falsey.title}", className="card-title"),
                    html.P(f"Reality: {falsey.text}", className="card-text"),
                    html.H5("Scientific References:"),
                    dbc.ListGroup(
                        children=links,
                    ),
                ]
            )
        ),
        width={"offset": 2, "size": 6},
    )


def read_falsehoods_from_json(json_file: str) -> List[Falsehood]:
    with open(json_file) as jfile:
        out = json.load(jfile)

    falsehoods: List[Falsehood] = [
        Falsehood(title=each.get("title"), text=each.get("text"), ref=each.get("links"))
        for each in out.get("contents")
    ]

    return falsehoods
