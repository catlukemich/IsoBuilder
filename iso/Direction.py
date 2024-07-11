from .Vector3D import *

class Direction:
    X_PLUS = Vector3D(1, 0, 0)  # +1 on X axis
    X_MINUS = Vector3D(-1, 0, 0)  # -1 on X axis
    Y_PLUS = Vector3D(0, 1, 0)  # -1 on Y axis
    Y_MINUS = Vector3D(0, -1, 0)  # +1 on Y axis
    Z_PLUS = Vector3D(0, 0, 1)  # +1 on Z axis
    Z_MINUS = Vector3D(0, 0, -1)  # -1 on Z axis
