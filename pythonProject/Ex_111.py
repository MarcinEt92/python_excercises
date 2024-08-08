"""
Kat miedzy wskazowkami zegara
12h
"""
import math


def calculate_angle(hour, minute):
    if hour > 12:
        hour -= 12
    minute_angle = minute / 60 * 360
    hour_angle = hour / 12 * 360 + minute / 60 * 30
    return math.fabs(minute_angle - hour_angle)


def answer():
    hour = 18
    minute = 17
    print(f"Angle at {hour}:{minute} is: {calculate_angle(hour, minute)}")


if __name__ == "__main__":
    answer()
