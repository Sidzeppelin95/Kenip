"""Reusable geometry helpers for SVG diagrams."""
from math import cos, pi, sin
def radial_points(cx, cy, radius, count, start_angle=-pi/2):
    if count < 1: return []
    return [(cx + radius*cos(start_angle + 2*pi*i/count), cy + radius*sin(start_angle + 2*pi*i/count)) for i in range(count)]
def polyline(points): return " ".join(f"{x:.1f},{y:.1f}" for x,y in points)
