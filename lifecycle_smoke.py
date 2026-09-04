def can_access(is_admin: bool) -> bool:
    """Only administrators may access this resource."""
    return is_admin
