import math
ang=float(input('digite o ângulo para saber seu seno, cosseno e tangente:'))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tg=math.tan(math.radians(ang))
print('ângulo {}º\nsen={:.2f}º\ncos{:.2f}º\ntg={:.2f}º'.format(ang, sen, cos, tg))
