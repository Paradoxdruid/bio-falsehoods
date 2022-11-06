"""App to dispell common biology falsehoods."""
from random import choice

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output

from bio_falsehoods.layout import (
    FOOTER,
    NAVBAR,
    PADDING,
    THEME,
    Falsehood,
    generate_card,
)

# ----------------- Initialize App --------------------------

app = dash.Dash(__name__, external_stylesheets=[THEME])
app.title = "Bio-Falsehoods"
server = app.server

# ---------------- Helper Functions --------------------------

falsehoods = [
    Falsehood("test 1", "test text", "test link"),
    Falsehood("test 2", "test text", "test link"),
    Falsehood("test 3", "test text", "test link"),
    Falsehood("test 4", "test text", "test link"),
    Falsehood("test 5", "test text", "test link"),
]

# ----------------- Main layout -----------------------------

app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(dbc.Col(NAVBAR, width={"offset": 2, "size": 6}), class_name="pt-3"),
        dbc.Row(
            dbc.Col(
                dbc.Button(
                    "Show me another",
                    color="primary",
                    id="submit-button",
                    class_name="me-1",
                    n_clicks=0,
                ),
                width={"offset": 2, "size": 6},
            ),
            class_name=PADDING,
        ),
        dbc.Row(id="output-div"),
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
def generate_graphs(_: int) -> dbc.Row:

    falsey = choice(falsehoods)

    return generate_card(falsey)
