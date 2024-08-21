lar = float(input('Lardura da parede: '))
alt = float(input('Altura da parede :'))
area = lar * alt
tin = area / 2
print('A parede tem as medidas de {}x{} e sua área é {}m².'.format(lar, alt, area))
print('Para pintar sua parede, será necessario {}l de tinta'.format(tin))
