import numpy as np

from src.steering_vector import steering_vector


def beampattern(
    positions,
    azimuth,
    elevation,
    wavelength,
    weights=None
):
    """
    Calcula o beampattern normalizado em dB.

    Parâmetros
    ----------
    positions : ndarray (M, 3)
        Coordenadas tridimensionais dos sensores.

    azimuth : float ou array_like
        Azimute(s) em radianos.

    elevation : float
        Elevação em radianos.

    wavelength : float
        Comprimento de onda.

    weights : ndarray (M,), opcional
        Vetor de pesos complexo. Se None, utiliza pesos uniformes.

    Retorna
    -------
    ndarray
        Ganho normalizado em dB.
    """

    positions = np.asarray(positions, dtype=float)

    M = positions.shape[0]

    if weights is None:
        weights = np.ones(M, dtype=complex)
    else:
        weights = np.asarray(weights, dtype=complex)

        if weights.shape != (M,):
            raise ValueError(
                f"O vetor de pesos deve possuir dimensão ({M},)."
            )

    azimuth = np.atleast_1d(azimuth)

    array_factor = np.zeros(azimuth.size, dtype=complex)

    for i, phi in enumerate(azimuth):

        a = steering_vector(
            positions,
            phi,
            elevation,
            wavelength
        )

        array_factor[i] = np.conjugate(weights) @ a

    # Magnitude do Array Factor
    gain = np.abs(array_factor)

    max_gain = np.max(gain)

    if max_gain == 0:
        raise ValueError("O ganho máximo é igual a zero.")

    # Normalização
    gain /= max_gain

    # Conversão para dB
    gain_db = 20 * np.log10(np.maximum(gain, 1e-12))

    return gain_db
