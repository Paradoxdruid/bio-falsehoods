"""Utility functions for bio-falsehoods"""

import json
from dataclasses import dataclass
from typing import List

import dash_bootstrap_components as dbc
from dash import html


@dataclass(frozen=True)
class Falsehood_Link:
    """A reference link for a Falsehood"""

    title: str
    url: str


@dataclass(frozen=True)
class Falsehood:
    """A bio-Falsehood"""

    title: str
    text: str
    ref: List[Falsehood_Link]


def generate_card(falsey: Falsehood) -> dbc.Col:
    """Generate a bootstrap card for a Falsehood.

    Args:
        falsey (Falsehood): a bio Falsehood

    Returns:
        dbc.Col: column contaning a styled bootstrap card
    """

    links = [dbc.ListGroupItem(each.title, href=each.url) for each in falsey.ref]

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
    )


def read_falsehoods_from_json(json_file: str) -> List[Falsehood]:
    """Read a json file to generate a list of Falsehoods

    Args:
        json_file (str): json filename

    Returns:
        List[Falsehood]: list of Falsehoods
    """
    with open(json_file) as jfile:
        out = json.load(jfile)

    falsehoods: List[Falsehood] = [
        Falsehood(
            title=each.get("title"),
            text=each.get("text"),
            ref=[
                Falsehood_Link(title=sub.get("link_title"), url=sub.get("link_url"))
                for sub in each.get("links")
            ],
        )
        for each in out.get("contents")
    ]

    return falsehoods
