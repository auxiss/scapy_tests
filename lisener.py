from scapy.all import *
import pktManipulator
import logger
import time
import pktModifyer
import pktSender

class lisener:

    def __init__(self,iface) -> None:
        self.running = True

        self.pktBuffer = []
        self.iface = iface


        def sniffer(self):

            def packetHandler(pkt):

                while len(self.pktBuffer) >= 1024: #whait for buffer to be procesed
                    print("Buffer max reached!")
                    print(len(self.pktBuffer))
                    time.sleep(0.1)


                modPkt = pktManipulator.filter(pkt,"DNS") #keep the dns packets only


                if modPkt != None:
                    self.pktBuffer.append(modPkt)


                
                #logger.log("buffer size: "+str(len(self.pktBuffer)))





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
                #logger.log("buffer read")
                return rcvedPkt
            except:
                logger.log("failed reading buffer!")
                return None

        


if __name__ == "__main__":
    import time
    iface = "wlx00c0cab26f0a"
    rx = lisener(iface)

    while True:

        pkt = rx.BufferRead()
        if pkt != None:
            try:
                
                #pkt = pktModifyer.getDnsQues(pkt)
                #pktManipulator.show(pkt)
                response = pktSender.getResponse(pkt)
                #pktManipulator.show(response)
                pktSender.sendResponse(response,pkt)

            except:
                pass

    
    input()
    rx.stop()