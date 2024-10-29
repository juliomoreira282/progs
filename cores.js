const brain = require('brain.js');

const net = new brain.NeuralNetwork();

const trainingData = [
    { input: {r: 1, g: 0, b: 0}, output: { vermelho: 1}},
    { input: {r: 0, g: 1, b: 0}, output: { verde: 1}},
    { input: {r: 0, g: 0, b: 1}, output: { azul: 1}},
    { input: {r: 1, g: 1, b: 0}, output: { amarelo: 1}}
];

net.train(trainingData, { iterations: 2000});

const output = net.run({ r: 0.8, g: 0.1, b: 0.1});

console.log(`Classificação da Cor: ${output}`);