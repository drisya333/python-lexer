from tokens import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def identifier(self):
        result = ""
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return Token(TokenType.IDENT, result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS)

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS)

            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MUL)

            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIV)

            if self.current_char == "=":
                self.advance()
                return Token(TokenType.ASSIGN)

            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN)

            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN)

            raise Exception(f"Illegal character: {self.current_char}")

        return Token(TokenType.EOF)


if __name__ == "__main__":
    code = input("Enter Expression:")
    lexer = Lexer(code)

    token = lexer.get_next_token()
    while token.type != TokenType.EOF:
        print(token)
        token = lexer.get_next_token()
