"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = result()
    print(score)

def result():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        score = "Invalid score"
    elif score >= 90:
        score = "Excellent"
    elif score >= 50:
        score = "Passable"
    else:
        score = "Bad"
    return score

main()