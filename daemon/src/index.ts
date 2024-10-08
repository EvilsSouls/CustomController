const { Console } = require("node:console");

const robot = require("kbm-robot");

const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');
const port = new SerialPort({ path: '/dev/ttyACM0', baudRate: 9600});

interface Data {
    x: number;
    y: number;
    pressed: boolean;
}

const DAMPENING_VALUE = 0.01;

robot.startJar();

robot.mouseMove(900, 500).go();
let mouseX = 900;
let mouseY = 500;

const parser = port.pipe(new ReadlineParser({ delimiter: '\t' }));
parser.on('data', (rawData: string) => {
    const formattedData: Data = JSON.parse(rawData);

    formattedData.x = formattedData.x * DAMPENING_VALUE;
    formattedData.y = formattedData.y * DAMPENING_VALUE;

    mouseX += formattedData.x;
    mouseY += formattedData.y;
    console.log(mouseX, mouseY)

    robot.mouseMove(mouseX, mouseY).go();
});

robot.stopJar();