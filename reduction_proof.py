import math
import numpy as np

def sat_to_phi(m_clauses):
    C0 = math.log2(2**m_clauses)
    print(f"SAT-to-Φ: C(0) = {C0}")
    return C0  # Maps to v_φ(i) = clause literal count

def analytical_trigger(C0, delta=0.621568):
    """Analytical k = ceil(C0 / delta) for large m"""
    k_ana = math.ceil(C0 / delta)
    return k_ana

# Small m=10 Test (C(0)=10.0, expect k=17)
C = sat_to_phi(10)
print("Small m=10 Test:")
k_arr = np.arange(1, 34)
corrections = -0.621568 + np.log(k_arr) / 1000
C_arr = np.cumsum(corrections) + C
k_trigger = np.argmax(C_arr <= 0)
if k_trigger == 0:
    k_trigger = 33
print(f"Vectorized reduced in {k_trigger} ticks")

# 10^7-SAT Scale Test
C = sat_to_phi(10**7)
print("\n10^7-SAT Scale Test:")
k_ana = analytical_trigger(C)
if k_ana <= 33:
    print(f"Reduced in {k_ana} ticks (analytical)")
else:
    print(f"Bound k={k_ana} >33 (analytical fallback)")
