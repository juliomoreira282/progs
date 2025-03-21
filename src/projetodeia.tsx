import React, {useState} from 'react';
import axios from 'axios';

interface ChatMessage {
    user: string;
    message: string;
}

const ChatBot: React.FC = () => {
    const[messages, setMessages] = useState<ChatMessage[]>([]);
    const[input, setInput] = useState('');

    const sendMessage = async(userMessage: string) => {
        const newMessage = {user: 'Você', message: userMessage};
        setMessages([...messages, newMessage]);
        setInput('');
        try {
            const response = await axios.post('/api/chatbot', { message: userMessage });
            const botMessage = response.data.response;
            setMessages((prevMessages) => [...prevMessages, { user: 'Bot', message: botMessage}]);
        }
        catch(error) {
            setMessages((prevMessages) => [...prevMessages, { user: 'Bot', message: 'Erro ao obter resposta. Tente novamente.'}]);
        }
    };

    const handleInputChange = (e:React.ChangeEvent<HTMLInputElement>) => 
    setInput(e.target.value);
    const handleKeyPress = (e:React.KeyboardEvent) => {
        if(e.key === 'Enter') sendMessage(input);
    };

    return (
        <div className="chatbot-container">
            <div className="messages">
            {messages.map((msg, index) => (
                <div key={index} className={msg.user === 'Bot' ? 'bot-message': 'user-message'}>
                    <strong>{msg.user}</strong>{msg.message}
        </div>
            ))}
        </div>
        <input
        type="text"
        value={input}
        onChange={handleInputChange}
        onKeyUp={handleKeyPress}
        placeholder="Digite sua mensagem..."
        />
        </div>
    );
};

export default ChatBot;
import express from 'express';
import brain from 'brain.js';
const app = express();
app.use(express.json());

const net = new brain.NeuralNetwork();

net.train([
    { input: { reserva: 1 }, output: { reservaResposta: 1 }},
    { input: { turismo: 1}, output: { turismoResposta: 1}},
    { input: { saudacao: 1}, output: { saudacaoResposta: 1 }},
    { input: { transporte: 1}, output: { transporteResposta: 1 }},
    { input: { restaurantes: 1}, output: { restaurantesResposta: 1}},
    { input: { compras: 1}, output: { comprasResposta: 1}},
    { input: { praias: 1}, output: { praiasResposta: 1}},
    { input: { clubes: 1}, output: { clubesResposta: 1}},
    { input: { bares: 1}, output: { baresResposta: 1}},
    { input: { parquesAquaticos: 1}, output: { parquesAquaticosResposta: 1}},
    { input: { shows: 1}, output: { showsResposta: 1}},
    { input: { parquesDeDiversoes: 1}, output: { parquesDeDiversoesResposta: 1}},
]);

interface InterpretationResult {
    reservaResposta: number;
    turismoResposta: number;
    saudacaoResposta: number;
    transporteResposta: number;
    restaurantesResposta: number;
    comprasResposta: number;
    praiasResposta: number;
    clubesResposta: number;
    baresResposta: number;
    parquesAquaticosResposta: number;
    showsResposta: number;
    parqueDeDiversoesResposta: number;
}

const interpretMessage = (message: string): InterpretationResult => {
    const input = {
        reserva: message.includes("reserva") ? 1 : 0,
        turismo: message.includes("turismo") || message.includes("pontos turísticos") ? 1 : 0,
        saudacao: message.includes("oi") || message.includes("olá") ? 1 : 0,
        transporte: message.includes("táxi") || message.includes("uber") || message.includes("ônibus") ? 1 : 0,
        restaurantes: message.includes("restaurante") || message.includes("lanchonete") || message.includes("pizzaria") ? 1 : 0,
        compras: message.includes("shopping") || message.includes("compras") ? 1 : 0,
        praias: message.includes("praias") ? 1 : 0,
        clubes: message.includes("clubes") ? 1 : 0,
        bares: message.includes("bares") || message.includes("lugar para beber") ? 1 : 0,
        parquesAquaticos: message.includes("parque aquático") || message.includes("piscina") ? 1 : 0,
        shows: message.includes("shows") ? 1 : 0,
    };
    return net.run(input) as InterpretationResult;
}

const handleBotResponse = (message: string) => {
    const response = interpretMessage(message);
    if(response.reservaResposta > 0.5) {
        return "Claro! posso te ajudar a reservar um quarto! Qual a data e o tipo de hospedagem?";
    }
    if(response.turismoResposta > 0.5) {
        return "Recomendo o Marco dos Corais, algum outro ponto turístico?";
    }
    if(response.saudacaoResposta > 0.5) {
        return "Olá! Como posso te ajudar hoje?";
    }
    if(response.transporteResposta > 0.5) {
        return "Claro! O que gostaria de pedir para ir até o local solicitado?";
    }
    if(response.restaurantesResposta > 0.5) {
        return "Muito bem. em que tipo de restaurante deseja comer?";
    }
    if(response.comprasResposta > 0.5) {
        return "Interessante. Onde você gostaria de fazer compras?";
    }
    if(response.praiasResposta > 0.5) {
        return "Ótima escolha! Para qual praia gostaria de ir?";
    }
    if(response.clubesResposta > 0.5) {
        return "Muito bem. Para qual clube você gostaria de ir?";
    }
    if(response.baresResposta > 0.5) {
        return "Entendido. Para qual bar deseja ir?";
    }
    if(response.parquesAquaticosResposta > 0.5) {
        return "Querendo aliviar o calor, né? Certo. Para qual parque aquático deseja ir?";
    }
    if(response.showsResposta > 0.5) {
        return "Quer um pouco de curtição? Temos excelentes shows programados para hoje!";
    }
    if(response.parqueDeDiversoesResposta > 0.5) {
        return "Compreensível. Para qual parque de diversões deseja ir?";
    }
    return "Não entendi, poderia reformular sua pergunta, por favor.";
};

app.post('api/chatbot', (req, res) => {
    const { message } = req.body;
    const botResponse = handleBotResponse(message);
    res.json({ response: botResponse });
});

app.listen(3000, () => console.log("Servidor rodando na porta 3000."));