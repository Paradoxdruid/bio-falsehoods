"""App to dispell common biology falsehoods."""
from random import choice
from typing import List

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html

from bio_falsehoods.layout import (
    FOOTER,
    PADDING,
    THEME,
    Falsehood,
    generate_card,
    read_falsehoods_from_json,
)

# ----------------- Initialize App --------------------------

app = dash.Dash(__name__, external_stylesheets=[THEME])
app.title = "Bio-Falsehoods"
server = app.server

# ---------------- Load Falsehood data ----------------------

falsehoods: List[Falsehood] = read_falsehoods_from_json("./assets/misconceptions.json")

# ----------------- Layout ----------------------------------

modal = html.Div(
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

navbar = dbc.NavbarSimple(
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

app.layout = dbc.Container(
    fluid=True,
    children=[
        modal,
        dbc.Row(dbc.Col(navbar, width={"offset": 2, "size": 6}), class_name="pt-3"),
        dbc.Row(id="output-div"),
        dbc.Row(
            dbc.Col(
                dbc.Button(
                    "Show me another",
                    color="primary",
                    id="submit-button",
                    class_name="me-1 btn",
                    n_clicks=0,
                ),
                width={"offset": 2, "size": 6},
            ),
            class_name=PADDING,
        ),
        dbc.Row(
            dbc.Col(dbc.CardFooter(FOOTER), width={"offset": 2, "size": 6}),
            class_name=PADDING,
        ),
    ],
)

# ------------------ Callbacks -----------------------------------------


@app.callback(
    Output(component_id="output-div", component_property="children"),
    [Input("submit-button", "n_clicks")],
)  # type: ignore[misc]
def generate_cards(_: int) -> dbc.Row:

    falsey = choice(falsehoods)

    return generate_card(falsey)


@app.callback(
    Output("modal", "is_open"),
    [Input("dropdown-button", "n_clicks"), Input("close-button", "n_clicks")],
    [State("modal", "is_open")],
)  # type: ignore[misc]
def toggle_modal(n1: int, n2: int, is_open: bool) -> bool:
    if n1 or n2:
        return not is_open
    return is_open
