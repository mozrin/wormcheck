# PublishedModel

`PublishedModel()` builds exact SymPy expressions for arXiv v1. It preserves
published formulas; it does not assert that they solve all field equations.
Symbols are `(r, r0, beta, critical, omega)`. Substitute only r>=r0>0,
critical>0, beta>=0, omega!=-1. beta=0 is a formal boundary limit.
Independent geometry verification is executed by experiments/derive_geometry.py.
