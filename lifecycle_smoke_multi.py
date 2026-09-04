def safe_average(total: float, count: int) -> float:
    """Return 0 when count is zero, otherwise return total / count."""
    if count == 0:
        return 0
    return total / count
