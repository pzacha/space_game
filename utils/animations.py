from math import cos, sin, pi
import pygame


def circle(progress, x, y, r):
    return (
        x + r * cos(2 * pi * progress),
        y + r * sin(2 * pi * progress),
    )


def draw_sun(progress, x, y, r):
    return (
        x + (r - r / pi) * cos(2 * pi * progress) + r / pi * cos(((r - r / pi) / r / pi) * 2 * pi * progress),
        y + (r - r / pi) * sin(2 * pi * progress) - r / pi * sin(((r - r / pi) / r / pi) * 2 * pi * progress),
    )


def morph_figure(progress, a, b):
    progress = progress * 50
    return draw_sun(progress, a, b)


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


def draw_sun(window, color, pos, r):
    x = int(pos[0])
    y = int(pos[1])
    POINTS = 20000
    pygame.draw.circle(
        window,
        color,
        pos,
        radius=r,
        width=4,
    )
    for it in range(POINTS):
        progress = 50 * it / POINTS
        pygame.draw.circle(
            window,
            color,
            draw_sun(progress, x, y, r),
            radius=1,
        )


# # SUN ANIMATION
# ##########################################
# starting_progress = 50
# clock = pygame.time.Clock()
# POINTS = 20000
# for it in range(POINTS):
#     progress = starting_progress * it / POINTS
#     pygame.draw.circle(
#         screen,
#         WHITE,
#         figure(progress, 200, 63.7),
#         radius=1,
#     )
#     pygame.draw.circle(
#         screen,
#         WHITE,
#         (400, 400),
#         radius=205,
#         width=4,
#     )

# for it in range(POINTS):
#     progress = starting_progress + 100 * it / POINTS

#     pygame.draw.circle(
#         screen,
#         WHITE,
#         figure(progress, 200, 63.7),
#         radius=1,
#     )
#     if it % 100 == 0:
#         clock.tick(60)
#         pygame.display.flip()
# ##########################################
