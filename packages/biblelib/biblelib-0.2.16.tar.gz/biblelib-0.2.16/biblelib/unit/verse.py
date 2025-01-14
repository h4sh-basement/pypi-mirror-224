"""Define Verse class."""

from typing import Any

from biblelib.word import BCVID
from .unit import Unit, Versification


class Verse(Unit):
    """Manage Verse units.

    The scheme for identifying verses is BCV (no word or part index):
    these identifiers are used for comparison.

    A Verse instance has a data attribute for consistency, but it's
    not currently populated.

    A versification attribute indicates how the identifiers should be
    interpreted: only the default of the 'eng' scheme for now, and not
    actually used yet.

    """

    # if defined, the parent instance: e.g. parent_chapter of Mark 4:3 is Mark 4
    # could also be parent sentence, paragraph, pericope ... so dict for extensibility
    parent: dict[str, Any] = {"Chapter": None}

    def __init__(
        self, list: list = None, identifier: BCVID = "", versification: Versification = Versification.ENG
    ) -> None:
        """Instantiate a Verse."""
        super().__init__(list=list, identifier=identifier)
        assert isinstance(identifier, BCVID), f"Identifier must be a BCVID instance: {identifier}"
        assert versification in Versification, f"Invalid versification: {versification}"
        self.versification = versification
