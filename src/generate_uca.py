import numpy as np


def _validate_positive_int(name: str, value: int) -> int:
    """
    Valida se o parâmetro é um inteiro positivo.
    """
    value = int(value)

    if value <= 0:
        raise ValueError(f"{name} deve ser um inteiro positivo.")

    return value


def _validate_positive_float(name: str, value: float) -> float:
    """
    Valida se o parâmetro é um número positivo.
    """
    value = float(value)

    if value <= 0:
        raise ValueError(f"{name} deve ser maior que zero.")

    return value


def generate_uca(M: int, R: float) -> np.ndarray:
    """
    Gera as coordenadas tridimensionais de um Uniform Circular Array (UCA).

    Parâmetros
    ----------
    M : int
        Número de sensores.

    R : float
        Raio do círculo.

    Retorna
    -------
    numpy.ndarray
        Matriz de dimensão (M, 3) contendo as coordenadas (x, y, z)
        dos sensores.
    """

    M = _validate_positive_int("M", M)
    R = _validate_positive_float("R", R)

    # Ângulos igualmente espaçados
    angles = 2.0 * np.pi * np.arange(M, dtype=float) / M

    # Coordenadas dos sensores
    positions = np.column_stack(
        (
            R * np.cos(angles),
            R * np.sin(angles),
            np.zeros(M, dtype=float),
        )
    )

    return positions


if __name__ == "__main__":

    M = 8
    R = 1.0

    positions = generate_uca(M, R)

    print("Posições dos sensores:")
    print(positions)
