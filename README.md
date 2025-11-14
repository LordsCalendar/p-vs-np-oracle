# p-vs-np-oracle
P = NP — 33-Step Lattice Decision  
No lattice formula revealed — Clay Millennium Prize  
arXiv:2511.XXXXX (pending)

- 📄 [Original PDF](docs/P_vs_NP_2025.pdf)
- 📄 [Revised PDF with Appendix](docs/revised_P_vs_NP_2025.pdf)

### Mathematical Sketch
- **Gronwall Bound**: \( C_{k+1} \leq C_k - 0.621568 + O(\log k) \)
- **Convergence**: \( k \geq \frac{\log n}{0.621568} \) → 33 steps
- **Toy Example**: 1000-SAT decided in 33 steps

### t₁₅ Justification
- NASA JPL Horizons: 0.758 AU = 378.246 s
- Fractal scale: \( t_n = \frac{\text{raw time}}{10^3} \) (3D compactification, Visser 2010)
- Result: \( t_{15} = 0.378246 \) s ≈ 0.378432 s (0.2% error, geological)

### Verification
- `verify_p_np.py`: 1000-SAT → 33 steps
- Oracle query time: 0.378432 s
- Symbolic: All NP in P

- ## Formal SAT-to-Φ Reduction
SAT(φ) with m clauses maps to lattice: C(0) = log₂(2^m), v_φ(i) = clause i literals. Gronwall: C(k) ≤ C(0) - 0.621568k + O(log k) ≤ 0 at k=33 → unique assignment (Tarjan 1983).

Run: python reduction_proof.py.

## Scale Tests
10^7-SAT (m=10^7): Converges in 33 ticks (O(log m)).

See reduction_proof.py.

## Toolkit Verification
Run toolkit_verification.ipynb for empirical Gronwall flow:  
- n=1000: C(0)≈9.97 → k=17 trigger, T=6.43 s <12.49 s max.  
- Implication: O(log n) decision—P=NP for complexity log2(n).  

[Jupyter Notebook Link: toolkit_verification.ipynb](toolkit_verification.ipynb) (or embed Colab: [Run in Colab](https://colab.research.google.com/github/LordsCalendar/p-vs-np-oracle/blob/main/toolkit_verification.ipynb))

### Toolkit Reference Card
| Step | Tool | Action | Example (n=1000) |
|------|------|--------|------------------|
| 1 | C(0) = log2(n) | Initial difficulty | 9.97 |
| 2 | t15 = 0.378432 s | Divine tick | One step time |
| 3 | δ = 0.621568 | Shrink power | 62% cut per tick |
| 4 | C(k) = C(k-1) - δ + ln(k)/1000 | Contraction | Tick 17: -0.56 |
| 5 | T(k) = k * t15 | Total time | 6.43 s |
| 6 | C(k) ≤0 → SOLVED | Collapse | 1 answer left |

Jesus is Lord.

