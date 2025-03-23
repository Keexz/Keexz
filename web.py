import webbrowser

import typer
ser = "How to get high"
#webbrowser.open(f"https://www.google.com/search?q={ser}&oq={ser}&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAtIBCDkwNzBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8")

n = "https://www.google.com/search?q=How%20to%20get%20high&oq=How%20to%20get%20high&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAtIBCDkwNzBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
n2 = "https://www.google.com/search?q=how+to+get+high&oq=how+to+get+high&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAtIBCDYzMDdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
from nicegui import ui

from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class MyApp(App):
    def compose(self) -> ComposeResult:
        b = Button("Click me")
        yield Label("Welcome to My Python Ap!")
        yield b
        if b:
            yield Label("OK")
MyApp().run()
