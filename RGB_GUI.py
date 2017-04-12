import Tkinter
import RPi.GPIO as GPIO # Import GPIO library
GPIO.setmode(GPIO.BOARD) # Use board pin numbering
GPIO.setup(7, GPIO.OUT) # Setup GPIO Pin 7 to OUT
GPIO.setup(11, GPIO.OUT) # Setup GPIO Pin 11 to OUT
GPIO.setup(13, GPIO.OUT) # Setup GPIO Pin 13 to OUT

fudge = Tkinter.Tk()

fudge.wm_title("LED GUI") #sets title of GUI

newButt = Tkinter.Button(fudge, text="LED 1", command=toggleLED1)
newButt.grid(row=0, column=0)
newButt2 = Tkinter.Button(fudge, text="LED 2", command=toggleLED2)
newButt2.grid(row=0, column=1)
newButt3 = Tkinter.Button(fudge, text="LED 3", command=toggleLED3)
newButt3.grid(row=0, column=2)
newButt4 = Tkinter.Button(fudge, text="EXIT", command=terminate)
newButt4.grid(row=0, column=2)

fudge.geometry("500x350") #sets window size

fudge.mainloop()

def toggleLED1():
    if (GPIO.input(7) == True):
        GPIO.output(7, False)
    else:
        GPIO.output(7, True)

def toggleLED2():
    if (GPIO.input(11) == True):
        GPIO.output(11, False)
    else:
        GPIO.output(7, True)

def toggleLED3():
    if (GPIO.input(13) == True):
        GPIO.output(13, False)
    else:
        GPIO.output(13, True)

def terminate():
 GPIO.cleanup()
 global tk
 tk.destroy()

