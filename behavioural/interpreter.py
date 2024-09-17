# Core or library code


class Context:
    """Stores variable values for expression evaluation."""

    def __init__(self, variables: dict[str, int]):
        self.variables = variables

    def get_variable_value(self, name: str) -> int:
        """Returns the value of a variable."""
        return self.variables.get(name, 0)


class AbstractExpression:
    """Defines the interface for all arithmetic expressions."""

    def interpret(self, context: Context) -> int: ...


# Consumer or add-on code


class TerminalVariableExpression(AbstractExpression):
    """Responsible for grammar for variable expression."""

    def __init__(self, name: str):
        self.name = name

    def interpret(self, context: Context) -> int:
        return context.get_variable_value(self.name)


class NonTerminalAddExpression(AbstractExpression):
    """Responsible for grammar for addition between two expressions."""

    def __init__(self, left: AbstractExpression, right: AbstractExpression):
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) + self.right.interpret(context)


# Any component can make code like this (client, core, non-core)


class Client:
    def evaluate_expression(
        self, expression: AbstractExpression, variables: dict[str, int]
    ):
        """Evaluates an arithmetic expression with variable values."""
        context = Context(variables)
        result = expression.interpret(context)
        print(f"Result: {result}")
        return result


if __name__ == "__main__":
    client = Client()

    expression_1 = TerminalVariableExpression("x")
    result = client.evaluate_expression(expression_1, {"x": 5})
    assert result == 5

    expression_2 = NonTerminalAddExpression(
        TerminalVariableExpression("x"), TerminalVariableExpression("y")
    )
    result = client.evaluate_expression(expression_2, {"x": 3, "y": 4})
    assert result == 7

    print("All tests passed!")
