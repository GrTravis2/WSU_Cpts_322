"""Define tuple types representing sqlite tables."""

from abc import abstractmethod
from typing import ClassVar, NamedTuple, override


class Table(NamedTuple):
    """Abstract table class for sqlite tables."""

    TABLE_NAME = ClassVar[str]

    def adapt(self) -> str:
        """Convert tuple fields to sqlite3 compatible str."""
        return ";".join(self)

    def convert(self, tuple: str) -> NamedTuple:
        """Convert sqlite row string to table instance."""
        row = tuple.split(";")
        return self.from_list(row)

    @property
    def insert_format(self) -> str:
        """Create insert string to be used with sqlite db."""
        cols = ", ".join(self._fields)
        vals = "? " * len(self)
        return f"INSERT INTO {self.TABLE_NAME} ({cols}) VALUES ({vals})"

    @abstractmethod
    @staticmethod
    def from_list(csv_line: list[str]) -> NamedTuple:
        """Parse a list of fields into a tuple instance."""
        raise NotImplementedError


class ClubData(Table):
    """Club data table instance."""

    TABLE_NAME = "CLUB_DATA"

    club_name: str
    club_president: str
    email: str
    club_size: int
    club_advisor: str
    club_advisor_email: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> Table:
        match csv_line:
            case [n, p, e, s, a, a_e]:
                return ClubData(
                    n,  # type: ignore
                    p,
                    e,
                    int(s),
                    a,
                    a_e,
                )
            case _:
                msg = f"unrecognized input str {csv_line}"
                raise ValueError(msg)


class InputData(Table):
    """Raw CSV input data straight from the source."""

    TABLE_NAME = "INPUT_DATA"

    building: str
    room_num: int
    times_accessed: int
    access_succeed: int
    access_fail: int
    data_entered: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> Table:
        match csv_line:
            case [r, b, t, s, f, d]:
                return InputData(
                    int(r),  # type: ignore
                    b,
                    int(t),
                    int(s),
                    int(f),
                    d,
                )
            case _:
                msg = f"unrecognized input str {csv_line}"
                raise ValueError(msg)


class RoomLog(Table):
    """Room to club relation table."""

    TABLE_NAME = "ROOM_LOG"

    building: str
    room_num: int
    assigned_club: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> Table:
        match csv_line:
            case [r, b, c]:
                return RoomLog(
                    int(r),  # type: ignore
                    b,
                    c,
                )
            case _:
                msg = f"unrecognized input str {csv_line}"
                raise ValueError(msg)
