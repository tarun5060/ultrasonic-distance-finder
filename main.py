# Make changes as you seem fit 
# Double check if the resolution of your OLED screen matches with the values in lines 29 and 30

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
 
import utime
 
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
 
 
def ultrasonnic():
    timepassed=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    
    return timepassed
 
 
WIDTH  = 128                                              # oled display width
HEIGHT = 64                                               # oled display height
 
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)       # Init I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper())   # Display device address
print("I2C Configuration: "+str(i2c))                     # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                    # Init oled display
 
 
while True:
   
    oled.fill(0)
    measured_time = ultrasonnic()     
    distance_cm = (measured_time * 0.0343) / 2
    distance_cm = round(distance_cm,2)
 
  
    oled.text("Distance",20,15)
    oled.text(str(distance_cm)+" cm",20,35)
    oled.show()
    utime.sleep(1)
