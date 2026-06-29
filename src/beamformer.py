import numpy as np

from src.steering_vector import steering_vector


def beamformer(
    x,
    positions,
    steering_direction,
    wavelength
):
    """
    Beamformer convencional (Delay-and-Sum).

    Parâmetros
    ----------
    x : ndarray (M,)
        Sinais recebidos pelos sensores.

    positions : ndarray (M, 3)
        Coordenadas dos sensores.

    steering_direction : tuple
        (azimuth, elevation) em radianos.

    wavelength : float
        Comprimento de onda.

    Retorna
    -------
    complex
        Saída do beamformer.
    """

    positions = np.asarray(positions, dtype=float)
    x = np.asarray(x, dtype=complex)

    M = positions.shape[0]

    if x.shape != (M,):
        raise ValueError(
            f"x deve possuir dimensão ({M},)"
        )

    azimuth, elevation = steering_direction

    # Steering vector
    a = steering_vector(
        positions,
        azimuth,
        elevation,
        wavelength
    )

    # Delay-and-Sum
    w = a / M

    # Saída
    y = np.conjugate(w) @ x

    return y
