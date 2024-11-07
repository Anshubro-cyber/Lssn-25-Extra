# Function to perform bitwise operations
def bitwise_operations(a, b):
    # AND operator
    and_result = a & b
    print(f"a & b = {a} & {b} = {and_result}")

    # OR operator
    or_result = a | b
    print(f"a | b = {a} | {b} = {or_result}")

    # XOR operator
    xor_result = a ^ b
    print(f"a ^ b = {a} ^ {b} = {xor_result}")

    # NOT operator
    not_result_a = ~a
    not_result_b = ~b
    print(f"~a = ~{a} = {not_result_a}")
    print(f"~b = ~{b} = {not_result_b}")

    # Left Shift operator
    left_shift_result_a = a << 2  # Shifting a by 2 bits
    left_shift_result_b = b << 2  # Shifting b by 2 bits
    print(f"a << 2 = {a} << 2 = {left_shift_result_a}")
    print(f"b << 2 = {b} << 2 = {left_shift_result_b}")

    # Right Shift operator
    right_shift_result_a = a >> 2  # Shifting a by 2 bits
    right_shift_result_b = b >> 2  # Shifting b by 2 bits
    print(f"a >> 2 = {a} >> 2 = {right_shift_result_a}")
    print(f"b >> 2 = {b} >> 2 = {right_shift_result_b}")

# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function to perform the bitwise operations
bitwise_operations(a, b)
