"""
Ein Skript zum Testen der Funktionen aus dem Paket 'pyth11'.
"""
# Importiert die Funktionen gezielt aus dem Modul innerhalb des Pakets.
from pyth11.wurzel_quadrat import quadrat, wurzel

# Ein fester Wert für die Berechnungen.
fester_wert = 64

# Die Funktionen aufrufen.
ergebnis_quadrat = quadrat(fester_wert)
ergebnis_wurzel = wurzel(fester_wert)

# Das Ergebnis ausgeben.
print(f"Der verwendete Wert ist: {fester_wert}")
print(f"Das Quadrat von {fester_wert} ist: {ergebnis_quadrat}")
print(f"Die Wurzel von {fester_wert} ist: {ergebnis_wurzel}")

