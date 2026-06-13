import numpy as np

# Функция для быстрого вычисления нормальной составляющей волнового вектора
def kz_count(k: np.ndarray, 
             kx: complex) -> complex:
    """
    Вычисляет нормальную составляющую волнового вектора kz.

    Parameters
    ---
    param k : np.ndarray
        Волновое число среды
    param kx : complex
        Поперечная составляющая волнового вектора
    
    Return
    ---
    complex
        Нормальная составляющая волнового вектора

    Notes
    ---
    - The branch of the square root for kz is chosen such that Im(kz)
    
    """
    kz = np.sqrt(k**2 - kx**2 + 0j)
    return np.where(np.imag(kz) >= 0, kz, -kz)

# Функция построения интерференционной матрицы
def interference_matrix(k1: complex, 
                        k2: complex) -> np.ndarray:
    """
    Построение интерференционной матрицы для двух границ сред.

    Parameters
    ---
    param k1 : complex
        Волновое число первой среды
    param k2 : complex
        Волновое число второй среды
    
    Return
    ---
    complex
        Интерференционная матрица размера 2x2
    """
    return np.array([
        [(k2 + k1)/2/k2, (k2 - k1)/2/k2],
        [(k2 - k1)/2/k2, (k2 + k1)/2/k2]
    ])

# Функция построения фазовой матрицы
def phase_matrix(k: complex, 
                 h: float) -> np.ndarray:
    """
    Построение фазовой матрицы распространения волны через среду.

    Parameters
    ---
    param k : complex
        Волновое число среды
    param h : float
        Толщина слоя
    
    Return
    ---
    np.ndarray
        Фазовая матрица размера 2x2
    """
    exp_term = np.exp(1j * k * h)
    return np.diag([exp_term, 1/exp_term])

# Основной алгоритм метода Transfer Matrix Method
def tmm_reflection(k_values: np.ndarray, 
                   h_layers: np.ndarray, 
                   incident_angle: float) -> complex:
    """
    Compute the complex reflection coefficient using the Transfer Matrix Method (TMM)
    for a multilayer planar structure under TE polarization.

    Parameters
    ----------
    h_layers : np.ndarray
        Thicknesses of the internal layers (excluding incident and substrate media),
        shape (N,).
    k_values : np.ndarray
        Wave numbers of all media including incident medium and substrate,
        shape (N+2,).
    incident_angle : float
        Angle of incidence in radians.

    Returns
    -------
    complex
        Complex reflection coefficient r.

    Notes
    -----
    - TE polarization is assumed.
    - The branch of the square root for kz is chosen such that Im(kz) >= 0.
    - The implementation follows the standard transfer matrix formalism.
    """
    assert len(k_values) == len(h_layers) + 2
    assert np.all(np.array(h_layers) >= 0)

    # Преобразование углов в вещественное пространство
    if isinstance(incident_angle, complex):
        raise ValueError("Угол падения должен быть вещественным числом.")
        
    # Подготовительные шаги
    k_values = np.asarray(k_values)
    kx = k_values[0] * np.sin(incident_angle)
    kz_values = kz_count(k_values, kx)

    # Формирование массива толщин с нулём в конце (условия внешней среды)
    layer_thicknesses = np.append([0.0], h_layers)
    
    # Начальное состояние: единичная матрица
    total_matrix = np.eye(2, dtype=complex)
    
    # Основная итерация по слоям сверху вниз
    for idx in range(len(kz_values)-1, 0, -1):
        current_kz = kz_values[idx]
        next_kz = kz_values[idx - 1]
        thickness = layer_thicknesses[idx - 1]

        int_mat = interference_matrix(current_kz, next_kz)
        phs_mat = phase_matrix(next_kz, thickness)

        total_matrix = total_matrix @ int_mat @ phs_mat
    
    # Извлекаем коэффициент отражения из полученной матрицы
    r_coeff = total_matrix[1, 0] / total_matrix[1, 1]
    return r_coeff