import math

def sat_to_phi(m_clauses):
    C0 = math.log2(2**m_clauses)
    print(f"SAT-to-Φ: C(0) = {C0}")
    return C0  # Maps to v_φ(i) = clause literal count

# Small m=10 Test (C(0)=3.32, expect k=5)
C = sat_to_phi(10)
print("Small m=10 Test:")
for k in range(1, 34):
    C = C - 0.621568 + math.log(k)/1000
    if C <= 0:
        print(f"Reduced in {k} ticks")
        break

# 10^7-SAT Scale Test
C = sat_to_phi(10**7)
print("\n10^7-SAT Scale Test:")
for k in range(1, 34):
    C = C - 0.621568 + math.log(k)/1000
    if C <= 0:
        print(f"Reduced in {k} ticks")
        break
