import numpy as np

def generate_ucya(Mc, Nz, R, dz):
    """
    Gera as coordenadas tridimensionais de um
    Uniform Cylindrical Array (UCYA).

    Parâmetros
    ----------
    Mc : int
        Número de sensores por anel.

    Nz : int
        Número de anéis.

    R : float
        Raio do cilindro.

    dz : float
        Espaçamento vertical entre anéis.

    Retorna
    -------
    positions : ndarray (Mc*Nz, 3)
        Coordenadas (x, y, z) dos sensores.
    """

    if Mc <= 0 or Nz <= 0:
        raise ValueError("Mc e Nz devem ser maiores que zero.")

    if R <= 0 or dz <= 0:
        raise ValueError("R e dz devem ser maiores que zero.")

    positions = np.zeros((Mc * Nz, 3), dtype=float)

    phi = np.linspace(0, 2*np.pi, Mc, endpoint=False)

    k = 0
    for iz in range(Nz):
        z = iz * dz

        for ang in phi:
            positions[k, 0] = R * np.cos(ang)
            positions[k, 1] = R * np.sin(ang)
            positions[k, 2] = z
            k += 1

    return positions
