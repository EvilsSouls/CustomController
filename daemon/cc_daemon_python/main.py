import serial
import json
import pyautogui

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5,
    inter_byte_timeout=0.1
)

MAX_VALUE = 6554
SCREEN_SIZE = pyautogui.size()
print(SCREEN_SIZE)


while True:
    # Checks for more bytes in the input buffer
    bufferBytes = ser.inWaiting()

    # If exists, it is added to the myBytes variable with previously read information
    if bufferBytes:
        data = ser.read(bufferBytes).decode('utf-8').strip()
        print(data)
        try:
            if data[0] != "{":
                data = "{" + data
            if data[-1] != "}":
                data = data[:len(data)-1]
            if len(data) > 20:
                print(data)
                json_data = json.loads(data)
                print(json_data)
                if int(json_data["x"]) <= 1000:
                    pyautogui.move(1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        , 0, 0.01)
                if int(json_data["x"]) >= 5000:
                    pyautogui.move(-1, 0, 0.01)
                if int(json_data["y"]) <= 1000:
                    pyautogui.move(1, 1, 0.01)
                if int(json_data["y"]) >= 5000:
                    pyautogui.move(0, -1, 0.01)
                print("-" * 80)
        except IndexError:
            pass

