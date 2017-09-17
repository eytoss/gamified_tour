import math

# ref. http://developer.estimote.com/indoor/ios-tutorial/
ACCURACY_DEF = {
    "veryHigh": 1,
    "high": 1.62,
    "medium": 2.62,
    "low": 4.24,
    "verylow": 50,
    "unknown": None
}

def get_distance_range(x_1, y_1, x_2, y_2, accuracy):
    """
    based on accuracy level of the detected postion
    return (distance, lower_bound, upper_bound)
    """
    distance = _get_distance(x_1, y_1, x_2, y_2)
    dist_delta = ACCURACY_DEF[accuracy]
    return (distance, max(distance-dist_delta, 0), distance+dist_delta)

def _get_distance(x_1, y_1, x_2, y_2):
    """
    return distance between two points
    TODO: potential improvement
        return orientation info:
        For example orientation=0 means (x_1, y_1) is to the north of (x_2, y_2)
    """
    return math.sqrt(math.pow(abs(x_2-x_1), 2) + math.pow(abs(y_2-y_1), 2))

