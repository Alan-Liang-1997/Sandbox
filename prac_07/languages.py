"""CP1404/CP5632 Practical - Client code to use ProgrammingLanguage class."""

from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


print(ruby)
print(python)
print(visual_basic)

# Line break
print()

# Languages list contains the three existing objects
languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
