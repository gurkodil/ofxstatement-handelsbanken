import os

from ofxstatement.ui import UI
from datetime import date

from ofxstatement_handelsbanken.plugin import HandelsbankenPlugin


def test_handelsbanken() -> None:
    plugin = HandelsbankenPlugin(UI(), {})
    here = os.path.dirname(__file__)
    sample_filename = os.path.join(here, "transactions.xlsx")

    parser = plugin.get_parser(sample_filename)
    statement = parser.parse()

    assert statement is not None
    assert statement.account_id == "123 123 123"
    assert statement.currency == "SEK"
    assert statement.bank_id == "HANDELSBANKEN"

    assert len(statement.lines) == 2
    stmt_line1, stmt_line2 = statement.lines

    assert stmt_line1.memo == "blipp"
    assert stmt_line1.amount == -238
    assert stmt_line1.date == date(2025, 1, 2)

    assert stmt_line2.memo == "blupp"
    assert stmt_line2.amount == -228
    assert stmt_line2.date == date(2025, 1, 2)
