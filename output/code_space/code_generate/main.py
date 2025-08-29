import binary_search


def run_example():
    # Example 1: Target exists in the list
    sorted_list = [1, 3, 5, 7, 9]
    target = 5
    result = binary_search.binary_search(sorted_list, target)
    print(f"Index of {target}: {result}")

    # Example 2: Target does not exist in the list
    target = 4
    result = binary_search.binary_search(sorted_list, target)
    print(f"Index of {target}: {result}")


if __name__ == "__main__":
    run_example()