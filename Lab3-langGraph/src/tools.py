"""Tools definition for the University Assistant."""

import ast
import operator as op
from datetime import datetime
from langchain_core.tools import tool

# Whitelisted operators for secure arithmetic evaluation
_ALLOWED_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.FloorDiv: op.floordiv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def _safe_eval(node):
    """Recursively evaluates an AST node containing only arithmetic operations."""
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPS:
        return _ALLOWED_OPS[type(node.op)](_safe_eval(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPS:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ALLOWED_OPS[type(node.op)](left, right)
    raise ValueError(f"Unsupported AST node or operation: {ast.dump(node)}")


@tool
def calculator(expression: str) -> str:
    """Safely calculate a mathematical expression using an AST parser.
    Supports addition (+), subtraction (-), multiplication (*), division (/),
    modulo (%), exponentiation (**), integer division (//), and unary signs.
    Does NOT execute arbitrary Python code.
    """
    try:
        cleaned = expression.strip().replace("^", "**")
        parsed = ast.parse(cleaned, mode="eval")
        res = _safe_eval(parsed)
        return str(res)
    except Exception as e:
        return f"Calculation error: {e}"


@tool
def current_datetime(_: str = "") -> str:
    """Return the current date and time.
    Use for any question regarding today's date, the current day, or time.
    """
    return datetime.now().strftime("%A, %B %d, %Y at %H:%M:%S")


# Export list of active assistant tools
ALL_TOOLS = [calculator, current_datetime]

