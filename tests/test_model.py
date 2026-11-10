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
