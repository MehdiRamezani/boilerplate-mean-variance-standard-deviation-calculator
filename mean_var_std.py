import numpy as np

def calculate(list):

  mat_temp = np.array(list)
  if mat_temp.shape != (9,):
    raise ValueError('List must contain nine numbers.')
    
  shape = (3, 3)
  mat_reshape = mat_temp.reshape(shape)
    
  mean = [mat_reshape.mean(axis=0).tolist() , mat_reshape.mean(axis=1).tolist(), mat_reshape.mean()]
    
  variance = [mat_reshape.var(axis=0).tolist() , mat_reshape.var(axis=1).tolist(), mat_reshape.var()]
  
  std = [mat_reshape.std(axis=0).tolist() , mat_reshape.std(axis=1).tolist(), mat_reshape.std()]
  
  max =[mat_reshape.max(axis=0).tolist() , mat_reshape.max(axis=1).tolist(), mat_reshape.max()]
  
  min =[mat_reshape.min(axis=0).tolist() , mat_reshape.min(axis=1).tolist(), mat_reshape.min()]
  
  sum = [mat_reshape.sum(axis=0).tolist() , mat_reshape.sum(axis=1).tolist(), mat_reshape.sum()]
    
  calculations = {'mean': mean ,'variance': variance, 'standard deviation': std, 'max': max, 'min': min, 'sum': sum}
  return calculations