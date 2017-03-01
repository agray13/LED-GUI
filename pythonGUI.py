from Tkinter import *
import RPi.GPIO as GPIO # Import GPIO library
GPIO.setmode(GPIO.BOARD) # Use board pin numbering
GPIO.setup(7, GPIO.OUT) # Setup GPIO Pin 7 to OUT
 
#Set display sizes
WINDOW_W = 500
WINDOW_H = 100
def createDisplay():
 global tk
 # create the tk window - within which
 # everything else will be built.
 tk = Tk()
 #Add a canvas area ready for drawing on
 canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H)
 canvas.pack()
 #Add an exit button
 btn = Button(tk, text="Exit", command=terminate)
 btn.pack()
 btn2 = Button(tk, text="ON", command=onLED)
 btn2.pack()
 btn3 = Button(tk, text="OFF", command=offLED)
 btn3.pack()
 # Start the tk main-loop (this updates the tk display)
 tk.mainloop()
 
def onLED():
 GPIO.output(7, True)

def offLED():
 GPIO.output(7, False)

def terminate():
 GPIO.cleanup()
 global tk
 tk.destroy()
 
def main():
 createDisplay()
 
if __name__ == '__main__':
 main()

