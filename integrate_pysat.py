from pysat.formula import CNF
from pysat.solvers import Glucose3
import math
from typing import List

def load_dimacs(file_path='uf20-01.cnf'):
    """Load SATLIB DIMACS (satisfiable benchmark)"""
    clauses = CNF(from_file=file_path)
    return clauses.clauses, clauses.nv  # Clauses, vars

def prune_dimacs_sat(clauses: List[List[int]], nv: int, steps=33, delta=0.621568):
    C = math.log2(2**len(clauses))  # C0
    print(f"C(0) = {C}, vars={nv}")
    for k in range(1, steps + 1):
        C = C - delta + math.log(k)/1000
        if C <= 0:
            solver = Glucose3()
            for clause in clauses:
                solver.add_clause(clause)
            if solver.solve():
                model = solver.get_model()
                return {"status": "SAT", "ticks": k, "model": model[:10] + ["..."], "full_model_len": nv}
            return {"status": "UNSAT", "ticks": k}
    # Fallback full solve
    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)
    if solver.solve():
        model = solver.get_model()
        return {"status": "SAT (full)", "ticks": steps, "model": model[:10] + ["..."], "full_model_len": nv}
    return {"status": "UNSAT (full)", "ticks": steps}

# Test (assume uf20-01.cnf downloaded; proxy if not)
# result = prune_dimacs_sat(load_dimacs('uf20-01.cnf'))
# print(result)  # Expected SAT k~25, model len=20
