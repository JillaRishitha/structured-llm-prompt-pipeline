from validator import validate_json


def test_valid_json():
    data = {
        "name": "Rishitha",
        "project": "Structured LLM Prompt Pipeline"
    }

    assert validate_json(data) is True
    print("Test 1 passed: Valid JSON")


def test_missing_name():
    data = {
        "project": "Structured LLM Prompt Pipeline"
    }

    try:
        validate_json(data)
    except ValueError:
        print("Test 2 passed: Missing name detected")
        return

    raise AssertionError("Missing name was not detected")


def test_missing_project():
    data = {
        "name": "Rishitha"
    }

    try:
        validate_json(data)
    except ValueError:
        print("Test 3 passed: Missing project detected")
        return

    raise AssertionError("Missing project was not detected")


def test_invalid_data_type():
    try:
        validate_json("invalid data")
    except ValueError:
        print("Test 4 passed: Invalid data type detected")
        return

    raise AssertionError("Invalid data type was not detected")


if __name__ == "__main__":
    test_valid_json()
    test_missing_name()
    test_missing_project()
    test_invalid_data_type()

    print("\nAll tests completed successfully!")