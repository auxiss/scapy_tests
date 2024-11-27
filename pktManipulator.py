from scapy.all import *
import logger


def show(pkt):
    print("packet info:")
    print("summery:")
    print(pkt.summary())
    print("all:")
    print(pkt.show())
    #print("payload:")
    #print(pkt.payload)
    #print("outer most layer:")
    #print(pkt.name)
    pass

    
    

def getLayers(pkt):
    layers = []

    layers.append(pkt.name)
    inerlayers = str(pkt.payload).split('/')
    layers = layers+inerlayers

    return layers


def filter(pkt,keyword):
    if keyword in str(pkt.summary):
        return pkt
    else:
        return None
    

def decapsulate(pkt):
    layers = getLayers(pkt)
    for i in range(len(layers)): 
        layer = layers[i]

        if "Ether" in layer:
            pass




