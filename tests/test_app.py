"""Pytest tests for bio_falsehoods app"""

import re

from bio_falsehoods.app import toggle_modal, update_link


def test_update_link_callback() -> None:
    output = update_link(1, "Bio-Falsehoods: 1")
    assert re.match(r"/\d+", output)


def test_toggle_modal_callback() -> None:

    output_open = toggle_modal(1, None, True)
    assert output_open is False

    output_closed = toggle_modal(1, None, False)
    assert output_closed is True
