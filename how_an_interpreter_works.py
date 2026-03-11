# How a Python Interpreter Works - A Simple Demonstration

# 1. LEXICAL ANALYSIS (Tokenization)
# The interpreter breaks source code into tokens

def tokenize(code):
    """Convert code string into tokens"""
    tokens = []
    current_token = ""
    
    for char in code:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char in "()+-*/=":
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ""
        else:
            current_token += char
    
    if current_token:
        tokens.append(current_token)
    return tokens


# 2. PARSING (Building Abstract Syntax Tree)
# The interpreter organizes tokens into a meaningful structure

class ASTNode:
    """Represents a node in the Abstract Syntax Tree"""
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = int(value)

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


# 3. SEMANTIC ANALYSIS & EXECUTION
# The interpreter evaluates the AST

def evaluate(node):
    """Execute the AST and return the result"""
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, BinaryOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        
        if node.op == "+":
            return left + right
        elif node.op == "-":
            return left - right
        elif node.op == "*":
            return left * right
        elif node.op == "/":
            return left / right


# Example usage
if __name__ == "__main__":
    code = "5 + 3"
    print(f"Code: {code}")
    
    tokens = tokenize(code)
    print(f"Tokens: {tokens}")
    
    # Simple AST for "5 + 3"
    ast = BinaryOp(Number("5"), "+", Number("3"))
    result = evaluate(ast)
    print(f"Result: {result}")

# Hello is printed...
print("Hello")
# ...but then a runtime error occurs here (ZeroDivisionError)
print(10 / 0)
# ...so this line is never reached until the error is handled
print("World")