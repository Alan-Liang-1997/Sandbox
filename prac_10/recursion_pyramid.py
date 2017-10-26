"""
CP1404/CP5632 Practical
Recursion Pyramid
"""


# # LOOP VERSION
def block_step(rows):
    total = 0
    for i in range(rows):
        total += rows
        rows -= 1
    return total


# RECURSIVE VERSION
def block_step(rows):
    if rows <= 0:
        return 0
    return rows + block_step(rows - 1)


def main():
    rows = int(input("How many rows are in your 2D pyramid? : "))
    print(block_step(rows))

main()
