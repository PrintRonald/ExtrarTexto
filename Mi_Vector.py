from vectors import *

#Mi_vector = Vector2D(2,3)

#print(Mi_vector)

#print(Mi_vector.module)

#print(Mi_vector.scalar_prod(3))

v1 = Vector2D(2,3)
v2 = Vector2D(4,6)
#print(v1.extend_to_3D())
#print(Vector2D.distance(v1, v2))
#print(v1.scalar_prod(2))

v3 = Vector3D(1,2,3)
v4 = Vector3D(2,4,6)
#print(v3)
#print(type(v3.scalar_prod(2)))
print(Vector3D.dot_product(v3, v4))
#print(v3.scalar_prod(2))
#print(Vector3D.forward())
