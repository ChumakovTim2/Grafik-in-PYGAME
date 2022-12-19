import pygame as pg

pg.init()
a =[[0,0]]
for i in range(int(input('Введите количество координат: '))): #координаты не должны превышать размер поля
    a.append([int(c) for c in input().split(',')]) #введите координаты (2 числа) через запятую

screen = pg.display.set_mode((800, 800))

while True:
    screen.fill((255,255,255))
    for b in range(len(a)-1):
        pg.draw.circle(screen, (0,0,0),a[b], 2)
        pg.draw.circle(screen, (0,0,0),a[b+1], 2)
        pg.draw.aaline(screen, ('red'), a[b], a[b+1])
    pg.display.flip()
