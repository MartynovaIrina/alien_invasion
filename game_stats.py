import os
import json
class GameStats:
    '''Отслеживание статистики для игры.'''

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # Переменная для рекорда
        path = os.getcwd()
        if 'best.txt' in os.listdir():
            with open('best.txt') as file:
                self.high_score = json.load(file)
        else:
            self.high_score = 0        

    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1