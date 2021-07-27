# Imports
import pygame
from pygame.locals import *
from pygame import mixer

# Inputs and Beginning
input("\033[1;32mSet Sound Volume to 10 for best sound effects. ")
input("\033[1;32mWelcome to \033[1;33mStar Clicker\033[1;32m\nIn this game, your goal is to make as many stars as possible. Pres\nYou can make endless stars! Hover over a unit for info.\nClick the giant sun to make 1 star.\nas you click more, your levels will incrase, with each one doubling the amount of stars you make per click.\nYou also will have units, but them at the right side of th screen. \nUnits make a certain amount of stars each second.\nThe cost of buying more star units will go up every time you buy one. \nHave fun! ")
music_type = eval(input("Music type (1), (2), or (3): "))

# Key Variables and Initialization
pygame.init()
title = "Star Clicker"
FPS_clock = pygame.time.Clock()
red = (255, 0, 0),
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
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

# If_clicked Images
sun_if_clicked = pygame.transform.scale(sun, (325, 325))

# Tech Variables
stars = 0
star_level = 1
star_barrier = 50
stars_per_second = 0
counter_for_stars = 0
click_font = pygame.font.SysFont('Calibri', 30)
star_count_font = pygame.font.SysFont("Impact", 40)
purchase_font = pygame.font.SysFont("Impact", 40)
display_font = pygame.font.SysFont("Impact", 40)
info_font = pygame.font.SysFont("Calibri", 24, bold=True)
amount_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
star_producers = [brown, red, neutron, regular, giant, supergiant, nebula, foam, bang]
stars_made_per_unit = [0.25, 1, 8, 47, 260, 1400, 7800, 44000, 260000]
cost_list = [15, 100, 1500, 8000, 20000, 150000, 1000000, 2500000, 10000000]



# Background Music Function
def music():
    mixer.init()
    if music_type == 1:
        pygame.mixer.music.load('Battle Cats BGM - Main Theme.mp3')
        pygame.mixer.music.play(-1)
    elif music_type == 2:
        pygame.mixer.music.load('Battle Cats BGM - Uphill Battle.mp3')
        pygame.mixer.music.play(-1)
    elif music_type == 3:
        pygame.mixer.music.load('Battle Cats BGM - Boss Battle Theme.mp3')
        pygame.mixer.music.play(-1)


# Background Music
music()

# Screen part
while True:
    FPS_clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        producing = star_count_font.render(str(stars_per_second) + " stars per second", False, white)
        level = star_count_font.render("STAR LEVEL = " + str(star_level), False, white)
        screen.blit(star_background, (0, 0))

    # Click mechanics
        if event.type == MOUSEBUTTONDOWN and sun.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            stars += star_level
            screen.blit(sun_if_clicked, (25, 25))
            star_adder = click_font.render("+" + str(star_level) + " STARS", False, white)
            if stars >= star_barrier*star_level:
                star_level += 1
                star_barrier += 40
            screen.blit(star_adder, (120, 35))
        else:
            screen.blit(sun, (25, 25))
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
    star_display = star_count_font.render("TOTAL STARS = " + str(stars), False, white)
    counter_for_stars += 1
    if counter_for_stars == 1:
        stars += stars_per_second/30
        counter_for_stars = 0
    screen.blit(star_display, (340, 155))
    screen.blit(level, (340, 205))
    screen.blit(producing, (100, 365))

    # Price Button Side
    Purchase_border = pygame.Rect(925, 0, 25, 810)
    Inner_border = pygame.Rect(930, 0, 15, 810)
    Middle_border = pygame.Rect(935, 0, 5, 810)
    pygame.draw.rect(screen, (255, 255, 255), Purchase_border)
    pygame.draw.rect(screen, (127, 127, 127), Inner_border)
    pygame.draw.rect(screen, (0, 0, 0), Middle_border)
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
    brown_info = info_font.render("A weak brown dwarf, produces 0.25 stars per second. (" + str(amount_list[0]) + "). Costs " + str(round(cost_list[0])) + " stars.", False, green)
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
        pygame.draw.rect(screen, (0, 0, 0), purchase_rect_list[i])
    for i in range(len(star_producers)):
        screen.blit(star_producers[i], (950, i*90))
        if purchase_rect_list[i].collidepoint(mouse):
            screen.blit(description_list[i], (15, 780))
            pygame.draw.rect(screen, yellow, (950, i*90, 200, 90), 6, border_radius=5)
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars >= cost_list[i]:
            purchase_success = purchase_font.render('SUCCESS', True, green)
            screen.blit(purchase_success, (970, 90*i+5))
            stars -= round(cost_list[i])
            stars_per_second += stars_made_per_unit[i]
            cost_list[i] *= 1.25
            amount_list[i] += 1
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars < cost_list[i]:
            bad_font = pygame.font.SysFont("Impact", 35)
            purchase_fail = bad_font.render('NOT ENOUGH', True, (255, 255, 255))
            screen.blit(purchase_fail, (960, 90*i+5))

    # Rounding Decimals
    if stars_per_second >= 1:
        round(stars_per_second)
    elif 0 < stars_per_second < 1:
        round(stars_per_second, 3)

    # Adding stars to total
    stars = round(stars, 3)
    star_adder = click_font.render("+" + str(star_level) + " STARS", False, white)
    pygame.display.update()

    # Refresh Screen after update
    screen.blit(star_background, (0, 0))
    if event.type == MOUSEBUTTONDOWN and sun.get_rect().collidepoint(pygame.mouse.get_pos()):
        screen.blit(star_adder, (120, 35))
        screen.blit(sun_if_clicked, (25, 25))
    else:
        screen.blit(sun, (25, 25))
        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
    star_display = star_count_font.render("TOTAL STARS = " + str(stars), False, white)
    screen.blit(star_display, (340, 155))
    screen.blit(level, (340, 205))
    screen.blit(producing, (100, 365))
    pygame.draw.rect(screen, (255, 255, 255), Purchase_border)
    pygame.draw.rect(screen, (127, 127, 127), Inner_border)
    pygame.draw.rect(screen, (0, 0, 0), Middle_border)
    for i in range(len(star_producers)):
        pygame.draw.rect(screen, (0, 0, 0), purchase_rect_list[i])
    for i in range(len(star_producers)):
        screen.blit(star_producers[i], (950, i*90))
        if purchase_rect_list[i].collidepoint(mouse):
            screen.blit(description_list[i], (15, 780))
            pygame.draw.rect(screen, yellow, (950, i*90, 200, 90), 6, border_radius=5)
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars >= cost_list[i]:
            purchase_success = purchase_font.render('SUCCESS', True, green)
            screen.blit(purchase_success, (970, 90*i+5))
            stars -= round(cost_list[i])
            stars_per_second += stars_made_per_unit[i]
            cost_list[i] *= 1.25
            amount_list[i] += 1
        if purchase_rect_list[i].collidepoint(mouse) and pygame.mouse.get_pressed()[0] and stars < cost_list[i]:
            bad_font = pygame.font.SysFont("Impact", 35)
            purchase_fail = bad_font.render('NOT ENOUGH', True, (255, 255, 255))
            screen.blit(purchase_fail, (960, 90*i+5))

