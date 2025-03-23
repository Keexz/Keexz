import pyttsx3

def speechEngine(prompt):
    engine = pyttsx3.init()
    
    # Get available voices
    voices = engine.getProperty("voices")
    
    #Set a different voice which is female
    engine.setProperty("voice", voices[1].id)  # Change index for different voices
    

    # Change speaking rate
    engine.setProperty("rate", 150)  # Default ~200, lower is slower
    
    # Change volume (0.0 to 1.0)
    engine.setProperty("volume", 1.0)  # Max volume

    engine.say(prompt)
    engine.runAndWait()
