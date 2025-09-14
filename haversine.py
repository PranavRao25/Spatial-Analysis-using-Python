import numpy as np

RADIUS_EARTH = 6.3781e+6

def haversine(point1, point2):
    """
    Returns the spherical distance between two points in metres
    using their coordinates by the haversine method

    :param point1: pair of latitude & longitude of the point
    :param point2: pair of latitude & longitude of the point
    :returns: distance between the points in metres
    """
    lat1, long1 = point1
    lat2, long2 = point2
    del_lat, del_long = lat2 - lat1, long2 - long1
    return 2 * RADIUS_EARTH * np.arcsin(
        np.sqrt(
            (1 - np.cos(del_lat) + np.cos(lat1) * np.cos(lat2) * (1 - np.cos(del_long))) / 2
        )
    )
