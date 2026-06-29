import numpy as np

from src.steering_vector import steering_vector


def beamformer(
    x,
    positions,
    steering_direction,
    wavelength,
    weights=None
):
    """
    Beamformer convencional (Delay-and-Sum).

    Parâmetros
    ----------
    x : ndarray (M,)
        Sinais recebidos pelos sensores.

    positions : ndarray (M, 3)
        Coordenadas tridimensionais dos sensores.

    steering_direction : tuple
        Tupla (azimuth, elevation) em radianos.

    wavelength : float
        Comprimento de onda.

    weights : ndarray (M,), opcional
        Vetor de pesos complexo. Se None, utiliza
        os pesos do beamformer Delay-and-Sum.

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
            f"x deve possuir dimensão ({M},)."
        )

    azimuth, elevation = steering_direction

    # Vetor diretor
    a = steering_vector(
        positions,
        azimuth,
        elevation,
        wavelength
    )

    # Delay-and-Sum (pesos padrão)
    if weights is None:
        weights = a / M
    else:
        weights = np.asarray(weights, dtype=complex)

        if weights.shape != (M,):
            raise ValueError(
                f"O vetor de pesos deve possuir dimensão ({M},)."
            )

    # Saída do beamformer
    y = np.conjugate(weights) @ x

    return y


if __name__ == "__main__":

    from src.generate_ula import generate_ula

    wavelength = 1.0

    M = 8
    d = wavelength / 2

    positions = generate_ula(M, d)

    # Sinal recebido (exemplo)
    x = np.ones(M, dtype=complex)

    # Direção de observação
    steering_direction = (
        np.deg2rad(0),
        np.deg2rad(0)
    )

    y = beamformer(
        x,
        positions,
        steering_direction,
        wavelength
    )

    print("Saída do beamformer:")
    print(y)
