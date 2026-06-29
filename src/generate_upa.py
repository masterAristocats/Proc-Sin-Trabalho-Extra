import numpy as np

def generate_upa(Mx, My, dx, dy):
    """
    Gera as coordenadas tridimensionais de um
    Uniform Planar Array (UPA).

    Parâmetros
    ----------
    Mx : int
        Número de sensores na direção x.

    My : int
        Número de sensores na direção y.

    dx : float
        Espaçamento horizontal.

    dy : float
        Espaçamento vertical.

    Retorna
    -------
    positions : ndarray (Mx*My, 3)
        Coordenadas (x, y, z) dos sensores.
    """

    if Mx <= 0 or My <= 0:
        raise ValueError("Mx e My devem ser maiores que zero.")

    if dx <= 0 or dy <= 0:
        raise ValueError("dx e dy devem ser maiores que zero.")

    positions = np.zeros((Mx * My, 3), dtype=float)

    k = 0
    for j in range(My):
        for i in range(Mx):
            positions[k, 0] = i * dx
            positions[k, 1] = j * dy
            k += 1

    return positions
