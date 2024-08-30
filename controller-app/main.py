from picozero import pico_temp_sensor, pico_led
import utime
import json
from machine import Pin, ADC

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(16, Pin.IN, Pin.PULL_UP)


while True:
    # str(bool(abs(button_value-1)))
    xValue = xAxis.read_u16() // 10
    yValue = yAxis.read_u16() // 10
    button_value = button.value()
    data = {"x": {xValue}, "y": {yValue}, "pressed": str(bool(abs(button_value-1)))}
    print(json.dumps(data).replace("True", "true").replace("False", "false"), end="hello")
    utime.sleep(0.1)

