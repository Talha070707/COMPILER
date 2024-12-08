import re

# Define token specifications
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(when|otherwise|altern|loop|aslong|halt|create|giveback|display|ask|also|either|nope|within)\b'),
    ('DATATYPE', r'\b(whole|decimal|flag|text|collection|map|pack|group|empty)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('NUMBER', r'\b\d+(\.\d+)?\b'),
    ('STRING', r'"[^"]*"'),
    ('OPERATOR', r'[=+*/-]|==|!=|<=|>=|<|>'),
    ('DELIMITER', r'[{}();,]'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.'),
]

# Compile regex patterns
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)


def tokenize(code):
    """Tokenize the input NexCode program."""
    tokens = []
    line_number = 1
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NEWLINE':
            line_number += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character '{value}' on line {line_number}")
        else:
            tokens.append((kind, value, line_number))
    return tokens


# Main program
def main():
    print("Enter your NexCode program (end input with an empty line):")
    user_input = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_input.append(line)
    nexcode_program = "\n".join(user_input)

    print("\nProcessing your NexCode program...\n")
    try:
        tokens = tokenize(nexcode_program)
        print("Tokens:")
        for token in tokens:
            print(token)
    except SyntaxError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
