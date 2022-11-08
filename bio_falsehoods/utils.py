"""Utility functions for bio-falsehoods"""

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
        Falsehood(title=each.get("title"), text=each.get("text"), ref=each.get("links"))
        for each in out.get("contents")
    ]

    return falsehoods
