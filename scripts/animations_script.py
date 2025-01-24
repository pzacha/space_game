from math import cos, pi, sin, sqrt

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)


def circle(progress):
    # Middle coords + radius * cos(t) where t = 2*pi*progress
    return (
        WIDTH // 2 + WIDTH // 4 * cos(2 * pi * progress),
        HEIGHT // 2 + HEIGHT // 4 * sin(2 * pi * progress),
    )


def eight(progress):
    return (
        WIDTH // 2 + WIDTH // 4 * sin(4 * pi * progress),
        HEIGHT // 2 + HEIGHT // 4 * cos(2 * pi * progress),
    )


### DRAW CIRCLE


# POINTS = 10000
# for it in range(POINTS):
#     progress = it / POINTS
#     pygame.draw.circle(
#         screen,
#         WHITE,
#         circle(progress),
#         radius=1,
#     )

# while True:
#     pygame.display.flip()


### ANIMATION


FPS = 60
DURATION = 3
FRAMES = FPS * DURATION  # 90
# clock = pygame.time.Clock()


# frame = 0
# while frame <= FRAMES:
#     clock.tick(FPS)

#     # Draw density NEW points per frame.
#     density = 1
#     for i in range(density):
#         progress = frame / FRAMES + i / density / FRAMES
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             circle(progress),  # eight
#             radius=1,
#         )

#     frame += 1
#     pygame.display.flip()


### Morphing


# def morph(fig1, fig2, progress, alpha):
#     x1, y1 = fig1(progress)
#     x2, y2 = fig2(progress)
#     return (
#         x1 + (x2 - x1) * alpha,
#         y1 + (y2 - y1) * alpha,
#     )


# frame = 0
# while frame <= FRAMES:
#     clock.tick(FPS)

#     screen.fill(BLACK)  # Clear previous drawing.

#     alpha = frame / FRAMES
#     # Draw 1000 points over the morphed figure.
#     for i in range(1000):
#         progress = i / 1000
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             morph(circle, eight, progress, alpha),  # <<<
#             radius=1,
#         )

#     frame += 1
#     pygame.display.flip()


#####################################################################################################
### More figures


### DRAW a/b


def figure(progress, a, b):
    return (
        400 + (a - b) * cos(2 * pi * progress) + b * cos(((a - b) / b) * 2 * pi * progress),
        400 + (a - b) * sin(2 * pi * progress) - b * sin(((a - b) / b) * 2 * pi * progress),
    )


a = pi
b = 1
r = 100  # radius
T = 30  # Number of full rotations


# POINTS = 100000
# for i in range(POINTS):
#     progress = i * T / POINTS
#     pygame.draw.circle(
#         screen,
#         WHITE,
#         figure(progress, r * a, r * b),
#         radius=1,
#     )
# while True:
#     pygame.display.flip()

### ANIMATION a/b


# FPS = 60
# ROTATION_DURATION = 1
# FRAMES = FPS * ROTATION_DURATION

# clock = pygame.time.Clock()
# frame = 0

# while frame <= T * FRAMES:
#     clock.tick(FPS)

#     # Draw 50 points per frame.
#     for i in range(50):
#         progress = frame / FRAMES + i / 50 / FRAMES
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             figure(progress, a * r, b * r),
#             radius=1,
#         )

#     frame += 1
#     pygame.display.flip()


### MORPH a/b


# def morph_figure(progress, a, b):
#     progress = progress * 50
#     return figure(progress, a, b)


# def morph(fig1, fig2, progress, alpha, a=pi, b=1, r=100):
#     x1, y1 = fig1(progress, a * r, b * r)
#     x2, y2 = fig2(progress)
#     return (
#         x1 + (x2 - x1) * alpha,
#         y1 + (y2 - y1) * alpha,
#     )


# FPS = 60
# DURATION = 10
# FRAMES = FPS * DURATION

# clock = pygame.time.Clock()
# frame = 0


# while frame <= FRAMES:
#     clock.tick(FPS)

#     screen.fill(BLACK)  # Clear previous drawing.

#     alpha = frame / FRAMES
#     # Draw 10000 points over the morphed figure.
#     for i in range(10000):
#         progress = i / 10000
#         pygame.draw.circle(
#             screen,
#             WHITE,
#             morph(morph_figure, circle, progress, alpha, pi, 1),
#             radius=1,
#         )

#     frame += 1
#     pygame.display.flip()
