"""Linear Rec 2020 color class."""
from __future__ import annotations
from ..cat import WHITES
from .srgb import sRGB
from .. import algebra as alg
from ..types import Vector

ALPHA = 1.09929682680944
BETA = 0.018053968510807
BETA45 = 0.018053968510807 * 4.5

RGB_TO_XYZ = [
    [0.6369580483012911, 0.14461690358620838, 0.1688809751641721],
    [0.262700212011267, 0.677998071518871, 0.05930171646986196],
    [4.994106574466074e-17, 0.028072693049087438, 1.060985057710791]
]

XYZ_TO_RGB = [
    [1.7166511879712683, -0.3556707837763925, -0.25336628137365985],
    [-0.666684351832489, 1.6164812366349388, 0.01576854581391115],
    [0.017639857445310783, -0.04277061325780852, 0.9421031212354738]
]


def lin_2020_to_xyz(rgb: Vector) -> Vector:
    """
    Convert an array of linear-light rec-2020 values to CIE XYZ using  D65.

    (no chromatic adaptation)
    http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    """

    return alg.dot(RGB_TO_XYZ, rgb, dims=alg.D2_D1)


def xyz_to_lin_2020(xyz: Vector) -> Vector:
    """Convert XYZ to linear-light rec-2020."""

    return alg.dot(XYZ_TO_RGB, xyz, dims=alg.D2_D1)


class Rec2020Linear(sRGB):
    """Linear Rec 2020 class."""

    BASE = "xyz-d65"
    NAME = "rec2020-linear"
    SERIALIZE = ('--rec2020-linear',)
    WHITE = WHITES['2deg']['D65']

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Linear Rec 2020."""

        return lin_2020_to_xyz(coords)

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Linear Rec 2020."""

        return xyz_to_lin_2020(coords)
