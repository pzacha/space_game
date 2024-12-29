from math import cos, sin, pi
import pygame as pg


def sun_animation(progress, x, y, r, ratio=pi):
    """
    Calculate the position of a point on a specific sun animation path.

    Args:
        progress (float): The progress of the animation, typically between 0 and 1.
        x (float): The x-coordinate of the center of the sun.
        y (float): The y-coordinate of the center of the sun.
        r (float): The radius of the sun.
        ratio (float): The ratio used in the animation calculation.

    Returns:
        tuple: A tuple containing the x and y coordinates of the point on the sun's path.
    """
    return (
        x
        + (r - r / ratio) * cos(2 * pi * progress)
        + r / ratio * cos(((r - r / ratio) / r / ratio) * 2 * pi * progress),
        y
        + (r - r / ratio) * sin(2 * pi * progress)
        - r / ratio * sin(((r - r / ratio) / r / ratio) * 2 * pi * progress),
    )


def draw_sun(window, color, pos, r, timestamp, animation_ratio):
    """
    Draws an animated sun on the given window.

    Args:
        window (pygame.Surface): The surface on which to draw the sun.
        color (tuple): The color of the sun, represented as an RGB tuple.
        pos (tuple): The position of the sun's center, represented as an (x, y) tuple.
        r (int): The radius of the sun.
        timestamp (int): The current timestamp, used for animation progression.
        animation_ratio: Ratio used in a function that calculates the position of animated points.
            This function should take five arguments: progress (float), x (int), y (int), radius (int) and ratio.
    """
    POINTS = 2000

    # parameter for animation density
    if animation_ratio < 2:
        x = 35
    elif animation_ratio < 3:
        x = 25
    elif animation_ratio < 4:
        x = 15
    else:
        x = 10

    pg.draw.circle(
        window,
        color,
        pos,
        radius=r + 1,
        width=1,
    )
    for it in range(POINTS):
        progress = timestamp / 100 + x * it / POINTS
        pg.draw.circle(
            window,
            color,
            sun_animation(progress, pos[0], pos[1], r, animation_ratio),
            radius=1,
        )


def draw_collision(game, obj):
    def _circle(progress, x, y, r):
        return (
            x + r * cos(2 * pi * progress),
            y + r * sin(2 * pi * progress),
        )

    def _figure(progress, x, y, r, ratio):
        a = r
        b = r / ratio
        return (
            x + (a - b) * cos(2 * pi * progress) + b * cos(((a - b) / b) * 2 * pi * progress),
            y + (a - b) * sin(2 * pi * progress) - b * sin(((a - b) / b) * 2 * pi * progress),
        )

    def _morph_figure(progress, x, y, r, ratio=pi):
        progress = progress * 50
        return _figure(progress, x, y, r, ratio)

    def _morph(progress, alpha, r, pos):
        x1, y1 = _morph_figure(progress, x=pos[0], y=pos[1], r=r)
        x2, y2 = _circle(progress, x=pos[0], y=pos[1], r=r)
        return (
            x1 + (x2 - x1) * alpha,
            y1 + (y2 - y1) * alpha,
        )

    frame = game.timestamp - obj.collision_time
    frames = game.fps * 3
    alpha = frame / frames
    if alpha < 0.5:
        radius = obj.radius * 2
    else:
        radius = obj.radius * (1 / alpha)

    # Draw 1000 points over the morphed figure.
    for i in range(1000):
        progress = i / 1000
        pg.draw.circle(
            game.window,
            obj.color,
            _morph(progress, alpha, radius, obj.game_pos),
            radius=1,
        )

    pg.draw.circle(game.window, obj.color, obj.game_pos, radius=obj.radius * alpha)

    if frame == frames:
        obj.collision_time = None
