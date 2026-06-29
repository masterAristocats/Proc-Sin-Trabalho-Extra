import numpy as np

def generate_ula(M, d):
    """
    Gera as coordenadas tridimensionais de um
    Uniform Linear Array (ULA).

    Parâmetros
    ----------
    M : int
        Número de sensores.
    d : float
        Espaçamento entre sensores.

    Retorna
    -------
    positions : ndarray (M, 3)
        Coordenadas (x, y, z) dos sensores.
    """

    if M <= 0:
        raise ValueError("M deve ser maior que zero.")

    if d <= 0:
        raise ValueError("d deve ser maior que zero.")

    positions = np.zeros((M, 3), dtype=float)

    # Sensores distribuídos ao longo do eixo x
    positions[:, 0] = np.arange(M) * d

    return positions
