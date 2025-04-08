"""My first exercise in CAMP110!"""

__author__ = "730677063"


def greet(name: str) -> str:
    """A welcoming firs function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("WHAT IS YOUR NAME? ")))
