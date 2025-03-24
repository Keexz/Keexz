import pyautogui
import subprocess
import typer
import time
import pygetwindow as gw
from speechengine import speechEngine #SElf created function that generates a female voice

def planner():
    #Ask the amount of plans i want to set then collects my input via planA_1
    planq_1 = "How many plans do you want to set?"
    typer.echo(message=f"\nSARA: {planq_1}\n")
    speechEngine(planq_1)
    planA_1 = typer.prompt(text="Gnosis", type=int)
    
    i = 0
    
    with typer.open_file('set_plan.txt', mode='w') as plan:
        
        while i < planA_1+1: #Add one to the amount of my plan so i can write the name of my plan
            if i == 0: 
                #Ask me the name of my plan and collects the input via plan_name_ans
                plan_name = "What is the name of your plan?"
                typer.echo(message=f"\nSARA: {plan_name}\n")
                speechEngine(plan_name)
                plan_name_ans = typer.prompt(text="Gnosis")
                plan.writelines(f"{plan_name_ans}\n\n")
                i+=1
                
            elif i < planA_1+1 and i == 1:
                plan_plan = "What is the plan"
                typer.echo(message=f"\nSARA: {plan_plan}\n")
                speechEngine(plan_plan)
                n2 = typer.prompt(text="Gnosis")
                plan.writelines(f"{i}. {n2}\n\n")
                i+=1
            
            elif i < planA_1+1 and i > 1:
                next_plan = "What is the next plan"
                typer.echo(message=f"\nSARA: {next_plan}\n")
                speechEngine(next_plan)
                n2 = typer.prompt(text="Gnosis")
                plan.writelines(f"{i}. {n2}\n\n")
                i+=1
                
            elif i >= planA_1+1:
                typer.echo("Set")
            
    # Open Notepad
    subprocess.Popen(['notepad.exe'])
    time.sleep(2)  # Wait for the app to open
    # Type text from the plan.txt file
    with typer.open_file('plan.txt') as plan:
        n = plan.read()
        pyautogui.write(message=n, interval=0.5)
        pyautogui.press("enter")
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        if gw.getActiveWindowTitle() == "Confirm Save As":
            pyautogui.press('left')
            time.sleep(1)
            pyautogui.press('enter')
            saved_plan = "I have saved your plan"
            typer.echo(message=f"\nSARA: {saved_plan}\n")
            speechEngine(saved_plan)
            
        else:
            typer.echo(message=f"\nSARA: {saved_plan}\n")
            speechEngine(saved_plan)