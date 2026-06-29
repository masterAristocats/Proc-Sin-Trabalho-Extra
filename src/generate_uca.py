import numpy as np


def generate_uca(M, R):
    """
    Gera as coordenadas tridimensionais de um Uniform Circular Array (UCA).

    Parâmetros
    ----------
    M : int
        Número de sensores.
    R : float
        Raio do círculo.

    Retorna
    -------
    numpy.ndarray
        Matriz de dimensão (M, 3) contendo as coordenadas (x, y, z)
        dos sensores.
    """

    if M <= 0:
        raise ValueError("M deve ser maior que zero.")

    if R <= 0:
        raise ValueError("R deve ser maior que zero.")

    positions = np.zeros((M, 3), dtype=float)

    # Ângulos igualmente espaçados
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    # Coordenadas dos sensores
    positions[:, 0] = R * np.cos(phi)
    positions[:, 1] = R * np.sin(phi)

    return positions


if __name__ == "__main__":
    M = 8
    R = 1.0

    positions = generate_uca(M, R)

    print("Posições dos sensores:")
    print(positions)
