import sys

import pygame

from settings import Setting


class AlienInvasion:
    """Класс для управления ресурсами и проведением игры."""

    def __init__(self):
        """Инициализирует игру и создает иговые ресурсы."""
        pygame.init()
        self.settings = Setting()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
