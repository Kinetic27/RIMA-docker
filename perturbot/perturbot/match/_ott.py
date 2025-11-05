"""Compatibility imports for the OTT-JAX package.

Some environments install OTT using a `src` layout (accessible as
`ott.src.ott`), while others expose the modules directly under `ott`.
This module centralizes the import logic so the rest of the codebase can
work with either layout transparently.
"""

try:  # Prefer the src layout when it is available.
    from ott.src.ott.geometry import geometry, pointcloud  # type: ignore[attr-defined]
    from ott.src.ott.problems.linear import linear_problem  # type: ignore[attr-defined]
    from ott.src.ott.problems.quadratic import quadratic_problem  # type: ignore[attr-defined]
    from ott.src.ott.solvers import linear  # type: ignore[attr-defined]
    from ott.src.ott.solvers.linear import acceleration, sinkhorn  # type: ignore[attr-defined]
    from ott.src.ott.solvers.quadratic import gromov_wasserstein  # type: ignore[attr-defined]
except ModuleNotFoundError:
    from ott.geometry import geometry, pointcloud  # type: ignore[attr-defined]
    from ott.problems.linear import linear_problem  # type: ignore[attr-defined]
    from ott.problems.quadratic import quadratic_problem  # type: ignore[attr-defined]
    from ott.solvers import linear  # type: ignore[attr-defined]
    from ott.solvers.linear import acceleration, sinkhorn  # type: ignore[attr-defined]
    from ott.solvers.quadratic import gromov_wasserstein  # type: ignore[attr-defined]

__all__ = [
    "acceleration",
    "geometry",
    "gromov_wasserstein",
    "linear",
    "linear_problem",
    "pointcloud",
    "quadratic_problem",
    "sinkhorn",
]
