import math

import pytest

from metalcutting import turning, material


def test_speed_round_trip():
    n = turning.spindle_speed(200, 100)
    assert n == pytest.approx(636.62, rel=1e-4)
    assert turning.cutting_speed(100, n) == pytest.approx(200)


def test_mrr():
    assert turning.metal_removal_rate(200, 3, 0.3) == pytest.approx(180)


def test_power_worked_example():
    hm = turning.chip_thickness(0.3, 95)
    kc = material.specific_cutting_force(1500, hm, 0.25, gamma0=6)
    assert hm == pytest.approx(0.29886, rel=1e-4)
    assert kc == pytest.approx(1906.4, rel=1e-3)
    assert turning.net_power(200, 3, 0.3, kc) == pytest.approx(5.72, rel=1e-3)


def test_power_equals_force_times_speed():
    # Pc [kW] = Fc [N] * vc [m/min] / 60 / 1000
    Fc = turning.cutting_force(3, 0.3, 2000)
    assert turning.net_power(200, 3, 0.3, 2000) == pytest.approx(Fc * 200 / 60 / 1000)


def test_machining_time():
    assert turning.machining_time(150, 0.3, 500) == pytest.approx(1.0)


def test_roughness_round_trip():
    fn = turning.feed_for_roughness_ra(1.6, 0.8)
    assert turning.surface_roughness_ra(fn, 0.8) == pytest.approx(1.6)
    # Ra is roughly a quarter of Rmax
    assert turning.surface_roughness_ra(0.2, 0.8) / turning.surface_roughness_rmax(0.2, 0.8) == pytest.approx(0.2566, rel=1e-3)


def test_feed_for_chip_thickness_round_trip():
    fn = turning.feed_for_chip_thickness(0.2, 45)
    assert turning.chip_thickness(fn, 45) == pytest.approx(0.2)


@pytest.mark.parametrize("args", [(0, 100), (100, 0), (-1, 100)])
def test_rejects_non_positive(args):
    with pytest.raises(ValueError):
        turning.cutting_speed(*args)


def test_rejects_bad_angle():
    with pytest.raises(ValueError):
        turning.chip_thickness(0.3, 0)
