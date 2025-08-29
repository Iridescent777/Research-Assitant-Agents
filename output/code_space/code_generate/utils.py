def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")
    if not input_list:
        raise ValueError("Input list cannot be empty.")
    return True


def print_sorted_list(input_list):
    validate_input(input_list)
    sorted_list = sorted(input_list)
    print(sorted_list)