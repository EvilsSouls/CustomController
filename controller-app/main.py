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
    print(str({"x": xValue, "y": yValue, "pressed": str(bool(abs(button_value-1))})), end="\t")
    utime.sleep(0.1)

