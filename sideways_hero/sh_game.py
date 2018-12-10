import sys

import pygame

from ship import Ship

class SidewaysHero:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sideways Hero")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Up key has been pressed!
                        #  We want the ship to move up.
                        self.ship.rect.y -= 10
                    if event.key == pygame.K_DOWN:
                        self.ship.rect.y += 10
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.rect.x -= 10
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

            # Update positions of any characters that might be moving.
            self.ship.update()

            self.screen.fill((255, 255, 255))
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sh_game = SidewaysHero()
    sh_game.run_game()
