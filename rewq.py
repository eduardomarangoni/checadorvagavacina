import paho.mqtt.client as mqtt
import sys
from requests import get
from bs4 import BeautifulSoup
import time
print("Mensagem de checagem de funcinamento")



#definicoes: 
Broker = "raspberrypi.local"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "vacina" #dica: troque o nome do topico por algo "unico", 
                                    #Dessa maneira, ninguem ira saber seu topico de
                                    #subscribe e interferir em seus testes

#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    pass


print("[STATUS] Inicializando MQTT...")
#inicializa MQTT:
client = mqtt.Client()
client.on_connect = on_connect
      
        

client.connect(Broker, PortaBroker, KeepAliveBroker)
client.publish("vacina", "teste")


while True:
    # Code executed here
    
    url = 'https://www.vacinajoinville.com.br/'
    response = get(url)

    # create soup
    soup = BeautifulSoup(response.text, 'html.parser')



    te = soup.find("h5", class_="card-title")
    string = te.get_text()
    if ((string.find("20") != -1) or (string.find("19") != -1) or (string.find("18") != -1)):
        print("tem vacina")
        client.publish("vacina", "nao tem vacina")
        seconds = time.time()
        local_time = time.ctime(seconds)
        print("Hora:", local_time)
        
    else:
        print ("nao tem vacina")
        client.publish("vacina", "nao tem vacina")
        seconds = time.time()
        local_time = time.ctime(seconds)
        print("Hora:", local_time)

    time.sleep(3600)
