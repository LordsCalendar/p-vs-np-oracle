import pytest
import math
from n_vs_np_engine import LordsCalendarOracle
from sat_backtrack_full import prune_sat_full_backtrack  # Assume imported

def test_engine_k_trigger():
    oracle = LordsCalendarOracle()
    k, _, _ = oracle.contraction_vectorized(9.965784)  # C0 n=1000
    assert k == 17, f"Expected 17, got {k}"

def test_prune_verify_true():
    # Dummy clauses for test (satisfiable)
    dummy_clauses = [[1, -2, 3]]  # Simple True with [1,1,1]
    result = prune_sat_full_backtrack(dummy_clauses, steps=33)
    assert result['verify'] == True, "Expected verify True"

def test_performance_under_tau():
    oracle = LordsCalendarOracle()
    start = time.time()
    result = oracle.solve_3sat(1000)
    end = time.time()
    assert end - start < 12.49, f"Expected <12.49 s, got {end-start:.2f}"

if __name__ == "__main__":
    pytest.main(['-v', __file__])
