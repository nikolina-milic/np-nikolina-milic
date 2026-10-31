"""Funkcije za računanje prosječne cijene."""


def prosjecna_cijena(cijene: list[float]) -> float:
    """Vrati aritmetičku sredinu proslijeđenih cijena.

    Args:
        cijene: Neprazna lista brojčanih cijena.

    Raises:
        ValueError: Ako je lista cijena prazna.
    """
    if not cijene:
        raise ValueError("Lista cijena ne smije biti prazna.")

    return sum(cijene) / len(cijene)
