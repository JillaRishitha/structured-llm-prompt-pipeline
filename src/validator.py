def validate_json(data: dict) -> bool:
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")

    if "name" not in data:
        raise ValueError("Missing required field: name")

    if "project" not in data:
        raise ValueError("Missing required field: project")

    return True