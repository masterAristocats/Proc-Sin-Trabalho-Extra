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
    positions : numpy.ndarray
        Coordenadas dos sensores (M, 3).

    azimuth : array_like
        Vetor de azimutes (rad).

    elevation : float
        Elevação (rad).

    wavelength : float
        Comprimento de onda.

    weights : numpy.ndarray, opcional
        Vetor de pesos complexo.
        Se None, utiliza pesos uniformes.

    Retorna
    -------
    numpy.ndarray
        Ganho normalizado em dB.
    """

    M = positions.shape[0]

    if weights is None:
        weights = np.ones(M, dtype=complex)

    azimuth = np.atleast_1d(azimuth)

    AF = np.zeros(len(azimuth), dtype=complex)

    for i, phi in enumerate(azimuth):

        a = steering_vector(
            positions,
            phi,
            elevation,
            wavelength
        )

        AF[i] = np.conjugate(weights) @ a

    # Magnitude
    B = np.abs(AF)

    # Normalização
    B /= np.max(B)

    # Conversão para dB
    B_dB = 20 * np.log10(np.maximum(B, 1e-12))

    return B_dB
