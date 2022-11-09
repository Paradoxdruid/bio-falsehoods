"""Utility functions for bio-falsehoods"""

import json
from dataclasses import dataclass
from typing import Dict, List

import dash_bootstrap_components as dbc
from dash import html

from bio_falsehoods.layout import FOOTER, MODAL, PADDING, SIZING


@dataclass(frozen=True)
class Falsehood_Link:
    """A reference link for a Falsehood"""

    title: str
    url: str


@dataclass(frozen=True)
class Falsehood:
    """A bio-Falsehood"""

    id: int
    title: str
    text: str
    ref: List[Falsehood_Link]


def generate_layout(falsey: Falsehood) -> dbc.Container:
    """Generate a bootstrap layout for a Falsehood.

    Args:
        falsey (Falsehood): a bio Falsehood

    Returns:
        dbc.Container: layout containing a styled bootstrap card
    """

    links = [dbc.ListGroupItem(each.title, href=each.url) for each in falsey.ref]

    navbar = dbc.Row(
        dbc.Col(
            dbc.NavbarSimple(
                id="nav_bar",
                children=[
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("More", header=True),
                            dbc.DropdownMenuItem(
                                "About", id="dropdown-button", n_clicks=0
                            ),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="More",
                    ),
                ],
                brand=f"Bio-Falsehoods # {falsey.id}",
                brand_href="#",
                color="primary",
                dark=True,
                class_name="pb-3 rounded",
            )
        ),
        class_name="pt-3",
    )
    card = dbc.Col(
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
    )

    return dbc.Container(
        fluid=True,
        children=dbc.Row(
            dbc.Col(
                children=[
                    MODAL,
                    navbar,
                    dbc.Row(card),
                    dbc.Row(
                        dbc.Col(
                            dbc.Button(
                                "Show me another",
                                color="primary",
                                id="submit-button",
                                class_name="me-1 btn",
                                n_clicks=0,
                            ),
                        ),
                        class_name=PADDING,
                    ),
                    FOOTER,
                ],
                **SIZING,
            ),
            justify="center",
        ),
        style={"min-height": "100vh"},  # fill the whole background
    )


def read_falsehoods_from_json(json_file: str) -> Dict[int, Falsehood]:
    """Read a json file to generate a list of Falsehoods

    Args:
        json_file (str): json filename

    Returns:
        List[Falsehood]: list of Falsehoods
    """
    with open(json_file) as jfile:
        out = json.load(jfile)

    falsehoods: Dict[int, Falsehood] = {
        int(each.get("id")): Falsehood(
            id=int(each.get("id")),
            title=each.get("title"),
            text=each.get("text"),
            ref=[
                Falsehood_Link(
                    title=sub.get("link_title"),
                    url=sub.get("link_url"),
                )
                for sub in each.get("links")
            ],
        )
        for each in out.get("contents")
    }

    return falsehoods
