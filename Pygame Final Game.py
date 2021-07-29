# Imports
import pygame
from pygame.locals import *
from pygame import mixer

# Inputs and Beginning of Game
input("\033[1;32mSet Sound Volume to 10 for best sound effects. ")
input("\033[1;32mWelcome to \033[1;33mStar Clicker\033[1;32m\nIn this game, your goal is to make as many stars as possible. Pres\nYou can make endless stars! Hover over a unit for info.\nClick the giant sun to make 1 star.\nas you click more, your levels will incrase, with each one doubling the amount of stars you make per click.\nYou also will have units, but them at the right side of th screen. \nUnits make a certain amount of stars each second.\nThe cost of buying more star units will go up every time you buy one. \nHave fun! ")
music_type = eval(input("Music type (1), (2), or (3): "))

# Initializations
pygame.init()

# Program Variables
title = "Star Clicker"
FPS_clock = pygame.time.Clock()
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
width = 1150
height = 810
pygame.display.set_caption(title)
screen = pygame.display.set_mode((width, height))

# Images Load
star_background = pygame.image.load('Star.jpg').convert()
sun = pygame.image.load("The Sun.png")
brown1 = pygame.image.load('Brown Dwarf.jpg').convert()
red1 = pygame.image.load('Red Dwarf.jpg').convert()
neutron1 = pygame.image.load('Neutron Star.jpg').convert()
regular1 = pygame.image.load('Regular Star.jpg').convert()
giant1 = pygame.image.load('Red Giant.jpg').convert()
supergiant1 = pygame.image.load('Blue Supergiant.jpg').convert()
nebula1 = pygame.image.load('Nebula.jpg').convert()
foam1 = pygame.image.load('Quantum Foam.jpg').convert()
bang1 = pygame.image.load('The Big Bang.jpg').convert()

# Images Fit Size
star_background = pygame.transform.scale(star_background, (width, height))
sun = pygame.transform.scale(sun, (300, 300))
brown = pygame.transform.scale(brown1, (200, 90))
red = pygame.transform.scale(red1, (200, 90))
neutron = pygame.transform.scale(neutron1, (200, 90))
regular = pygame.transform.scale(regular1, (200, 90))
giant = pygame.transform.scale(giant1, (200, 90))
supergiant = pygame.transform.scale(supergiant1, (200, 90))
nebula = pygame.transform.scale(nebula1, (200, 90))
foam = pygame.transform.scale(foam1, (200, 90))
bang = pygame.transform.scale(bang1, (200, 90))

# If_clicked Image
sun_if_clicked = pygame.transform.scale(sun, (325, 325))

# Game Variables
stars = 0
star_level = 1
star_barrier = 50
stars_per_second = 0
counter_for_stars = 0
click_font = pygame.font.SysFont('Impact', 30)
star_count_font = pygame.font.SysFont("Calibri", 35, bold=True)
purchase_font = pygame.font.SysFont("Impact", 40)
display_font = pygame.font.SysFont("Impact", 40)
info_font = pygame.font.SysFont("Calibri", 24, bold=True)
amount_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
star_producers = [brown, red, neutron, regular, giant, supergiant, nebula, foam, bang]
stars_made_per_unit = [0.1, 1, 8, 47, 260, 1400, 7800, 44000, 260000]
cost_list = [15, 100, 1500, 8000, 20000, 150000, 1000000, 2500000, 10000000]
mouse_click_counter = 0  # Sets a mouse click counter


# Background Music Function
def music():
    mixer.init()  # Initiates the Mixer

    # Music Select 1
    if music_type == 1:
        pygame.mixer.music.load('Battle Cats BGM - Main Theme.mp3')
        pygame.mixer.music.play(-1)

    # Music Select 2
    elif music_type == 2:
        pygame.mixer.music.load('Battle Cats BGM - Uphill Battle.mp3')
        pygame.mixer.music.play(-1)

    # Music Select 3
    elif music_type == 3:
        pygame.mixer.music.load('Battle Cats BGM - Boss Battle Theme.mp3')
        pygame.mixer.music.play(-1)


# Click Sound Effect
def click():
    click = pygame.mixer.Sound('Click.wav')  # Click effect variable
    click.play()  # Plays the click sound


# Purchase Success Sound Effect
def purchase_success():
    success = pygame.mixer.Sound("Purchase Success.wav")
    success.play()


# Purchase Fail Sound Effect
def purchase_fail():
    fail = pygame.mixer.Sound("Purchase Fail.wav")
    fail.play()


# Calls the music function
music()

# Screen and Gameplay
while True:
    FPS_clock.tick(60)  # 30 frames per second
    for event in pygame.event.get():

        # If exit pygame, end program.
        if event.type == QUIT:
            print()
            print("Game has ended")
            exit()

        # Defining Star Fonts
        producing = star_count_font.render(str(stars_per_second) + " stars per second", False, white)
        level = star_count_font.render("STAR LEVEL = " + str(star_level), False, white)

        # Displays background image
        screen.blit(star_background, (0, 0))

        # Click mechanics of Sun
        if event.type == MOUSEBUTTONDOWN and sun.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)  # Changes Cursor if clicked
            click()  # Click sound effect
            stars += star_level  # Every click gives [star_level] stars
            screen.blit(sun_if_clicked, (25, 25))

            # Displays the text [+(star_level) stars]
            star_adder = click_font.render("+" + str(star_level) + " STARS", False, white)
            screen.blit(star_adder, (120, 35))

            if stars >= star_barrier*star_level:
                star_level += 1  # Star level increases by 1 exponentially, so does clicking
                star_barrier += 25  # Star barrier regularly increases by half the regular amount
        else:
            screen.blit(sun, (25, 25))
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
    star_display = star_count_font.render("TOTAL STARS = " + str(stars), False, white)
    screen.blit(star_display, (330, 155))
    screen.blit(level, (330, 205))
    screen.blit(producing, (90, 355))

    # Adds Stars to Total
    star_counter = 0
    star_counter += 1
    if star_counter == 1:
        stars += stars_per_second/60
    stars = round(stars, 3)

    # Price Button Side Variables
    Purchase_border = pygame.Rect(925, 0, 25, 810)
    Inner_border = pygame.Rect(930, 0, 15, 810)
    Middle_border = pygame.Rect(935, 0, 5, 810)
    pygame.draw.rect(screen, white, Purchase_border)
    pygame.draw.rect(screen, (127, 127, 127), Inner_border)
    pygame.draw.rect(screen, black, Middle_border)
    purchase1 = pygame.Rect(950, 0, 200, 90)
    purchase2 = pygame.Rect(950, 90, 200, 90)
    purchase3 = pygame.Rect(950, 180, 200, 90)
    purchase4 = pygame.Rect(950, 270, 200, 90)
    purchase5 = pygame.Rect(950, 360, 200, 90)
    purchase6 = pygame.Rect(950, 450, 200, 90)
    purchase7 = pygame.Rect(950, 540, 200, 90)
    purchase8 = pygame.Rect(950, 630, 200, 90)
    purchase9 = pygame.Rect(950, 720, 200, 90)
    purchase_rect_list = [purchase1, purchase2, purchase3, purchase4, purchase5, purchase6, purchase7, purchase8, purchase9]
    mouse = pygame.mouse.get_pos()

    # Info Variables
    brown_info = info_font.render("A weak brown dwarf, produces 0.1 stars per second. (" + str(amount_list[0]) + "). Costs " + str(round(cost_list[0])) + " stars.", False, green)
    red_info = info_font.render("A somewhat stronger red dwarf, produces 1 star per second. (" + str(amount_list[1]) + ") Costs " + str(round(cost_list[1])) + " stars.", False, green)
    neutron_info = info_font.render("A more powerful neutron star, producing 8 stars per second. (" + str(amount_list[2]) + ") Costs " + str(round(cost_list[2])) + " stars.", False, green)
    regular_info = info_font.render("A regular star, produces 47 stars per second. (" + str(amount_list[3]) + ") Costs " + str(round(cost_list[3])) + " stars.", False, green)
    giant_info = info_font.render("A red giant, much larger than a star, 260 stars per second. (" + str(amount_list[4]) + ") Costs " + str(round(cost_list[4])) + " stars.", False, green)
    supergiant_info = info_font.render("A massive supergiant! 1400 stars per second. (" + str(amount_list[5]) + ") Costs " + str(round(cost_list[5])) + " stars.", False, green)
    nebula_info = info_font.render("The mother of all stars, makes 7800 stars per second. (" + str(amount_list[6]) + ") Costs " + str(round(cost_list[6])) + " stars.", False, green)
    foam_info = info_font.render("Can build stars at the Quantum level, makes 44000 stars per second. (" + str(amount_list[7]) + ") Costs " + str(round(cost_list[7])) + " stars.", False, green)
    bang_info = info_font.render("God Emperor of all stars, makes 260000 stars per second. (" + str(amount_list[8]) + ") Costs " + str(round(cost_list[8])) + " stars.", False, green)
    description_list = [brown_info, red_info, neutron_info, regular_info, giant_info, supergiant_info, nebula_info,foam_info, bang_info]

    # Info and Display
    for i in range(len(star_producers)):
        pygame.draw.rect(screen, black, purchase_rect_list[i])  # Draws infra-rectangles to register hovering
    for i in range(len(star_producers)):
        screen.blit(star_producers[i], (950, i*90))  # Displays the images for purchases
        if purchase_rect_list[i].collidepoint(mouse):
            screen.blit(description_list[i], (15, 780))  # Displays the corresponding description if mouse hovering
            pygame.draw.rect(screen, yellow, (950, i*90, 200, 90), 6, border_radius=5)  # Adds yellow border around picture

        # If mouse hovering and clicks and enough stars
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars >= cost_list[i]:
            mouse_click_counter += 1
            purchase_success = purchase_font.render('SUCCESS', True, green)  # Purchase Success
            if mouse_click_counter >= 5:
                purchase_success()
                stars -= round(cost_list[i])  # Subtract the cost from total stars
                stars_per_second += stars_made_per_unit[i]  # Add more to stars per second
                cost_list[i] *= 1.15  # The cost goes up by 15%
                amount_list[i] += 1 # The amount of that unit goes up by 1
                screen.blit(purchase_success, (970, 90 * i + 5))  # Displays success text
                mouse_click_counter = 0
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars < cost_list[i]:
            purchase_fail()
            bad_font = pygame.font.SysFont("Impact", 35)
            purchase_fail = bad_font.render('NOT ENOUGH', True, white)
            screen.blit(purchase_fail, (960, 90*i+5))
    if amount_list[0] == 3:
        stars_per_second = 0.3

    # Rounding Decimals
    if stars_per_second >= 1:
        stars_per_second = round(stars_per_second, 2)
    elif stars_per_second < 1:
        stars_per_second = round(stars_per_second, 3)

    pygame.display.update()  # Updates Screen

    # Refresh Screen After Update
    screen.blit(star_background, (0, 0))
    screen.blit(sun, (25, 25))
    screen.blit(star_display, (330, 155))
    screen.blit(level, (330, 205))
    screen.blit(producing, (90, 355))
    pygame.draw.rect(screen, white, Purchase_border)
    pygame.draw.rect(screen, (127, 127, 127), Inner_border)
    pygame.draw.rect(screen, black, Middle_border)
