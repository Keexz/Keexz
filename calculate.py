import time
import typer
from speechengine import speechEngine
import numpy

def calculate():
    prompt = "calculate 1 + 20 + 5".split()
    
    no = []
    
    with typer.open_file('numbers.txt', encoding='utf-8-sig') as nums:
        num = nums.read()
        for i in prompt:
            if i in num:
                    no.append(int(i))
        
        if "+" in prompt:
            typer.echo(numpy.sum(no))

calculate()