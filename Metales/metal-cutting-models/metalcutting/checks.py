"""
Answer checking for the exercise notebook.

    from metalcutting.checks import check
    check("T1_n", my_answer)

Answers are accepted within 1 percent of the reference value.
"""

import math

from . import turning, milling, drilling, material, tool_life

REL_TOL = 0.01


def _answers():
    a = {}

    # E0: write your own spindle speed function (checked on Dm=50, vc=150)
    a["E0"] = turning.spindle_speed(150, 50)

    # T1
    a["T1_n"] = turning.spindle_speed(250, 80)

    # T2
    kc1, mc = material.get("P1 unalloyed steel")
    hm = turning.chip_thickness(0.35, 95)
    kc = material.specific_cutting_force(kc1, hm, mc, gamma0=6)
    a["T2_hm"], a["T2_kc"] = hm, kc
    a["T2_Pc"] = turning.net_power(180, 4, 0.35, kc)

    # T3
    hm = turning.chip_thickness(0.4, 95)
    kc = material.specific_cutting_force(kc1, hm, mc, gamma0=6)
    P_avail = 15 * 0.8
    a["T3_ap"] = P_avail * 60e3 / (200 * 0.4 * kc)

    # T4
    n = turning.spindle_speed(220, 60)
    a["T4_Tc"] = turning.machining_time(200, 0.25, n)

    # T5
    a["T5_fn08"] = turning.feed_for_roughness_ra(1.6, 0.8)
    a["T5_fn12"] = turning.feed_for_roughness_ra(1.6, 1.2)

    # M1
    n = milling.spindle_speed(220, 80)
    a["M1_n"] = n
    a["M1_vf"] = milling.table_feed(0.15, n, 6)

    # M2
    a["M2_hm"] = milling.avg_chip_thickness_side(0.1, 8, 40, 90)
    a["M2_hex"] = milling.max_chip_thickness_side(0.1, 8, 40, 90)
    a["M2_fz"] = milling.feed_for_max_chip_thickness_side(0.1, 8, 40, 90)

    # M3
    kc1, mc = material.get("K1 grey cast iron")
    hm = milling.avg_chip_thickness_face_centred(0.2, 100, 125, 45)
    kc = material.specific_cutting_force(kc1, hm, mc, gamma0=0)
    n = milling.spindle_speed(250, 125)
    vf = milling.table_feed(0.2, n, 8)
    Pc = milling.net_power(3, 100, vf, kc)
    a["M3_hm"], a["M3_kc"] = hm, kc
    a["M3_Q"] = milling.metal_removal_rate(3, 100, vf)
    a["M3_Pc"] = Pc
    a["M3_Mc"] = milling.torque(Pc, n)

    # D1
    kc1, mc = material.get("P2 low-alloy steel")
    n = drilling.spindle_speed(120, 20)
    vf = drilling.penetration_rate(0.25, n)
    hm = drilling.chip_thickness(0.25, 70)
    kc = material.specific_cutting_force(kc1, hm, mc)
    Pc = drilling.net_power(0.25, 120, 20, kc)
    a["D1_n"], a["D1_vf"], a["D1_hm"], a["D1_kc"] = n, vf, hm, kc
    a["D1_Pc"] = Pc
    a["D1_Mc"] = drilling.torque(Pc, n)
    a["D1_Ff"] = drilling.feed_force(kc, 20, 0.25, 70)
    a["D1_Tc"] = drilling.machining_time(60, vf)

    # L1
    nt, C = tool_life.fit_taylor(200, 25, 300, 8)
    a["L1_n"], a["L1_C"] = nt, C
    a["L1_T250"] = tool_life.tool_life(250, C, nt)
    a["L1_v15"] = tool_life.speed_for_tool_life(15, C, nt)

    # L2
    Te = tool_life.economic_tool_life(nt, 2, 4, 1.5)
    a["L2_T"] = Te
    a["L2_vc"] = tool_life.speed_for_tool_life(Te, C, nt)

    # C1 capstone
    kc1, mc = material.get("P2 low-alloy steel")
    # turning
    n_t = turning.spindle_speed(200, 60)
    hm_t = turning.chip_thickness(0.3, 95)
    kc_t = material.specific_cutting_force(kc1, hm_t, mc, gamma0=6)
    Pc_t = turning.net_power(200, 3, 0.3, kc_t)
    Tc_t = turning.machining_time(150, 0.3, n_t)
    # drilling
    n_d = drilling.spindle_speed(100, 12)
    vf_d = drilling.penetration_rate(0.2, n_d)
    hm_d = drilling.chip_thickness(0.2, 70)
    kc_d = material.specific_cutting_force(kc1, hm_d, mc)
    Pc_d = drilling.net_power(0.2, 100, 12, kc_d)
    Tc_d = drilling.machining_time(42, vf_d)
    a["C1_Tc_total"] = Tc_t + Tc_d
    a["C1_P_spindle_max"] = max(Pc_t, Pc_d) / 0.85

    return a


ANSWERS = _answers()


def check(key, value):
    """Compare a student answer with the reference value and print feedback."""
    if key not in ANSWERS:
        print(f"[?] Unknown exercise key '{key}'.")
        return False
    if value is Ellipsis or value is None:
        print(f"[ ] {key}: not answered yet.")
        return False
    try:
        value = float(value)
    except (TypeError, ValueError):
        print(f"[x] {key}: answer must be a number (got {type(value).__name__}).")
        return False
    ref = ANSWERS[key]
    if math.isclose(value, ref, rel_tol=REL_TOL):
        print(f"[ok] {key} = {value:.4g}  correct")
        return True
    ratio = value / ref if ref else float("inf")
    hint = ""
    if any(math.isclose(ratio, f, rel_tol=0.02) for f in (1000, 0.001, 60, 1 / 60, 10, 0.1)):
        hint = "  (off by a constant factor: check your units)"
    print(f"[x] {key} = {value:.4g}  not quite, try again{hint}")
    return False
