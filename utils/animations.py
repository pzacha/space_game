from math import cos, sin, pi
import pygame


def circle(progress, x, y, r):
    return (
        x + r * cos(2 * pi * progress),
        y + r * sin(2 * pi * progress),
    )


def sun_1(progress, x, y, r):
    ratio = pi
    return (
        x + (r - r / ratio) * cos(2 * pi * progress) + r / ratio * cos(((r - r / ratio) / r / ratio) * 2 * pi * progress),
        y + (r - r / ratio) * sin(2 * pi * progress) - r / ratio * sin(((r - r / ratio) / r / ratio) * 2 * pi * progress),
    )


def morph_figure(progress, a, b):
    progress = progress * 50
    return sun_1(progress, a, b)


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


def draw_sun(window, color, pos, r, timestamp):
    POINTS = 2000
    pygame.draw.circle(
        window,
        color,
        pos,
        radius=r + 1,
        width=1,
    )
    for it in range(POINTS):
        progress = timestamp / 100 + 13 * it / POINTS
        pygame.draw.circle(
            window,
            color,
            sun_1(progress, pos[0], pos[1], r),
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
