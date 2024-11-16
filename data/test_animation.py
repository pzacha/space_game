from math import cos, sin, pi
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)


# DRAW
###############################################################


# def figure(progress, a, b):
#     return (
#         400 + (a - b) * cos(2 * pi * progress) + b * cos(((a - b) / b) * 2 * pi * progress),
#         400 + (a - b) * sin(2 * pi * progress) - b * sin(((a - b) / b) * 2 * pi * progress),
#     )


# FPS = 60
# DURATION = 10
# FRAMES = FPS * DURATION
# number_of_360 = 100

# clock = pygame.time.Clock()
# frame = 0

# while frame <= number_of_360 * FRAMES:
#     clock.tick(FPS)

#     # Draw 50 NEW points per frame.
#     for i in range(50):
#         progress = frame / FRAMES + i / 50 / FRAMES
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             figure(progress, 314, 100),
#             radius=1,
#         )

#     frame += 1
#     pygame.display.flip()

# MORPH
###############################################################


def circle(progress):
    return (
        WIDTH // 2 + WIDTH // 4 * cos(2 * pi * progress),
        HEIGHT // 2 + HEIGHT // 4 * sin(2 * pi * progress),
    )


def eight(progress):
    return (
        WIDTH // 2 + WIDTH // 4 * sin(10 * pi * progress),
        HEIGHT // 2 + HEIGHT // 4 * cos(6 * pi * progress),
    )


def figure(progress, a, b):
    return (
        400 + (a - b) * cos(2 * pi * progress) + b * cos(((a - b) / b) * 2 * pi * progress),
        400 + (a - b) * sin(2 * pi * progress) - b * sin(((a - b) / b) * 2 * pi * progress),
    )


def morph_figure(progress, a, b):
    progress = progress * 50
    return figure(progress, a, b)


def morph(fig1, fig2, progress, alpha, a=None, b=None):
    if a and b:
        x1, y1 = fig1(progress, a, b)
    else:
        x1, y1 = fig1(progress)
    x2, y2 = fig2(progress)
    return (
        x1 + (x2 - x1) * alpha,
        y1 + (y2 - y1) * alpha,
    )


FPS = 60
DURATION = 3
FRAMES = FPS * DURATION

clock = pygame.time.Clock()
frame = 0


while frame <= FRAMES:
    clock.tick(FPS)

    screen.fill(BLACK)  # Clear previous drawing.

    alpha = frame / FRAMES
    # Draw 1000 points over the morphed figure.
    for i in range(1000):
        progress = i / 1000
        pygame.draw.circle(
            screen,
            WHITE,
            morph(morph_figure, circle, progress, alpha, 200, 63.7),
            radius=1,
        )

    frame += 1
    pygame.display.flip()
