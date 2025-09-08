import time
import random

class SensorMovimento:
    """Simulação de um Sensor de Movimento"""
    def detectar_movimento(self):
        return random.choice([True, False])
    
class Lampada:
    """Simulação de uma lâmpada inteligente"""
    def __init__(self):
        self.estado = "desligada"

    def ligar(self):
        self.estado = "ligada"
        print("A lâmpada foi ligada.")
    
    def desligar(self):
        self.estado = "desligada"
        print("A lâmpada foi desligada.")

class AgenteReativoSimples:
    """Agente que irá descobrir que liga/desliga"""
    def __init__(self, sensor, lampada):
        self.sensor = sensor
        self.lampada = lampada

    def agir(self):
        movimento = self.sensor.detectar_movimento()

    # Regra Simples de Percepção

        if movimento:
            self.lampada.ligar()
        else:
            self.lampada.desligar()

# Teste
sensor = SensorMovimento()
lampada = Lampada()
agente = AgenteReativoSimples(sensor, lampada)

print("Iniciando uma simulação de A.R.S")
for _ in range(5):
    agente.agir()
    time.sleep(1)