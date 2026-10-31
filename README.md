# NP – Nikolina Milić

Projekat za vježbu iz predmeta **Napredno programiranje**. Sadrži funkciju
`prosjecna_cijena`, automatske testove napisane pomoću biblioteke `pytest` i
provjeru kvaliteta koda pomoću alata `ruff`.

## Pokretanje projekta

Potreban je Python 3.12 ili noviji.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Pokretanje testova:

```powershell
python -m pytest
```

Provjera koda:

```powershell
python -m ruff check .
```

## Korišćeni upit

> Generiši mi Python kod za funkciju `prosjecna_cijena(cijene)` koja računa
> prosječnu vrijednost proslijeđenih cijena. Dodaj provjeru za praznu listu i
> napiši testove pomoću biblioteke pytest.

## Uočeni nedostaci generisanog koda

Prva verzija AI-generisanog koda zahtijevala je kritički pregled. Uočeni su
sljedeći nedostaci:

- promjenjivi podrazumijevani argument, na primjer `rezultat=[]`, zadržava isto
  stanje između više poziva funkcije;
- dijeljenje sa nulom nije bilo spriječeno kada je proslijeđena prazna lista;
- funkcija je vraćala listu rezultata umjesto jedne prosječne vrijednosti;
- nijesu postojali testovi za decimalne vrijednosti, jednu vrijednost i praznu
  listu.

U završnoj verziji funkcija nema promjenjivi podrazumijevani argument, za praznu
listu podiže jasan `ValueError`, a očekivano ponašanje je pokriveno testovima.
