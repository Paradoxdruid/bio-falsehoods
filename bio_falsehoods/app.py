"""App to dispel common biology falsehoods."""

from random import choice
from typing import Dict, List

import dash
from dash import Input, Output, State, dcc
from dash_bootstrap_components import Container

from bio_falsehoods.layout import THEME
from bio_falsehoods.utils import Falsehood, generate_layout, read_falsehoods_from_json

# ----------------- Initialize App --------------------------

app = dash.Dash(__name__, external_stylesheets=[THEME], use_pages=True, pages_folder="")
app.title = "Bio-Falsehoods"
server = app.server

# ---------------- Load Falsehood data ----------------------

falsehoods: Dict[int, Falsehood] = read_falsehoods_from_json(
    "./assets/misconceptions.json"
)

layout_dict: Dict[int, Container] = {
    k: generate_layout(v) for k, v in falsehoods.items()
}

# ----------------- Page Registry ---------------------------

for k, v in layout_dict.items():
    dash.register_page(f"Bio-Falsehoods: {k}", path=f"/{k}", layout=v)

paths: List[str] = [page["relative_path"] for page in dash.page_registry.values()]

dash.register_page(
    "Bio-Falsehoods",
    path="/",
    layout=dcc.Location(id="page_ref", href=f"{choice(paths)}", refresh=True),
)  # redirect to entry on initial page load
# TODO: Can we avoid the initial refresh?

# ----------------- Layout ----------------------------------

app.layout = dash.page_container

# ------------------ Callbacks ------------------------------


@app.callback(
    Output(component_id="submit-button", component_property="href"),
    [Input("submit-button", "n_clicks"), State("nav_bar", "brand")],
)  # type: ignore[misc]
def update_link(_: int, brand: str) -> str:
    """Update the 'Show me another' link to a valid new url."""

    false_number: str = f"/{brand[17:]}"
    while True:
        my_choice: str = choice(paths)
        if my_choice != false_number:
            break

    return f"{my_choice}"


@app.callback(
    Output("modal", "is_open"),
    [Input("dropdown-button", "n_clicks"), Input("close-button", "n_clicks")],
    [State("modal", "is_open")],
)  # type: ignore[misc]
def toggle_modal(n1: int, n2: int, is_open: bool) -> bool:
    """Toggle the visibility of the 'About' modal."""
    if n1 or n2:
        return not is_open
    return is_open
