"""Internal utilities shared across funcache modules."""

import inspect
import os
from typing import Any, Callable, Dict, Tuple


def normalize_args(
    func: Callable, args: Tuple[Any, ...], kwargs: Dict[str, Any]
) -> Dict[str, Any]:
    """Convert positional arguments to keyword arguments based on function signature.

    This merges positional args into a unified kwargs dict for consistent
    cache key lookup by parameter name.
    """
    merged = dict(kwargs)
    params = list(inspect.signature(func).parameters.items())
    for i, (name, param) in enumerate(params):
        if name not in merged:
            merged[name] = args[i] if i < len(args) else param.default
    return merged


def ensure_gitignore(directory: str) -> None:
    """Create a .gitignore with '*' in the given directory if one doesn't exist."""
    os.makedirs(directory, exist_ok=True)
    ignore_file = os.path.join(directory, ".gitignore")
    if not os.path.exists(ignore_file):
        with open(ignore_file, "w") as f:
            f.write("*")
