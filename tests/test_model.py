"""Necessary identities and regression evidence for the initial audit."""
import sympy as s
from wormcheck import PublishedModel


def test_density_conservation_and_throat():
    model = PublishedModel()
    r, r0, beta, critical, omega = model.symbols
    assert model.residuals['density'] == 0
    assert model.residuals['conservation'] == 0
    assert s.simplify(model.b.subs(r, r0) - r0) == 0
    assert s.simplify(model.phi.subs(r, r0)) == 0


def test_regular_throat_requires_radial_pressure_constraint():
    model = PublishedModel()
    r, r0, beta, critical, omega = model.symbols
    expected = -1/r0**2 - 8*s.pi*model.pe.subs(r,r0)
    assert s.simplify(model.residuals['radial'].subs(r,r0)-expected) == 0


def test_published_sample_fails_radial_equation():
    model = PublishedModel()
    r, r0, beta, critical, omega = model.symbols
    substitutions = {r:s.Rational(11,10),r0:1,beta:s.Rational(1,100),critical:s.Rational(5,1000),omega:3}
    assert model.residuals['radial'].subs(substitutions).evalf(30) > 5
    assert model.residuals['angular'].subs(substitutions).evalf(30) > 14


def test_residual_identity_does_not_force_pressure_equations():
    model = PublishedModel()
    r = model.symbols[0]
    radial, angular = model.residuals['radial'], model.residuals['angular']
    identity = s.diff(radial,r)+s.diff(model.phi,r)*radial+2*(radial-angular)/r
    assert s.factor(identity) == 0


def test_casimir_residuals_have_nonzero_asymptotic_coefficients():
    model = PublishedModel()
    r, r0, beta, critical, omega = model.symbols
    for name, expected in [('radial',6),('angular',9)]:
        expression = s.factor(r**2*model.residuals[name].subs(omega,3))
        assert s.simplify(s.limit(expression,r,s.oo)-expected) == 0


def test_independent_numerical_transcription_agrees():
    import json
    import subprocess
    import sys
    from pathlib import Path

    script = Path(__file__).resolve().parents[1]/'experiments'/'precision_check.py'
    result = json.loads(subprocess.check_output([sys.executable,str(script)],text=True))
    model = PublishedModel()
    r,r0,beta,critical,omega = model.symbols
    for row in result['rows']:
        if row['digits'] == 60:
            parameters={r:s.Rational(row['r']),r0:1,beta:s.Rational(1,100),critical:s.Rational(5,1000),omega:3}
            for name in ['radial','angular']:
                symbolic = model.residuals[name].subs(parameters).evalf(50)
                independent = s.Float(row['components'][name]['residual'],50)
                assert abs(symbolic-independent) < s.Float('1e-45')
