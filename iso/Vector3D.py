import math

class Vector3D:



	def __init__(self, arg1 = 0, arg2 = 0, arg3 = 0):
		if isinstance(arg1, Vector3D):
			self.x = arg1.x
			self.y = arg1.y
			self.z = arg1.z
		else:
			self.x = arg1
			self.y = arg2
			self.z = arg3


	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		dz = self.z - other.z

		return math.sqrt(dx * dx + dy * dy + dz * dz)

	def __sub__(self, other):
		return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)


	def __add__(self, other):
		return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z


	def __mul__(self, other):
		return Vector3D(self.x * other, self.y * other, self.z * other)

	def __str__(self):
		return "Vector3D: (%f, %f, %f)" % (self.x, self.y, self.z)


if __name__ == "__main__":
	a = Vector3D(0,0,0)
	b = Vector3D(1,1,1)

	print(a.distance(b))