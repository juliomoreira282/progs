import { NeuralNetwork } from 'brain.js';

const net = new NeuralNetwork();

const trainingData = [
        { input: { size: 50, rooms: 2}, output: [200000]},
        { input: { size: 70, rooms: 3}, output: [300000]},
        { input: { size: 100, rooms: 4}, output: [400000]},
        { input: { size: 120, rooms: 5}, output: [500000]}
];

net.train(trainingData);

const output = net.run({ size: 85, rooms: 3});

console.log(`Preço estimado para uma casa de 85m^2 e três quartos: ${output}`);