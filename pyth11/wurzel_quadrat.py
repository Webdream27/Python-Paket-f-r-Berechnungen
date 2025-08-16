"""
Modul: wurzel_quadrat

Dieses Modul stellt zwei grundlegende mathematische Funktionen
zur Verfügung, die auf dem Standardmodul 'math' basieren.
"""
import math

def quadrat(zahl):
    """
    Berechnet das Quadrat der übergebenen Zahl.

    Args:
        zahl (int oder float): Die Zahl, die quadriert werden soll.

    Returns:
        Das Quadrat der Zahl (zahl * zahl).
    """
    return zahl * zahl

def wurzel(zahl):
    """
    Berechnet die Quadratwurzel einer übergebenen Zahl.
    Nutzt die Funktion sqrt() aus dem Modul 'math'.

    Args:
        zahl (int oder float): Die Zahl, aus der die Wurzel gezogen wird.

    Returns:
        Die Quadratwurzel der Zahl als float.
    """
    return math.sqrt(zahl)

