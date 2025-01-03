import re
import logging

from ofxstatement.plugin import Plugin
from ofxstatement.statement import Statement
from .parser import ExcelStatementParser


class HandelsbankenParser(ExcelStatementParser):
    """Parser for converting Handelsbanken bank statements from Excel to OFX format."""

    expected_headers = {
        "B9": "Transaktionsdatum",
        "C9": "Text",
        "D9": "Belopp",
    }

    mappings = {"date": 1, "memo": 2, "amount": 3}

    ACCOUNT_PATTERN = re.compile(r"^(\w+) (\d{3} \d{3} \d{3})$")
    HEADER_ROW_INDEX = 9

    def __init__(self, filename: str) -> None:
        super().__init__(filename=filename)

    def _parse_account_info(self) -> tuple[str, str]:  # Account-specific parsing
        account_cell = self.get_cell_value("A4")
        match = self.ACCOUNT_PATTERN.match(account_cell)
        if not match:
            raise ValueError(f"Invalid account format: {account_cell}")
        return match.group(1), match.group(2)

    def _validate_headers(self) -> None:
        for cell, expected in self.expected_headers.items():
            value = self.get_cell_value(cell)
            if value != expected:
                raise ValueError(
                    f"Unexpected column header. Expected: {expected}, "
                    f"Found: {value}"
                )

    def parse(self) -> Statement:
        account_name, account_id = self._parse_account_info()
        self.statement.account_id = account_id
        self.statement.currency = "SEK"
        self.statement.bank_id = "HANDELSBANKEN"

        logging.info(f"Parsing statement for account: {account_name} ({account_id})")

        self._validate_headers()

        return super().parse()


class HandelsbankenPlugin(Plugin):
    """Plugin for handling Handelsbanken bank statements."""

    def get_parser(self, filename: str) -> HandelsbankenParser:
        return HandelsbankenParser(filename)
