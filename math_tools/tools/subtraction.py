from agents import function_tool


@function_tool
def subtraction(a:int,b:int)->int:
    "subtract the given integers"

    print(f" Subtraction tool fire --> ")

    return a-b
