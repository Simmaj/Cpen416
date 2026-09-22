import pennylane as qp
import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def quantum_function1():
    qp.Hadamard(0) 
    qp.RY(phi = np.pi/2, wires=0)     
    qp.RY(phi = -np.pi/2, wires=0)  
    qp.S(0)         

    return qp.probs(wires = 0)




@qp.qnode(dev)
def quantum_function2():
    qp.RY(phi = np.pi/2, wires=0)     
    qp.RY(phi = np.pi/4, wires=0)  
    qp.T(0)         

    return qp.probs(wires = 0)

@qp.qnode(dev)
def quantum_function3():
    qp.H(0)
    qp.adjoint(qp.S(0))
    qp.adjoint(qp.T(0))
    qp.X(0)**0.5    

    return qp.probs(wires = 0)


result1 = quantum_function1()
result2 = quantum_function2()
result3 = quantum_function3()

print("Probabilities for circuti one: \n", result1)
print("Probabilities for circuti two: \n", result2)
print("Probabilities for circuti three: \n", result3)

