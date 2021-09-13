import math
class AngleCalc:

    """
    Bounds the provided angle between [-180, 180) degrees.
    Ex. 360 becomes 0, 270 becomes -90, -450 becomes -90.
    @param angle Input angle in degrees.
    @return The bounded angle in degrees.
    """
    def boundTo180(angle):
        while(angle >= 180):
            angle -= 360
        while angle < -180:
            angle += 360
        return angle

    """
    Determines whether |middle_angle| is in the acute angle between the other two bounding angles.
    Note: Input angles are bounded to 180 for safety.
    Ex. -180 is between -90 and 110 but not between -90 and 80.
    @param first_angle First angle in degrees.
    @param middle_angle Middle angle in degrees.
    @param second_angle Second angle in degrees.
    @return Whether |middle_angle| is between |first_angle| and |second_angle| (exclusive).
    """
    def isAngleBetween(first_angle, middle_angle, second_angle):
        min_clock = 0
        min_anticlock = 0
        clockwise = False
        if first_angle > second_angle:
            min_anticlock = math.fabs(first_angle) + math.fabs(second_angle)
            min_clock = 360 - min_anticlock
        elif second_angle > first_angle:
            min_clock = math.fabs(first_angle) + math.fabs(second_angle)
            min_anticlock = 360 - min_clock
        else:
            if first_angle == second_angle == middle_angle:
                return True
            else:
                return False

        if min_clock < min_anticlock:
            clockwise = True
        else:
            clockwise = False

        if not clockwise:
            if first_angle - min_anticlock<= middle_angle <= first_angle:
                return True
            else:
                return False
        else:
            if first_angle <= middle_angle <= first_angle + min_clock:
                return True
            else:
                return False
