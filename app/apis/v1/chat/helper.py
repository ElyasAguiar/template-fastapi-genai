"""Helper module to replace superscript citation markers with numeric references.

This module is designed to convert Unicode superscript citations (e.g., ¹, ², ³)
commonly used in documents into numbered bracketed references (e.g., [1], [2], [3]).
"""

import re


class CitationReplacer:
    """Replaces Unicode superscript citation digits with numeric bracketed references."""

    def __init__(self):
        """Initialize citation index and mapping dictionary."""
        self.citation_index = 1
        self.superscript_to_index = {}

    def replace(self, match: re.Match) -> str:
        """Replace a superscript match with a numbered reference."""
        superscript_str = match.group(0)
        digit = self._decode_superscript(superscript_str)

        if digit not in self.superscript_to_index:
            self.superscript_to_index[digit] = self.citation_index
            self.citation_index += 1

        return f"[{self.superscript_to_index[digit]}]"

    def _decode_superscript(self, superscript: str) -> str:
        """Convert a superscript string into its numeric string equivalent."""
        superscript_digits = {
            "⁰": "0",
            "¹": "1",
            "²": "2",
            "³": "3",
            "⁴": "4",
            "⁵": "5",
            "⁶": "6",
            "⁷": "7",
            "⁸": "8",
            "⁹": "9",
        }
        return "".join(superscript_digits.get(c, "") for c in superscript)

    def is_superscript(self, text: str) -> bool:
        """Check if the given text contains only superscript digits."""
        return all(c in "⁰¹²³⁴⁵⁶⁷⁸⁹" for c in text.strip())
