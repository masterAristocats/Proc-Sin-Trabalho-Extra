import numpy as np


def steering_vector(positions, azimuth, elevation, wavelength):
    """
    Calcula o steering vector de um arranjo de antenas.

    Parâmetros
    ----------
    positions : numpy.ndarray
        Matriz (M, 3) contendo as coordenadas (x, y, z) dos sensores.

    azimuth : float
        Ângulo de azimute em radianos.

    elevation : float
        Ângulo de elevação em radianos.

    wavelength : float
        Comprimento de onda.

    Retorna
    -------
    numpy.ndarray
        Steering vector de dimensão (M,).
    """

    if wavelength <= 0:
        raise ValueError("O comprimento de onda deve ser maior que zero.")

    # Número de onda
    k = 2 * np.pi / wavelength

    # Vetor unitário de propagação
    u = np.array([
        np.cos(elevation) * np.cos(azimuth),
        np.cos(elevation) * np.sin(azimuth),
        np.sin(elevation)
    ])

    # Produto escalar rᵀu para todos os sensores
    phase = positions @ u

    # Steering vector
    a = np.exp(-1j * k * phase)

    return a
