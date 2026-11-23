# Case Study 61: Nested List Examination Seating Validation
# The two reserved positions use 1-based row and column numbers.

seating = [
    ["ST101", "RESERVED", "ST103", "EMPTY"],
    ["ST104", "ST105", "ST101", "ST107"],  # ST101 is a duplicate.
    ["ST108", "ST109", "BAD09", "RESERVED"]
]
reserved_positions = [(1, 2), (3, 4)]
seen_roll_numbers = []
duplicate_count = 0
invalid_count = 0
empty_count = 0
reserved_errors = 0

print("SEATING VALIDATION REPORT")
for i in range(len(seating)):
    for j in range(len(seating[i])):
        seat = seating[i][j]
        row_number = i + 1
        column_number = j + 1
        position = (row_number, column_number)

        if position in reserved_positions:
            if seat != "RESERVED":
                print("Reserved-seat error at", position)
                reserved_errors = reserved_errors + 1
        elif seat == "EMPTY":
            print("Vacant seat at", position)
            empty_count = empty_count + 1
        elif len(seat) < 4 or seat[0:2] != "ST" or seat[2:].isdigit() == False:
            print("Invalid roll number", seat, "at", position)
            invalid_count = invalid_count + 1
        elif seat in seen_roll_numbers:
            print("Duplicate roll number", seat, "at", position)
            duplicate_count = duplicate_count + 1
        else:
            seen_roll_numbers.append(seat)

print("\nDuplicate entries:", duplicate_count)
print("Invalid entries:", invalid_count)
print("Vacant seats:", empty_count)
print("Reserved-seat errors:", reserved_errors)
