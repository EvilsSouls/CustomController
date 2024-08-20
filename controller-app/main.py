from picozero import pico_temp_sensor, pico_led
import utime
from machine import Pin, ADC

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(16, Pin.IN, Pin.PULL_UP)


while True:
    xValue = xAxis.read_u16() // 10
    yValue = yAxis.read_u16() // 10
    button_value = button.value()
    print(f"{str(xValue)}, {str(yValue)}, {str(button_value)}")
    utime.sleep(0.1)

