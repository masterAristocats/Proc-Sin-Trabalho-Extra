import numpy as np

from src.steering_vector import steering_vector


def conventional_weights(
    positions: np.ndarray,
    azimuth: float,
    elevation: float,
    wavelength: float,
    normalize: bool = True,
) -> np.ndarray:
    """
    Calcula os pesos do beamformer convencional (Delay-and-Sum).

    Parâmetros
    ----------
    positions : ndarray (M, 3)
        Coordenadas dos sensores.

    azimuth : float
        Azimute de apontamento (rad).

    elevation : float
        Elevação de apontamento (rad).

    wavelength : float
        Comprimento de onda.

    normalize : bool, opcional
        Se True, normaliza os pesos por M.

    Retorna
    -------
    ndarray (M,)
        Vetor de pesos complexo.
    """

    weights = steering_vector(
        positions,
        azimuth,
        elevation,
        wavelength
    ).reshape(-1)

    if normalize:
        weights /= weights.size

    return weights


def array_factor(
    positions: np.ndarray,
    azimuth,
    elevation,
    wavelength: float,
    weights: np.ndarray | None = None,
) -> np.ndarray:
    """
    Calcula o Array Factor.

    AF(θ,φ) = wᴴ a(θ,φ)
    """

    positions = np.asarray(positions, dtype=float)

    M = positions.shape[0]

    if weights is None:
        weights = np.ones(M, dtype=complex)

    weights = np.asarray(weights, dtype=complex).reshape(-1)

    if weights.size != M:
        raise ValueError(
            f"O vetor de pesos deve possuir {M} elementos."
        )

    a = steering_vector(
        positions,
        azimuth,
        elevation,
        wavelength
    )

    return np.einsum(
        "m,...m->...",
        np.conjugate(weights),
        a
    )


def beampattern(
    positions: np.ndarray,
    azimuth,
    elevation,
    wavelength: float,
    weights: np.ndarray | None = None,
    floor_db: float = -80.0,
) -> np.ndarray:
    """
    Calcula o beampattern normalizado em dB.

    Parâmetros
    ----------
    positions : ndarray (M,3)
        Coordenadas dos sensores.

    azimuth : float ou ndarray
        Azimute(s) em radianos.

    elevation : float ou ndarray
        Elevação(ões) em radianos.

    wavelength : float
        Comprimento de onda.

    weights : ndarray (M,), opcional
        Pesos complexos.

    floor_db : float
        Piso inferior em dB.

    Retorna
    -------
    ndarray
        Beampattern normalizado em dB.
    """

    af = array_factor(
        positions,
        azimuth,
        elevation,
        wavelength,
        weights
    )

    gain = np.abs(af)

    max_gain = np.max(gain)

    if max_gain <= 0:
        gain_norm = gain
    else:
        gain_norm = gain / max_gain

    with np.errstate(divide="ignore"):

        gain_db = 20*np.log10(
            np.maximum(
                gain_norm,
                10**(floor_db/20)
            )
        )

    return gain_db


if __name__ == "__main__":

    from src.generate_uca import generate_uca

    wavelength = 1.0

    positions = generate_uca(
        M=8,
        R=wavelength
    )

    phi = np.linspace(0, 2*np.pi, 721)

    gain = beampattern(
        positions,
        azimuth=phi,
        elevation=0,
        wavelength=wavelength
    )

    print(gain)
