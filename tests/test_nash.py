import numpy as np
from game_theory.payoff import build_payoff
from game_theory.game_engine import solve_game
from game_theory.mixed_strategy import solve_zero_sum_lp
from game_theory.pure_nash import find_saddle_point, maximin_minimax
from game_theory.best_response import defender_best_response, attacker_best_response
from game_theory.expected_utility import expected_utility


def test_matching_pennies_known_solution():
    # rows = attacker, cols = defender, entries = defender utility. Value 0, mix 0.5/0.5
    U = np.array([[1, -1], [-1, 1]], dtype=float)
    q, p, v, w = solve_zero_sum_lp(U)
    assert np.allclose(q, [0.5, 0.5]) and np.allclose(p, [0.5, 0.5])
    assert abs(v) < 1e-9 and abs(w) < 1e-9
    assert find_saddle_point(U) is None


def test_rock_paper_scissors():
    U = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]], dtype=float)
    q, p, v, w = solve_zero_sum_lp(U)
    assert np.allclose(q, 1 / 3) and abs(v) < 1e-9


def test_saddle_point_detected():
    U = np.array([[3, 1], [4, 2]], dtype=float)   # defender col0 vs row...: pure equilibrium exists
    mm, MM = maximin_minimax(U)
    assert abs(mm - MM) < 1e-12
    assert find_saddle_point(U) is not None
    q, p, v, w = solve_zero_sum_lp(U)
    assert abs(v - mm) < 1e-9


def test_best_responses():
    U = np.array([[1, -1], [-1, 1]], dtype=float)
    assert defender_best_response(U, [1, 0])[0] == 0
    assert attacker_best_response(U, [1, 0])[0] == 1


def test_expected_utility():
    U = np.array([[1, -1], [-1, 1]], dtype=float)
    assert abs(expected_utility(U, [0.5, 0.5], [0.5, 0.5])) < 1e-12


def test_engine_on_project_game_both_threat_states():
    U, _ = build_payoff("data/")
    for t in ([0.60, 0.15, 0.20, 0.05], [0.15, 0.10, 0.65, 0.10], [0.25] * 4):
        r = solve_game(U, t)
        assert r["verified"]
        assert abs(r["defense_probs"].sum() - 1) < 1e-9
        assert r["value"] <= 0
        assert r["maximin"] <= r["value"] + 1e-7 <= r["minimax"] + 2e-7
