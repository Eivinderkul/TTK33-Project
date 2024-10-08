import numpy as np

##Function that takes two points and two vectors in the world coordinate frame and returns the best possible point "triang_point"
def triang(P_1, P_2, v_1, v_2):
    ##A*lambda=b

    A = np.array([[np.dot(v_1,v_1), -np.dot(v_1, v_2)],
                  [-np.dot(v_1, v_2), np.dot(v_2, v_2)]])
    
    b = np.array([np.dot(P_2-P_1, v_1),
                  -np.dot(P_2-P_1, v_2)])
    
    lam = np.linalg.solve(A,b)

    triang_point = ((P_1+lam[0]*v_1)+(P_2+lam[1]*v_2))/2
    return triang_point