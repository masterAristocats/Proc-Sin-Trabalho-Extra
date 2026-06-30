import numpy as np


def direction_unit_vector(
    azimuth,
    elevation
) -> np.ndarray:
    """
    Calcula o vetor unitário de propagação.

    Parâmetros
    ----------
    azimuth : float ou ndarray
        Azimute(s) em radianos.

    elevation : float ou ndarray
        Elevação(ões) em radianos.

    Retorna
    -------
    ndarray
        Vetor(es) unitário(s) de propagação. A última dimensão
        corresponde às componentes (x, y, z).
    """

    azimuth, elevation = np.broadcast_arrays(
        azimuth,
        elevation
    )

    return np.stack(
        (
            np.cos(elevation) * np.cos(azimuth),
            np.cos(elevation) * np.sin(azimuth),
            np.sin(elevation),
        ),
        axis=-1,
    )


def steering_vector(
    positions: np.ndarray,
    azimuth,
    elevation,
    wavelength: float,
) -> np.ndarray:
    """
    Calcula o steering vector de um arranjo de sensores.

    Parâmetros
    ----------
    positions : ndarray (M, 3)
        Coordenadas tridimensionais dos sensores.

    azimuth : float ou ndarray
        Ângulo(s) de azimute em radianos.

    elevation : float ou ndarray
        Ângulo(s) de elevação em radianos.

    wavelength : float
        Comprimento de onda.

    Retorna
    -------
    ndarray
        Steering vector.

        O formato da saída é:

            broadcast(azimuth, elevation).shape + (M,)
    """

    positions = np.asarray(positions, dtype=float)

    if positions.ndim != 2 or positions.shape[1] != 3:
        raise ValueError(
            "positions deve possuir dimensão (M, 3)."
        )

    wavelength = float(wavelength)

    if wavelength <= 0:
        raise ValueError(
            "O comprimento de onda deve ser maior que zero."
        )

    unit_vectors = direction_unit_vector(
        np.asarray(azimuth),
        np.asarray(elevation)
    )

    # Produto interno rᵀu para todos os ângulos simultaneamente
    phase = np.tensordot(
        unit_vectors,
        positions.T,
        axes=([-1], [0])
    )

    # Steering vector
    return np.exp(
        -1j * (2 * np.pi / wavelength) * phase
    )


if __name__ == "__main__":

    from src.generate_uca import generate_uca

    wavelength = 1.0

    positions = generate_uca(
        M=8,
        R=wavelength
    )

    phi = np.linspace(0, 2 * np.pi, 8)

    a = steering_vector(
        positions,
        azimuth=phi,
        elevation=0,
        wavelength=wavelength
    )

    print(a.shape)
