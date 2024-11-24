from scapy.all import *
import logger


def show(pkt):
    print("\nnew packet rcved----->")
    #print("summery:")
    #print(pkt.summary)
    print("payload:")
    print(pkt.payload)
    print("outer most layer:")
    print(pkt.name)

    
    

def getLayers(pkt):
    layers = []
    layers.append(pkt.name)
    
    inerlayers = str(pkt.payload).split('/')
    
    layers = layers+inerlayers


    return layers


def decapsulate(pkt):
    pass


