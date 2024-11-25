from scapy.all import *
import packetParcer
import logger
import time

class lisener:

    def __init__(self,iface) -> None:
        self.running = True

        self.pktBuffer = []
        self.iface = iface


        def sniffer(self):

            def packetHandler(pkt):

                while len(self.pktBuffer) >= 1024:
                    print("Buffer max reached!")
                    print(len(self.pktBuffer))
                    time.sleep(0.01)

                self.pktBuffer.append(pkt)
                logger.log("buffer size: "+str(len(self.pktBuffer)))

                packetParcer.show(pkt)
                #print(packetParcer.getLayers(pkt))
                #packetParcer.filter(pkt,"a4:a4:90:53:91:a4")
                #print('.')

                #packetParcer.decapsulate(pkt)




            print("starting sniffer")
            logger.log("starting sniffer")

            while self.running:
                sniff(iface = self.iface, prn = packetHandler, count=16)

            print("sniffer stoped")
            logger.log("sniffer stoped")

        
        print("starting sniffer threand")
        logger.log("starting sniffer threand")

        tlisener = Thread(target=sniffer, args=(self,))
        tlisener.start()

        print("sniffer thread statied")
        logger.log("sniffer thread statied")
    

    def stop(self):
        logger.log("stoping sniffer")
        self.running = False



    def BufferRead(self):
        if len(self.pktBuffer) == 0: time.sleep(0.5)
        else:
            #logger.log("reading buffer")

            try:
                #logger.log("buffer size: "+str(len(self.pktBuffer)))
                #logger.log("read element form buffer")
                rcvedPkt = self.pktBuffer.pop(0)
                print("rcvedPkt: "+str(type(rcvedPkt)))
                #logger.log("buffer read")
                return rcvedPkt
            except:
                logger.log("failed reading buffer!")
                return 1

        


if __name__ == "__main__":
    import time
    iface = "enp0s31f6"
    rx = lisener(iface)

    while True:

        if rx.BufferRead():
            pkt = rx.BufferRead()
            print("pkt: "+str(type(pkt)))
            print(pkt)
        
    input()
    rx.stop()