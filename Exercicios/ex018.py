from math import radians, cos, sin, tan

ang = float(input('Digite um angulo:'))
cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))

print(f'cosseno e {cos:.2f}, o seno e {sen:.2f}, a tangente e {tan:.2f}')
