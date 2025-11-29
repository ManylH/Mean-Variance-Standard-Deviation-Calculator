import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir en matrice 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calculs
    mean = [
        matrix.mean(axis=0).tolist(),
        matrix.mean(axis=1).tolist(),
        matrix.flatten().mean().tolist()
    ]

    variance = [
        matrix.var(axis=0).tolist(),
        matrix.var(axis=1).tolist(),
        matrix.flatten().var().tolist()
    ]

    standard_deviation = [
        matrix.std(axis=0).tolist(),
        matrix.std(axis=1).tolist(),
        matrix.flatten().std().tolist()
    ]

    max_vals = [
        matrix.max(axis=0).tolist(),
        matrix.max(axis=1).tolist(),
        matrix.flatten().max().tolist()
    ]

    min_vals = [
        matrix.min(axis=0).tolist(),
        matrix.min(axis=1).tolist(),
        matrix.flatten().min().tolist()
    ]

    sum_vals = [
        matrix.sum(axis=0).tolist(),
        matrix.sum(axis=1).tolist(),
        matrix.flatten().sum().tolist()
    ]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_vals,
        'min': min_vals,
        'sum': sum_vals
    }
