from scapy.all import *
import packetParcer
import logger
import time

class lisener:

    def __init__(self,iface) -> None:
        self.running = True

        self.iface = iface


        def sniffer(self):

            def packetHandler(pkt):
                #packetParcer.show(pkt)
                #print(packetParcer.getLayers(pkt))
                packetParcer.filter(pkt,"a4:a4:90:53:91:a4")
                print('.')

                #packetParcer.decapsulate(pkt)




            print("starting sniffer")
            logger.log("starting sniffer")

            while self.running:
                sniff(iface = self.iface, prn = packetHandler, count=16)

            print("sniffer stoped!")
            logger.log("sniffer stoped!")

        
        print("starting sniffer threand")
        logger.log("starting sniffer threand")

        tlisener = Thread(target=sniffer, args=(self,))
        tlisener.start()

        print("sniffer thread statied!")
        logger.log("sniffer thread statied!")
    

    def stop(self):
        logger.log("stoping sniffer")
        self.running = False


if __name__ == "__main__":
    import time
    iface = "wlx00c0cab26f0a"
    rx = lisener(iface)
    input()
    rx.stop()