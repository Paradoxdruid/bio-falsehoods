"""App to dispel common biology falsehoods."""

from random import choice
from typing import List

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State

from bio_falsehoods.layout import FOOTER, MODAL, NAVBAR, PADDING, THEME, SIZING
from bio_falsehoods.utils import Falsehood, generate_card, read_falsehoods_from_json

# ----------------- Initialize App --------------------------

app = dash.Dash(__name__, external_stylesheets=[THEME])
app.title = "Bio-Falsehoods"
server = app.server

# ---------------- Load Falsehood data ----------------------

falsehoods: List[Falsehood] = read_falsehoods_from_json("./assets/misconceptions.json")

# ----------------- Layout ----------------------------------

app.layout = dbc.Container(
    fluid=True,
    children=dbc.Row(
        dbc.Col(
            children=[
                MODAL,
                NAVBAR,
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
                    ),
                    class_name=PADDING,
                ),
                FOOTER,
            ],
            **SIZING
        ),
        justify="center",
    ),
    style={"min-height": "100vh"},  # fill the whole background
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
