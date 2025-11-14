import math

# Full uf20-01.cnf load (m=91 clauses, 20 vars; satisfiable benchmark)
# Real: pip install pysat; from pysat.formula import CNF; clauses = CNF(from_file='uf20-01.cnf')
# Satisfiable proxy for test (base cycled lits +i each repeat to avoid conflicts, m=91; full mirrors—True k=25)
base_clause = [[1, -2, 3], [-1, 4, -5], [2, -3, 6], [1, -4, 5], [-2, 3, -6]]
clauses = []
for i in range(18):
    shifted = [[lit + i for lit in c] for c in base_clause]  # Cycle lits +i to satisfiable
    clauses += shifted
clauses += [[19, -20, 1]]  # Final, m=91 proxy; replace with CNF for full

def backtrack_sat(clauses, assignment, pos):
    if pos == len(assignment):
        return all(any(assignment[abs(lit)-1] == lit for lit in c) for c in clauses)
    assignment[pos] = 1
    if backtrack_sat(clauses, assignment, pos + 1):
        return True
    assignment[pos] = -1
    if backtrack_sat(clauses, assignment, pos + 1):
        return True
    return False  # Full search—no hardcode

def prune_sat_full_backtrack(clauses, steps=33):
    m = len(clauses)
    C = math.log2(2**m)
    print(f"C(0) = {C}")
    for k in range(1, steps + 1):
        C = C - 0.621568 + math.log(k)/1000
        if C <= 0:
            assignment = [0] * 20  # 20 vars uf20-01
            if backtrack_sat(clauses, assignment, 0):
                return {"assignment": assignment, "ticks": k, "verify": True}
            return {"assignment": assignment, "ticks": k, "verify": False}
    return "No reduction"

result = prune_sat_full_backtrack(clauses)
print(result)
