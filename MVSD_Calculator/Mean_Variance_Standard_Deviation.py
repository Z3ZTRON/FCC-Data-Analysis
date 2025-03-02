
import numpy as np

def calculator(array):
    if len(array) != 9:
        raise ValueError("The array must contain nine numbers. ") # 
    
    matrix = np.array(array).reshape((3,3)) # Turn the list to an array
    
    compile_calc = {
        'mean':[matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), np.mean(matrix).tolist()],
        'variance':[matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation':[matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), np.std(matrix).tolist()],
        'max':[matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), np.max(matrix).tolist()],
        'min':[matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), np.min(matrix).tolist()],
        'sum':[matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), np.sum(matrix).tolist()]
    }
    
    return compile_calc

print(calculator([2,6,2,8,4,0,1,5,7]))
