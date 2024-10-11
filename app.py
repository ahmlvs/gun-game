import numpy as np
import pygame as pg
from random import randint
from config import WHITE, BLACK, RED, SCREEN_SIZE
from functions import rand_color


def main():
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("The gun-game")

    done = False
    clock = pg.time.Clock()

    mgr = Manager(n_targets=10)

    while not done:
        clock.tick(15)
        screen.fill(BLACK)
        done = mgr.process(pg.event.get(), screen)
        pg.display.flip()

    pg.quit()


class Manager:
    '''
    Class that manages events' handling,
    ball's motion and collision, target creation, etc.
    '''

    def __init__(self, n_targets=1):
        self.balls = []
        self.targets = []
        self.n_targets = n_targets
        self.new_mission()

    def new_mission(self):
        '''
        Adds new targets.
        '''
        pass

    def process(self, events, screen):
        '''
        Runs all necessary method for each iteration.
        Adds new targets, if previous are destroyed.
        '''
        done = self.handle_events(events)

        self.draw(screen)

        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()

        return done

    def handle_events(self, events):
        '''
        Handles events from keyboard, mouse, etc.
        '''
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done

    def draw(self, screen):
        '''
        Runs balls', gun's, targets' and score table's drawing method.
        '''
        for ball in self.balls:
            ball.draw(screen)
        for target in self.targets:
            target.draw(screen)


if __name__ == "__main__":
    main()
