import math

import pytest

from metalcutting import drilling, tool_life


def test_drilling_mrr_is_hole_area_times_feed():
    Dc, vc, fn = 20, 120, 0.25
    n = drilling.spindle_speed(vc, Dc)
    vf = drilling.penetration_rate(fn, n)
    area = math.pi * Dc**2 / 4                    # mm^2
    assert drilling.metal_removal_rate(vc, Dc, fn) == pytest.approx(area * vf / 1000)


def test_drilling_power_from_torque():
    # Two edges, each removing (Dc/2)*(fn/2), force acting at radius Dc/4
    Dc, vc, fn, kc = 20, 120, 0.25, 2000
    n = drilling.spindle_speed(vc, Dc)
    M_Nmm = 2 * kc * (Dc / 2) * (fn / 2) * (Dc / 4)
    P_kW = M_Nmm / 1000 * 2 * math.pi * n / 60 / 1000
    assert drilling.net_power(fn, vc, Dc, kc) == pytest.approx(P_kW)
    Pc = drilling.net_power(fn, vc, Dc, kc)
    assert drilling.torque(Pc, n) == pytest.approx(M_Nmm / 1000)


def test_drilling_chip_thickness():
    assert drilling.chip_thickness(0.25, 90) == pytest.approx(0.125)


def test_taylor_fit_round_trip():
    n, C = tool_life.fit_taylor(200, 25, 300, 8)
    assert tool_life.tool_life(200, C, n) == pytest.approx(25)
    assert tool_life.tool_life(300, C, n) == pytest.approx(8)
    assert tool_life.speed_for_tool_life(25, C, n) == pytest.approx(200)


def test_economic_tool_life():
    assert tool_life.economic_tool_life(0.25, 2, 4, 2) == pytest.approx(12)
    assert tool_life.max_production_tool_life(0.25, 2) == pytest.approx(6)


def test_economic_tool_life_minimises_cost():
    # Numerically check that T_econ is the minimum of cost per part
    n, C, lm_vf_const = 0.25, 600, 2000.0   # Tc = k / vc
    t_ct, C_t, M = 2, 4, 2

    def cost(vc):
        T = tool_life.tool_life(vc, C, n)
        return tool_life.cost_per_part(lm_vf_const / vc, T, t_ct, C_t, M)

    T_e = tool_life.economic_tool_life(n, t_ct, C_t, M)
    v_e = tool_life.speed_for_tool_life(T_e, C, n)
    assert cost(v_e) < cost(v_e * 0.95)
    assert cost(v_e) < cost(v_e * 1.05)
