"""Arquitectura modular para enrutamiento energéticamente eficiente en WSN (Etapa 3)."""

from wsn.exact_solver import ExactSolveResult, solve_exact
from wsn.instance import WSNInstance, generate_instance
from wsn.validator import validate_solution

__all__ = [
    "ExactSolveResult",
    "WSNInstance",
    "generate_instance",
    "solve_exact",
    "validate_solution",
]
