from scapy.all import *
import pktManipulator
import logger
import time
import pktModifyer as pktModifyer
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
                
                print("-------new packet--------->>>>\n\n")

                print("client request pkt:")
                pktManipulator.show(pkt)

                print("\nmodifyed client request pkt:" )
                dns_request =pktModifyer.flipSender(pkt)
                pktManipulator.show(dns_request)

                print("\nserver response pkt:")
                response = pktSender.getResponse(dns_request)
                print(type(response))
                pktManipulator.show(response)

                print("\nmodifyed_Response pkt:")
                modifyed_DNS_Response = pktModifyer.flipReciver(response,pkt)
                pktManipulator.show(modifyed_DNS_Response)


                pktSender.sendResponse(modifyed_DNS_Response)

            except:
                pass

    
    input()
    rx.stop()