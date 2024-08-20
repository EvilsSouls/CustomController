# Daemon for Custom Controller

This is the daemon that should run on the computer to receive the inputs of the PICO. It should be in the format:
```json
{   
    "leftjoystick": {
        "x": 1212,
        "y": 3131,
        "pressed": true
    },
    "rightjoystick": {
        "x": 1212,
        "y": 3144,
        "pressed": false
    }
}
```