import numpy as np

from src.beampattern import conventional_weights


def beamformer(
    x: np.ndarray,
    positions: np.ndarray,
    steering_direction: tuple[float, float],
    wavelength: float,
) -> np.ndarray:
    """
    Aplica o beamformer convencional Delay-and-Sum.

    Parâmetros
    ----------
    x : ndarray (M,) ou (M, N)
        Sinais recebidos pelos sensores.

    positions : ndarray (M, 3)
        Coordenadas tridimensionais dos sensores.

    steering_direction : tuple(float, float)
        Tupla (azimuth, elevation) em radianos.

    wavelength : float
        Comprimento de onda.

    Retorna
    -------
    ndarray
        Saída do beamformer.

        - Se x possui dimensão (M,), retorna um escalar complexo.
        - Se x possui dimensão (M, N), retorna um vetor de dimensão (N,).
    """

    x = np.asarray(x, dtype=complex)
    positions = np.asarray(positions, dtype=float)

    if positions.ndim != 2 or positions.shape[1] != 3:
        raise ValueError(
            "positions deve possuir dimensão (M, 3)."
        )

    if x.ndim not in (1, 2):
        raise ValueError(
            "x deve possuir dimensão (M,) ou (M, N)."
        )

    if x.shape[0] != positions.shape[0]:
        raise ValueError(
            "x deve possuir uma linha para cada sensor."
        )

    azimuth, elevation = steering_direction

    # Pesos Delay-and-Sum
    weights = conventional_weights(
        positions,
        azimuth,
        elevation,
        wavelength
    )

    # Saída do beamformer
    return np.conjugate(weights) @ x


if __name__ == "__main__":

    from src.generate_ula import generate_ula

    wavelength = 1.0

    positions = generate_ula(
        M=8,
        d=wavelength / 2
    )

    # Exemplo com uma única amostra
    x = np.ones(8, dtype=complex)

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
