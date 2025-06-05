import numpy as np
import random 

def print_matrix(x) :  
    A = np.random.randint(0, x, size=(x, x))
    for row in A:
        print(" ".join(str(val) for val in row))
    return A

def calc_size(A, x):
    edges = 0
    for i in range(x) :
        for j in range (x) :    
            edges += A[i, j]
    print("The size of a graph is %d" % edges)

def calc_degrees(A, x) :    
    out_deg = []
    in_deg = []
    deg = []
    for i in range (x) : #out degrees 
        out_deg.append(np.sum(A[i, :]))
        print("Vertex %d has out-degree  %d" % (i+1, out_deg[i]))

    for j in range (x) : # in degree
        in_deg.append(np.sum(A[:, j]))
        print("Vertex %d has in-degree  %d" % (j+1, in_deg[j]))

    for k in range(x) : #degree
        deg.append(out_deg[k] + in_deg[k])
        print("Vertex %d has degree  %d" % (k+1, deg[k]))

x =  int(input("Enter the number of Vertices: "))

while(x < 2) :
    try : 
        print("Invalid entry %d" % x)
        x = int(input("Enter the number of Vertices: "))
        break
    except ValueError:
        print("Invalid entry %d" % x)

A = print_matrix(x)
calc_size(A, x)
calc_degrees(A, x)
