from agents import function_tool


@function_tool
async def math_function(a:int,b:int)->int:
    "reutrn addition of 2 numbers"
    print(f" Plus tool fire --> ")
    return a + b