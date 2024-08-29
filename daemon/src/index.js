"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const { Console } = require("node:console");
const robot = require("kbm-robot");
const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');
const port = new SerialPort({ path: '/dev/ttyACM0', baudRate: 9600 });
const parser = port.pipe(new ReadlineParser({ delimiter: '\t' }));
parser.on('data', (rawData) => {
    const formattedData = JSON.parse(rawData);
});
robot.startJar();
robot.press("alt")
    .press("tab")
    .sleep(100)
    .release("tab")
    .release("alt")
    .sleep(100)
    .typeString("Hello World!")
    .go()
    .then(robot.stopJar);
