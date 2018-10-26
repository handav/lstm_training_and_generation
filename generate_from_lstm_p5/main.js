// See https://ml5js.org/docs/LSTMGenerator

var lstm;
var displayText;
var all_generations = [];

function preload() {
    // Create the LSTM Generator with a pre trained model
    lstm = ml5.LSTMGenerator('../models/littleprince/');
    console.log(lstm);
}

function setup() {
    createCanvas(600, 400);
}

function draw() {
    if (displayText) {
        background(255);
        text(displayText, 30, 30);
    }
}

function keyPressed() {
    // Generete content
    lstm.generate({
        seed: 'a',
        length: 60,
        temperature: 0.5
    }, function(results) {
        displayText = results.generated;
        all_generations.push(displayText);
        console.log(all_generations);
    });
    if (keyCode === ENTER) {
        console.log('saving file');
        saveStrings(all_generations, 'notes.txt');
    }
}
