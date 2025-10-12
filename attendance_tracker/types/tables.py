"""Define tuple types representing sqlite tables."""

from abc import abstractmethod
from typing import NamedTuple, override


class Table(NamedTuple):
    """Abstract table class for sqlite tables."""

    def adapt(self) -> str:
        """Convert tuple fields to sqlite3 compatible str."""
        return ";".join(self)

    def convert(self, tuple: str) -> NamedTuple:
        """Convert sqlite row string to table instance."""
        row = tuple.split(";")
        return self.from_list(row)

    @abstractmethod
    @staticmethod
    def from_list(csv_line: list[str]) -> NamedTuple:
        """Parse a list of fields into a tuple instance."""
        raise NotImplementedError


class ClubData(Table):
    """Club data table instance."""

    name: str
    president: str
    email: str
    size: int
    advisor: str
    advisor_email: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> NamedTuple:
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

    room_num: int
    building: str
    times_accessed: int
    access_succeed: int
    access_fail: int
    data_entered: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> NamedTuple:
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

    room_num: int
    building: str
    assigned_club: str

    @override
    @staticmethod
    def from_list(csv_line: list[str]) -> NamedTuple:
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
