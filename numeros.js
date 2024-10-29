import { NeuralNetwork } from 'brain.js';

// Criar uma nova rede neural
const net = new NeuralNetwork();
const trainingData = [
    { input: [0, 0], output: [0]},
    { input: [0, 1], output: [1]},
    { input: [1, 0], output: [1]},
    { input: [1, 1], output: [2]}
];

// Treinar a rede neural
net.train(trainingData, { iterations: 2000});

// Fazer previsões
const output = net.run([1, 1]);

console.log(`O resultado de 1 + 1 é aproximadamente: ${output}`);