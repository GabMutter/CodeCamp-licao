import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    def compute(func):
        return [
            func(matrix, axis=0).tolist(),   
            func(matrix, axis=1).tolist(),  
            func(matrix).item() if np.isscalar(func(matrix)) else func(matrix).tolist() 
        ]

    calculations = {
        'mean': compute(np.mean),
        'variance': compute(np.var),
        'standard deviation': compute(np.std),
        'max': compute(np.max),
        'min': compute(np.min),
        'sum': compute(np.sum)
    }
    return calculations