from tinyec.ec import SubGroup, Curve
from tinyec.ec import SubGroup, Curve
from tinyec import registry
from tinyec import registry
import secrets
from nummaster.basic import sqrtmod

# field = SubGroup(p=17, g=(15, 13), n=18, h=1)
# curve = Curve(a=0, b=7, field=field, name='p1707')
# print('curve:', curve)

# for k in range(0, 25):
#     p = k * curve.g
#     print(f"{k} * G = ({p.x}, {p.y})")

# print("------------------------------------")

field = SubGroup(p=17, g=(5, 9), n=18, h=1)
curve = Curve(a=0, b=7, field=field, name='p1707')
print('curve:', curve)

for k in range(0, 25):
    p = k * curve.g
    print(f"{k} * G' = ({p.x}, {p.y})")

print("------------------------------------")

from datetime import datetime
start_time = datetime.now()
curve = registry.get_curve('secp192r1')
print('curve:', curve)

for k in range(0, 10):
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")

print("Cofactor =", curve.field.h)

print('Cyclic group order =', curve.field.n)

nG = curve.field.n * curve.g
print(f"n * G = ({nG.x}, {nG.y})")

print("------------------------------------")


curve = registry.get_curve('secp192r1')

privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g
print("private key:", privKey)
print("public key:", pubKey)
print("------------------------------------")


# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


