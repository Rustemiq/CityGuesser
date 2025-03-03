import os
import sys

import pygame
import requests
from collections import deque

from get_scaling import get_scaling
from get_toponym import get_toponym

CITIES = deque(['Уфа', 'Рязань', 'Питер', 'Казань', 'Екатеринбург', 'Норильск'])
map_file = "map.png"

server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'


def get_city_map():
    toponym = get_toponym(CITIES[0])
    params = {
        'apikey': api_key,
        'll': toponym['Point']['pos'].replace(' ', ','),
        'spn': get_scaling(toponym)
    }

    response = requests.get(server_address, params)

    if not response:
        print("Ошибка выполнения запроса")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    with open(map_file, "wb") as file:
        file.write(response.content)


def swipe_slide(direction):
    CITIES.rotate(direction)
    get_city_map()
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


if __name__ == '__main__':

    print('Менять слайды стрелочками')

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    swipe_slide(-1)
                if event.key == pygame.K_LEFT:
                    swipe_slide(1)
    pygame.quit()
    os.remove(map_file)