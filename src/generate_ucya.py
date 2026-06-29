import numpy as np


def generate_ucya(Mc, Nz, R, dz):
    """
    Gera as coordenadas tridimensionais de um Uniform Cylindrical Array (UCYA).

    Parâmetros
    ----------
    Mc : int
        Número de sensores por anel.
    Nz : int
        Número de anéis.
    R : float
        Raio do cilindro.
    dz : float
        Espaçamento vertical entre os anéis.

    Retorna
    -------
    numpy.ndarray
        Matriz de dimensão (Mc * Nz, 3) contendo as coordenadas
        (x, y, z) dos sensores.
    """

    if Mc <= 0:
        raise ValueError("Mc deve ser maior que zero.")

    if Nz <= 0:
        raise ValueError("Nz deve ser maior que zero.")

    if R <= 0:
        raise ValueError("R deve ser maior que zero.")

    if dz <= 0:
        raise ValueError("dz deve ser maior que zero.")

    positions = np.zeros((Mc * Nz, 3), dtype=float)

    # Ângulos igualmente espaçados em cada anel
    phi = np.linspace(0, 2 * np.pi, Mc, endpoint=False)

    k = 0

    # Percorre os anéis
    for iz in range(Nz):
        z = iz * dz

        # Percorre os sensores do anel
        for angle in phi:
            positions[k, 0] = R * np.cos(angle)
            positions[k, 1] = R * np.sin(angle)
            positions[k, 2] = z
            k += 1

    return positions


if __name__ == "__main__":
    Mc = 8
    Nz = 3
    R = 1.0
    dz = 0.5

    positions = generate_ucya(Mc, Nz, R, dz)

    print("Posições dos sensores:")
    print(positions)
