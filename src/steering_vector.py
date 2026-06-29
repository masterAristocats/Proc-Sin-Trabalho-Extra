import numpy as np


def steering_vector(positions, azimuth, elevation, wavelength):
    """
    Calcula o steering vector de um arranjo de sensores.

    Parâmetros
    ----------
    positions : ndarray (M, 3)
        Coordenadas tridimensionais dos sensores.

    azimuth : float
        Ângulo de azimute (rad).

    elevation : float
        Ângulo de elevação (rad).

    wavelength : float
        Comprimento de onda.

    Retorna
    -------
    ndarray (M,)
        Steering vector.
    """

    if wavelength <= 0:
        raise ValueError("O comprimento de onda deve ser maior que zero.")

    positions = np.asarray(positions, dtype=float)

    if positions.ndim != 2 or positions.shape[1] != 3:
        raise ValueError("positions deve possuir dimensão (M, 3).")

    azimuth = float(azimuth)
    elevation = float(elevation)

    # Número de onda
    k = 2 * np.pi / wavelength

    # Vetor unitário de propagação
    u = np.array([
        np.cos(elevation) * np.cos(azimuth),
        np.cos(elevation) * np.sin(azimuth),
        np.sin(elevation)
    ])

    # Produto interno rᵀu
    phase = positions @ u

    # Steering vector
    return np.exp(-1j * k * phase)
