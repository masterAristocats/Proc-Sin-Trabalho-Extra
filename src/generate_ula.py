import numpy as np

_AXES = {"x": 0, "y": 1, "z": 2}


def _validate_positive_int(name: str, value: int) -> int:
    """Valida se o parâmetro é um inteiro positivo."""
    value = int(value)

    if value <= 0:
        raise ValueError(f"{name} deve ser um inteiro positivo.")

    return value


def _validate_positive_float(name: str, value: float) -> float:
    """Valida se o parâmetro é um número positivo."""
    value = float(value)

    if value <= 0:
        raise ValueError(f"{name} deve ser maior que zero.")

    return value


def generate_ula(
    M: int,
    d: float,
    axis: str = "x",
    center: bool = False,
) -> np.ndarray:
    """
    Gera as coordenadas tridimensionais de um Uniform Linear Array (ULA).

    Parâmetros
    ----------
    M : int
        Número de sensores.

    d : float
        Espaçamento entre sensores.

    axis : {"x", "y", "z"}, opcional
        Eixo ao longo do qual os sensores serão distribuídos.
        Padrão: "x".

    center : bool, opcional
        Se True, centraliza o arranjo na origem.
        Se False, o primeiro sensor fica na origem.
        Padrão: False.

    Retorna
    -------
    numpy.ndarray
        Matriz de dimensão (M, 3) contendo as coordenadas
        (x, y, z) dos sensores.
    """

    M = _validate_positive_int("M", M)
    d = _validate_positive_float("d", d)

    if axis not in _AXES:
        raise ValueError("axis deve ser 'x', 'y' ou 'z'.")

    offsets = np.arange(M, dtype=float) * d

    if center:
        offsets -= 0.5 * (M - 1) * d

    positions = np.zeros((M, 3), dtype=float)
    positions[:, _AXES[axis]] = offsets

    return positions


if __name__ == "__main__":

    M = 8
    d = 0.5

    positions = generate_ula(
        M=M,
        d=d,
        axis="x",
        center=False,
    )

    print("Posições dos sensores:")
    print(positions)
