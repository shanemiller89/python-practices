"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict(amazing = "the feeling of using a new language")

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["python"] = "A easy to read programming language"
word_definitions["terminal"] = "An environment to run programs and commands"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print("Amazing: ", word_definitions["amazing"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}")
