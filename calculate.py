import typer
from speechengine import speechEngine


def calculate(prompt:list):
    
    p = " ".join(prompt)
    NewPrompt = p.replace("calculate", "")
    ans = f"The result of the calculation is {eval(NewPrompt)}"
    typer.echo(message=f"\nSARA: {ans}\n")
    speechEngine(ans)
    