import time
import random

class SensorMovimento:
    def detectar_movimento(self):
        return random.choice([True, False])
    
class Lampada:
    def __init__(self):
        self.estado = "desligado"
    
    def ligar(self):
        self.estado = "ligado"
        print("A lâmpada foi ligada.")

    def desligar(self):
        self.estado = "desligado"
        print("A lâmpada foi desligada.")
    
class AgenteReativoSimples:
    def __init__(self, sensor, lampada):
        self.sensor = sensor
        self.lampada = lampada
    
    def agir(self):
        movimento = self.sensor.detectar_movimento()

        if movimento:
            self.lampada.ligar()

        else:
            self.lampada.desligar()

sensor = SensorMovimento()
lampada = Lampada()
agente = AgenteReativoSimples(sensor, lampada)

print("Iniciando uma simulação de ARS")
for _ in range(50):
    agente.agir()
    time.sleep(0.5)