"""Arquitectura modular para enrutamiento energéticamente eficiente en WSN (Etapa 3)."""

from wsn.exact_solver import ExactSolveResult, solve_exact
from wsn.instance import WSNInstance, generate_instance
from wsn.metaheuristic import MetaheuristicResult, solve_greedy, solve_simulated_annealing
from wsn.validator import validate_solution

__all__ = [
    "ExactSolveResult",
    "MetaheuristicResult",
    "WSNInstance",
    "generate_instance",
    "solve_exact",
    "solve_greedy",
    "solve_simulated_annealing",
    "validate_solution",
]
