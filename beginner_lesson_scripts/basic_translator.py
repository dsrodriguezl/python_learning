# Translate any phrase into a language where all vowels correspond to a g
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter in "AEIOUaeiou":
      translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print("First translator")
print(translate(input("Enter a phrase: ")))


# Another version of the previous translator
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print("Another version of the same translator")
print(translate(input("Enter a phrase: ")))


# This version replaces upper case vowels with Gs
def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation = translation + "G"
      else:
        translation = translation + "g"
    else:
      translation = translation + letter
  return translation
print("upper case consistent translator")
print(translate(input("Enter a phrase: ")))
