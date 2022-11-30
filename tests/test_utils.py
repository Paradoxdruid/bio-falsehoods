"""Pytest tests for bio_falsehoods utils"""

from typing import Dict

import dash_bootstrap_components as dbc
from dash import html
from pytest_mock.plugin import MockerFixture

from bio_falsehoods.layout import FOOTER, MODAL, PADDING, SIZING
from bio_falsehoods.utils import (
    Falsehood,
    Falsehood_Link,
    generate_layout,
    read_falsehoods_from_json,
)


def test_generate_layout() -> None:
    TEST_FALSEHOOD = Falsehood(
        id=1,
        title="Title",
        text="Text",
        ref=[
            Falsehood_Link(title="Link 1", url="https://test1.com"),
            Falsehood_Link(title="Link 2", url="https://test2.com"),
        ],
    )

    EXPECTED = dbc.Container(
        fluid=True,
        children=dbc.Row(
            dbc.Col(
                children=[
                    MODAL,
                    dbc.Row(
                        dbc.Col(
                            dbc.NavbarSimple(
                                id="nav_bar",
                                children=[
                                    dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("More", header=True),
                                            dbc.DropdownMenuItem(
                                                "About",
                                                id="dropdown-button",
                                                n_clicks=0,
                                            ),
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="More",
                                    ),
                                ],
                                brand="Bio-Falsehoods # 1",
                                brand_href="#",
                                color="primary",
                                dark=True,
                                class_name="pb-3 rounded",
                            )
                        ),
                        class_name="pt-3",
                    ),
                    dbc.Row(
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    children=[
                                        html.H4(
                                            "Myth: Title",
                                            className="card-title",
                                        ),
                                        html.P(
                                            "Reality: Text",
                                            className="card-text",
                                        ),
                                        html.H5("Scientific References:"),
                                        dbc.ListGroup(
                                            children=[
                                                dbc.ListGroupItem(
                                                    "Link 1",
                                                    href="https://test1.com",
                                                ),
                                                dbc.ListGroupItem(
                                                    "Link 2",
                                                    href="https://test2.com",
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ),
                        )
                    ),
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

    actual = generate_layout(TEST_FALSEHOOD)

    assert repr(actual) == repr(EXPECTED)


def test_read_falsehoods_from_json(mocker: MockerFixture) -> None:

    TEST_JSON = b"""{
  "title": "bio-falsehoods",
  "contents": [
    {
      "id": 1,
      "title": "Title 1",
      "text": "Text 1",
      "links": [
        {
          "link_title": "Title 1 Link 1",
          "link_url": "https://test1.com/link1"
        },
        {
          "link_title": "Title 1 Link 2",
          "link_url": "https://test1.com/link2"
        }
      ]
    },
    {
      "id": 2,
      "title": "Title 2",
      "text": "Text 2",
      "links": [
        {
          "link_title": "Title 2 Link 1",
          "link_url": "https://test2.com/link1"
        },
        {
          "link_title": "Title 2 Link 2",
          "link_url": "https://test2.com/link2"
        }
      ]
    }
      ]
    }
    """
    mocked_open = mocker.mock_open(read_data=TEST_JSON)
    mocker.patch("bio_falsehoods.utils.open", mocked_open)

    EXPECTED: Dict[int, Falsehood] = {
        1: Falsehood(
            id=1,
            title="Title 1",
            text="Text 1",
            ref=[
                Falsehood_Link(title="Title 1 Link 1", url="https://test1.com/link1"),
                Falsehood_Link(title="Title 1 Link 2", url="https://test1.com/link2"),
            ],
        ),
        2: Falsehood(
            id=2,
            title="Title 2",
            text="Text 2",
            ref=[
                Falsehood_Link(title="Title 2 Link 1", url="https://test2.com/link1"),
                Falsehood_Link(title="Title 2 Link 2", url="https://test2.com/link2"),
            ],
        ),
    }

    actual = read_falsehoods_from_json("test.json")

    assert actual == EXPECTED
