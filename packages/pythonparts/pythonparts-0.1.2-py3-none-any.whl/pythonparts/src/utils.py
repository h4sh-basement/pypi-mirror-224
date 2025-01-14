import math

from typing import Optional

import NemAll_Python_Geometry as AllplanGeo    # type: ignore

from .config import TOLERANCE


def child_global_coords_calc(concov, global_, child_space):
    """
    The function calculates the global coordinates of a child space based on the given parameters.
    
    :param concov: The parameter "concov" is likely an object or structure that represents the
    coordinates of a bounding box or volume. It may contain properties such as "left", "right", "front",
    "back", "bottom", and "top" which define the boundaries of the volume
    :param global_: The "global_" parameter is an object that represents the global coordinate system.
    It contains information about the start and end points of the global coordinate system in three
    dimensions (X, Y, Z)
    :param child_space: The child_space parameter represents the dimensions of a child space or object.
    It contains the width, length, and height of the child space
    :return: the child global start point and the child global end point as AllplanGeo.Point3D objects.
    """
    start_X, end_X = __coords_calc_axis(concov.left, 
                                        concov.right, 
                                        global_.start_point.X, 
                                        global_.end_point.X,
                                        child_space.width,)
    
    start_Y, end_Y = __coords_calc_axis(concov.front, 
                                        concov.back, 
                                        global_.start_point.Y, 
                                        global_.end_point.Y,
                                        child_space.length,)

    start_Z, end_Z = __coords_calc_axis(concov.bottom,
                                        concov.top, 
                                        global_.start_point.Z, 
                                        global_.end_point.Z,
                                        child_space.height,)
    
    child_global_start_pnt = AllplanGeo.Point3D(start_X, start_Y, start_Z)
    child_global_end_pnt   = AllplanGeo.Point3D(end_X, end_Y, end_Z)

    return child_global_start_pnt, child_global_end_pnt


def center_calc(concov, global_, child_space):
    """
    The function calculates the center position of a child space within a given global space along the
    X, Y, and Z axes.
    
    :param concov: The parameter "concov" seems to represent a bounding box or a region of interest. It
    has properties like "left", "right", "front", "back", "bottom", and "top" which define the
    boundaries of the region in different dimensions
    :param global_: The `global_` parameter represents the global coordinate system. It has a
    `start_point` and an `end_point` which define the range of the coordinate system along each axis (X,
    Y, and Z)
    :param child_space: The `child_space` parameter represents the dimensions of a child space or
    object. It has three properties: `width`, `length`, and `height`, which represent the width, length,
    and height of the child space respectively
    """
    yield __center_calc_axis(concov.left, 
                             concov.right, 
                             global_.start_point.X, 
                             global_.end_point.X,
                             child_space.width)
    
    yield __center_calc_axis(concov.front, 
                             concov.back, 
                             global_.start_point.Y, 
                             global_.end_point.Y,
                             child_space.length)

    yield __center_calc_axis(concov.bottom,
                             concov.top, 
                             global_.start_point.Z, 
                             global_.end_point.Z,
                             child_space.height)


def center_scene_calc(concov, child_space):
    """
    The function calculates the center position of a scene based on the dimensions of a child space.
    
    :param concov: The parameter "concov" is likely an object that represents the coverage or extent of
    a container or space. It may have properties such as "left", "front", and "bottom" that indicate the
    boundaries of the container in different dimensions
    :param child_space: The `child_space` parameter represents the dimensions of a child space or area.
    It has three attributes: `width`, `length`, and `height`, which represent the width, length, and
    height of the child space, respectively
    """
    yield -child_space.width/2. if concov.left is None else None
    yield -child_space.length/2. if concov.front is None else None
    yield -child_space.height/2. if concov.bottom is None else None


def equal_points(p1: Optional[AllplanGeo.Point3D], p2: Optional[AllplanGeo.Point3D]):
    """
    The function checks if two 3D points are equal within a given tolerance.
    
    :param p1: p1 is the first point, represented as an instance of the AllplanGeo.Point3D class. This
    class represents a point in three-dimensional space, with X, Y, and Z coordinates. The point is
    optional, meaning it can be None if no point is provided
    :type p1: Optional[AllplanGeo.Point3D]
    :param p2: The parameter `p2` is of type `Optional[AllplanGeo.Point3D]`, which means it can either
    be a `Point3D` object or `None`
    :type p2: Optional[AllplanGeo.Point3D]
    :return: a boolean value. It returns True if both points are equal or if both points are None. It
    returns False if only one of the points is None or if any of the coordinates of the points are not
    close enough within the specified tolerance.
    """
    if (p1 is None) and (p2 is None):
        return True
    if (p1 is None) or (p2 is None):
        return False
 
    return  (math.isclose(p1.X, p2.X, rel_tol=TOLERANCE, abs_tol=TOLERANCE)  
            and math.isclose(p1.Y, p2.Y, rel_tol=TOLERANCE, abs_tol=TOLERANCE)
            and math.isclose(p1.Z, p2.Z, rel_tol=TOLERANCE, abs_tol=TOLERANCE)
    )


def __coords_calc_axis(cc_start, cc_end, parent_global_start_point, parent_global_end_point, child_len):
    """
    The function calculates the global start and end points of a child object based on the start and end
    points of its parent object and the length of the child object.
    
    :param cc_start: The offset from the parent's global start point to the child's global start point.
    It is a positive value indicating how far the child's start point is from the parent's start point
    along the axis
    :param cc_end: The parameter "cc_end" represents the length of the child component that is connected
    to the parent component's end point
    :param parent_global_start_point: The starting point of the parent object in the global coordinate
    system
    :param parent_global_end_point: The parent_global_end_point is the end point of the parent object in
    the global coordinate system
    :param child_len: The length of the child object
    :return: the child global start point and child global end point.
    """
    if cc_start is not None:
        child_global_start_point = parent_global_start_point + cc_start
        child_global_end_point   = child_global_start_point + child_len
    elif cc_end is not None:
        child_global_end_point   = parent_global_end_point - cc_end
        child_global_start_point = child_global_end_point - child_len
    else:
        child_global_start_point = parent_global_start_point
        child_global_end_point   = child_global_start_point + child_len

    return child_global_start_point, child_global_end_point


def __center_calc_axis(cc_start, cc_end, parent_global_start_point, parent_global_end_point, child_len):
    """
    The function calculates the center position of a child object along a given axis within the parent
    object.
    
    :param cc_start: The starting point of the child component on the current axis
    :param cc_end: The cc_end parameter is the end point of the child component
    :param parent_global_start_point: The starting point of the parent object in the global coordinate
    system
    :param parent_global_end_point: The end point of the parent object in the global coordinate system
    :param child_len: The length of the child object
    :return: the value of `cc_start` if it is not `None` or `cc_end` is not `None`. Otherwise, it is
    calculating the shift needed to center the child object between the parent's global start and end
    points and returning that value.
    """
    if not (cc_start is None and cc_end is None):
        return cc_start
    parent_len = abs(parent_global_end_point - parent_global_start_point)
    shift = (parent_len - child_len) / 2.
    return shift


