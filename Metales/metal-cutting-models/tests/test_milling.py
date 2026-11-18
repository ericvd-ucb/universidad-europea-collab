import math

import numpy as np
import pytest

from metalcutting import milling


def numeric_avg_side(fz, ae, D):
    """Average of fz*sin(phi) over the engaged arc for side milling."""
    phi_e = math.acos(1 - 2 * ae / D)
    phi = np.linspace(0, phi_e, 200001)
    return float(np.mean(fz * np.sin(phi)))


def numeric_avg_face_centred(fz, ae, D):
    theta = math.asin(ae / D)
    phi = np.linspace(math.pi / 2 - theta, math.pi / 2 + theta, 200001)
    return float(np.mean(fz * np.sin(phi)))


def test_kinematics():
    n = milling.spindle_speed(220, 80)
    assert n == pytest.approx(875.35, rel=1e-4)
    vf = milling.table_feed(0.15, n, 6)
    assert milling.feed_per_tooth(vf, n, 6) == pytest.approx(0.15)
    assert milling.feed_per_revolution(vf, n) == pytest.approx(0.9)


@pytest.mark.parametrize("ae", [2, 8, 20, 30, 40])
def test_side_hm_matches_numeric_average(ae):
    assert milling.avg_chip_thickness_side(0.1, ae, 40) == pytest.approx(
        numeric_avg_side(0.1, ae, 40), rel=1e-4)


@pytest.mark.parametrize("ae", [10, 50, 100, 125])
def test_face_hm_matches_numeric_average(ae):
    assert milling.avg_chip_thickness_face_centred(0.2, ae, 125) == pytest.approx(
        numeric_avg_face_centred(0.2, ae, 125), rel=1e-4)


def test_full_slot_hm_is_2_over_pi():
    expected = 2 * 0.1 / math.pi
    assert milling.avg_chip_thickness_side(0.1, 40, 40) == pytest.approx(expected)
    assert milling.avg_chip_thickness_face_centred(0.1, 40, 40) == pytest.approx(expected)


def test_small_engagement_approximation_close():
    exact = milling.avg_chip_thickness_side(0.1, 2, 40)
    approx = milling.avg_chip_thickness_side_approx(0.1, 2, 40)
    assert approx == pytest.approx(exact, rel=0.03)


def test_hex_side_and_compensation():
    hex_ = milling.max_chip_thickness_side(0.1, 8, 40)
    assert hex_ == pytest.approx(0.08)
    assert milling.max_chip_thickness_side(0.1, 25, 40) == pytest.approx(0.1)
    fz = milling.feed_for_max_chip_thickness_side(0.1, 8, 40)
    assert fz == pytest.approx(0.125)


def test_power_torque():
    Pc = milling.net_power(3, 100, 1000, 1500)
    assert Pc == pytest.approx(7.5)
    # P = M * omega
    n = 500
    assert milling.torque(Pc, n) * 2 * math.pi * n / 60 / 1000 == pytest.approx(Pc)


def test_engagement_larger_than_cutter_rejected():
    with pytest.raises(ValueError):
        milling.avg_chip_thickness_side(0.1, 50, 40)
