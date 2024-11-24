from scapy.all import *
import logger
import time

class lisener:

    def __init__(self,iface) -> None:
        self.running = True

        self.iface = iface
        self.PktBuffer = []

        def sniffer(self):

            def packetHandler(pkt):
                print(pkt.show)

            print("starting sniffer")
            logger.log("starting sniffer")
            while self.running:
                sniff(iface = self.iface,prn = packetHandler, count=16)
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
    iface = "enp0s31f6"
    rx = lisener(iface)
    input()
    lisener.stop()