from __future__ import annotations

from typing import overload, Literal
from acryo.tilt._single import SingleAxisY, SingleAxisX, SingleAxis
from acryo.tilt._base import UnionAxes, NoWedge


@overload
def single_axis(
    tilt_range: tuple[float, float], axis: Literal["x", "y"] = "y"
) -> SingleAxis:
    ...


@overload
def single_axis(tilt_range: None, axis: Literal["x", "y"] = "y") -> NoWedge:
    ...


def single_axis(
    tilt_range: tuple[float, float] | None = None,
    axis: Literal["x", "y"] = "y",
) -> SingleAxis | NoWedge:
    """
    Create a single-axis missing wedge model.

    Parameters
    ----------
    tilt_range : (float, float)
        Minimum and maximum tilt angles in degrees.
    axis : str, default is "y"
        The rotation axis of tomography.
    """
    if tilt_range is None:
        return NoWedge()
    if axis == "y":
        return SingleAxisY(tilt_range)
    elif axis == "x":
        return SingleAxisX(tilt_range)
    else:
        raise ValueError(f"Invalid axis: {axis}")


def dual_axis(
    tilt_range_y: tuple[float, float],
    tilt_range_x: tuple[float, float],
) -> UnionAxes:
    """
    Create a dual-axis missing wedge model.

    Parameters
    ----------
    tilt_range_y : (float, float)
        Minimum and maximum tilt angles of the y-axis tilt series in degrees.
    tilt_range_x : (float, float)
        Minimum and maximum tilt angles of the x-axis tilt series in degrees.
    """
    return UnionAxes(
        [
            SingleAxisY(tilt_range_y),
            SingleAxisX(tilt_range_x),
        ]
    )


def no_wedge() -> NoWedge:
    """Create a no-wedge missing wedge model."""
    return NoWedge()
