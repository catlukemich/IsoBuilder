
class Bounds3D:

    def __init__(self, x_extent = 1, y_extent = 1, z_extent = 1):
        self.min_x = -x_extent / 2
        self.max_x =  x_extent / 2
        self.min_y = -y_extent / 2
        self.max_y =  y_extent / 2
        self.min_z = -z_extent / 2
        self.max_z =  z_extent / 2



