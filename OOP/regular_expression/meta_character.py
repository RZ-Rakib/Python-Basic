import re

# Sample text
text = "The quick brown or brooown fox jumps over the lazy dog."

# Meta characters and their corresponding patterns
patterns = {
    ".": r"br.wn",         # single dot allow one random character in a word
    ".": r"br...wn",       # Three dots need 3 characters to matches "br" followed by multiple character followed by "wn"
    "*": r"fox.*dog",      # astric allow zero or more character, '.*' means multiple character 
    "*": r"(ad*)",         # astric allow zero or more character, '(ad)*' means multiple d
    "+": r"quick+",        # plus allow one or more, there must be one charecter followed by 'q'
    "+": r"a+b",           # a + b means, atleast one a and one b followed by a 
    "^": r"^The",          # Matches if the string starts with "The"
    "$": r"dog$",          # Matches if the string ends with "dog"
    "?": r"colo?r",        # Matches "color" or "colour"
    "?": r"ice(-)?cream",  # '?' allow zero or one character, not more thn one
    "|": r"fox|dog",       # Matches either "fox" or "dog"
    "[]": r"[aeiou]",      # Matches any vowel character, for mandatory chracter we can use it
    "()": r"(brown|red)",  # Matches either "brown" or "red"
    "{}": r"\d{2}",        # Matches exactly two digits
    "{}": r"\d{1,4}",      # Matches exactly 1-4 digits
    "\\": r"\."            # Matches the period character "."
}

# Iterate over patterns and find matches in the text
for key, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern} | Matches: {matches}")

