import random
import typer
import datetime
from planner import planner # Self created function that save plans
from speechengine import speechEngine #SElf created function that generates a female voice
from calculate import calculate

app = typer.Typer()

@app.command()
def main():
    device = True #Set SARA on
    morning = [0,1,2,3,4,5,6,7,8,9,10,11]
    afternoon = [12,13,14,15,16,17,18]
    evening = [19,20,21,22,23]
    hour = datetime.datetime.now().hour
    x = "SARA"
    cal = ['calculate']
    plan = ['plans', 'plan']
    
    #Greetings
    if hour in morning:
        with typer.open_file('morning_greetings.txt', encoding="utf-8-sig") as mornings:
            m_greets = mornings.readlines()
            m_greet = random.choice(m_greets)
            typer.echo(message=f"\n{x}: {m_greet}\n")
            speechEngine(m_greet)
        
    elif hour in afternoon:
        with typer.open_file('afternoon_greetings.txt', encoding="utf-8-sig") as afternoons:
            a_greets = afternoons.readlines()
            a_greet = random.choice(a_greets)
            typer.echo(message=f"\n{x}: {a_greet}\n")
            speechEngine(a_greet)
            
    elif hour in evening:
        with typer.open_file('evening_greetings.txt', encoding="utf-8-sig") as evenings:
            e_greets = evenings.readlines()
            e_greet = random.choice(e_greets)
            typer.echo(message=f"\n{x}: {e_greet}\n")
            speechEngine(e_greet)
    
    no = 0
    
    while device:
        #Ask question and awaits for prompt
        
        if no == 0:
            with typer.open_file('questions.txt', encoding="utf-8-sig") as what:
                whats = what.readlines()
                whats_choice = random.choice(whats)
                typer.echo(message=f"\n{x}: {whats_choice}\n")
                speechEngine(whats_choice)
                no+=1
                
        elif no == 1:
            whatss = "What is next boss."
            typer.echo(message=f"\n{x}: {whatss}\n")
            speechEngine(whatss)
            
        prompt = str.lower(typer.prompt(text="Gnosis")).split()
        
        
        for p in plan:
            for i in prompt:
                if i == p:
                    planner()
                         
        for c in cal:
            for i in prompt:
                if i == c:
                    calculate(prompt=prompt)          
                
        
if __name__ == '__main__':
    app()