"""Testovi za funkciju ``prosjecna_cijena``."""

import pytest

from prosjecna_cijena import prosjecna_cijena


def test_prosjecna_cijena_vise_vrijednosti() -> None:
    assert prosjecna_cijena([10, 20, 30]) == pytest.approx(20)


def test_prosjecna_cijena_decimalne_vrijednosti() -> None:
    assert prosjecna_cijena([1.99, 2.49, 3.99]) == pytest.approx(2.8233333333)


def test_prosjecna_cijena_jedna_vrijednost() -> None:
    assert prosjecna_cijena([7.5]) == pytest.approx(7.5)


def test_prosjecna_cijena_prazna_lista() -> None:
    with pytest.raises(ValueError, match="ne smije biti prazna"):
        prosjecna_cijena([])
