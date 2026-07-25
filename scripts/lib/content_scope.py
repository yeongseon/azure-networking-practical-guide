from __future__ import annotations

from pathlib import Path
from typing import Union

SCANNED_SECTIONS: frozenset[str] = frozenset(
    {
        "platform",
        "best-practices",
        "operations",
        "troubleshooting",
    }
)

EXCLUDED_SUBPATHS: tuple[str, ...] = (
    "troubleshooting/kql/",
    "troubleshooting/lab-guides/",
)

NAVIGATION_INDEXES: frozenset[str] = frozenset(
    {
        "platform/index.md",
        "best-practices/index.md",
        "operations/index.md",
        "troubleshooting/index.md",
        "troubleshooting/first-10-minutes/index.md",
        "troubleshooting/playbooks/index.md",
    }
)

TAUTOLOGICAL_CLAIM_MARKER: str = "primary source basis"


def is_in_scope(rel_path: Union[Path, str]) -> bool:
    """Return ``True`` when ``rel_path`` requires ``content_validation``.

    ``rel_path`` must be relative to ``docs/``.

    >>> is_in_scope("platform/vnet-and-subnet-basics.md")
    True
    >>> is_in_scope("platform/index.md")
    False
    >>> is_in_scope("tutorials/lab-guides/lab-01-hub-spoke-topology.md")
    False
    >>> is_in_scope("troubleshooting/playbooks/connectivity-failures.md")
    True
    >>> is_in_scope("reference/glossary.md")
    False
    """
    rel = Path(rel_path)
    parts = rel.parts
    if not parts or parts[0] not in SCANNED_SECTIONS:
        return False

    posix = rel.as_posix()
    if any(posix.startswith(prefix) for prefix in EXCLUDED_SUBPATHS):
        return False

    if posix in NAVIGATION_INDEXES:
        return False

    return True


def is_tautological_text(text: object) -> bool:
    """Return ``True`` if ``text`` contains the tautological marker.

    >>> is_tautological_text("uses Microsoft Learn as the primary source basis")
    True
    >>> is_tautological_text("Virtual networks use CIDR ranges")
    False
    """
    if not isinstance(text, str):
        return False
    return TAUTOLOGICAL_CLAIM_MARKER.casefold() in text.casefold()


__all__ = [
    "SCANNED_SECTIONS",
    "EXCLUDED_SUBPATHS",
    "NAVIGATION_INDEXES",
    "TAUTOLOGICAL_CLAIM_MARKER",
    "is_in_scope",
    "is_tautological_text",
]
