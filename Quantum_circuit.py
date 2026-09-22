import pennylane as qp
import numpy as np

dev = qp.device('default.qubit',wires=1)

@qp.qnode(dev)
def quantum_circuit(y,x):
    qp.H(0)
    qp.RY(phi=y,wires = 0)
    qp.Z(0)
    qp.RX(phi=x,wires = 0)

    return qp.probs(0)


result = quantum_circuit(0.8, -0.4)

print("probability: ", result)