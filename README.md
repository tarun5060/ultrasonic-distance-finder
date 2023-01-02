# Ultrasonic Distance Finder

<img src='https://cdn.discordapp.com/attachments/798470888843378708/1059379937766801448/image.jpeg' alt='This is what my version looks like'/>

**An Ultrasonic Distance Finder using HC-SR04 Ultrasonic Distance Sensor, powered by Raspberry Pi Pico &amp; display the measured distance in an SSD1306 OLED Display.**

## Required Parts

* Raspberry Pi Pico
* Ultrasonic Sensor HC-SR04
* SSD1306 OLED Display (I used generic one with 128 x 64 resolution)
* Breadboard
* A few jumper wires 
* Micro-USB Cable (which we will need to connect the Pico Pi with our desktop)

## Connections 

We will firstly place the Pi Pico and other modules on the breadboard and then connect the jumper wires as shown in the tables below. Refer to this [PDF](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) for the Pi Pico pinouts.

**Interfacing the HC-SR04 Ultrasonic Distance Sensor with Pi Pico:**
| HC-SR04  | Pico |
| ------------- | ------------- |
| GND  | GND |
| Echo  | 2  |
| Trig| 3  |
| VCC| 3V3 (OUT)  |

**Interfacing the SSD1306 OLED Display with Pi Pico:**
|  SSD1306 | Pico |
| ------------- | ------------- |
| GND  | GND |
| SCL| GP17  |
| SDA| GP16  |
| VCC| 3V3 (OUT)  |

We have finished the hardware part, we can proceed with the software now.

## Python script 

I hope your Pi Pico is ready to be used with Thonny IDE, if not, refer to this [guide](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2). 
Once that's sorted, connect your Pi Pico with your desktop using the Micro-USB cable. 
* Open Thonny IDE and select `MicroPython (Raspberry Pi Pico)` as your interpreter
* Download the [`ssd1306.py`](https://github.com/tarun5060/ultrasonic-distance-finder/blob/main/ssd1306.py)module library and the [`main.py`](https://github.com/tarun5060/ultrasonic-distance-finder/blob/main/main.py) script 
* Place both `.py` scripts in Pi Pico and run it

You should see an output on the OLED display now and that's it you've done it. I hope you liked this project <3

## Contact & Support
If you encounter a bug or an issue, feel free to reach me 
- Discord: [`Tarun#0001`](https://discord.com/users/603592344348000266)
- Twitter: [`@_tarun0`](https://twitter.com/_tarun0)

If you wish to support me and this project, you can do so [here](https://buymeacoffee.com/trnx0). Appreciate it :)

Made with❤️by Tarun
