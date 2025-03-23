import time
import pyautogui
import subprocess
import typer
from speechengine import speechEngine

def calculate(prompt:str):
    
    
    subprocess.Popen(['calc.exe'])
    for i in prompt:
        pyautogui.press(i)
        time.sleep(2)
        
        
    pyautogui.press("=")
    cal_final = "I'm done with the calculation."
    typer.echo(message=f"\nSARA: {cal_final}\n")
    speechEngine(cal_final)