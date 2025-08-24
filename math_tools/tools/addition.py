from agents import function_tool


@function_tool
def addition(a:int,b:int)->int:
    "add the given integers"

    print(f" Plus tool fire --> ")

    return a+b




