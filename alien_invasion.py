import sys

import pygame

from settings import Settings

from ship import Ship

from alien import Alien

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard



def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the Play button
    play_button = Button(ai_settings,screen,"Play")

    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #make a ship
    ship = Ship(ai_settings, screen)

    #make an alien
    alien = Alien(ai_settings,screen)

    #make a group to store bullets in
    bullets = Group()

    #make a group of aliens
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #set the background color
    bg_color = (230,230,230)

    #Start main loop for the game
    while True:

        #call watch for keyboard and mouse movements
        gf.check_events(ai_settings,screen,stats, sb, play_button,ship, aliens, bullets)

        if stats.game_active:
            #call ship update method
            ship.update()

            #call repopulate fleet method
            gf.update_bullets(ai_settings,screen, stats, sb, ship,aliens,bullets)

            #call alien update method
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)


        #call redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        

        

run_game()