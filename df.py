import time
import re
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.modules.mac_learner import mac_learner
from threading import Thread
from pyretic.lib.query import *
from pyretic.modules.hub import hub
class UIFirewall(DynamicPolicy):
        ips=[]
        macs=[]
        flag=0

        def __init__(self):
                super(UIFirewall,self).__init__(true)
                self.policy=mac_learner()
                ob=Thread(target=self.UI_Loop)
                ob.start()

        def UI_Loop(self):
                print "\t\t\t Starting Controller...."
                print "*********************WELCOME TO UI CONTROLLER*********************"

                while True:
                #get argument
                        print "\nUSER CHOICE:\n-->1.Allow IP\n-->2.Block IP\n-->3.Allow MAC\n-->4.Block MAC\n-->5.Exit"
                        print "\n******************************************************************"
                        self.accept_user_choice()

        def accept_user_choice(self):
                try:
                        ch=int(raw_input("Please enter your choice --> "))
                        print "\n"
                        if ch==1:
                                print "******************************************************************"

                                ip_var=raw_input("Enter IP address you want to allow : ")
                                match = re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_var)
                                if match:
									 self.allow_IP(ip_var)
                                else:
                                        print "invalid IP"
                        elif ch==2:
                                print "******************************************************************"
                                ip_var=raw_input("Enter IP address you want to block : ")
                                match = re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_var)
                                if match:
                                        self.block_IP(ip_var)
                                else:
                                        print "invalid IP"

                        elif ch==3:
                                print "******************************************************************"
                                mac_var=raw_input("Enter MAC you want to allow : ")
                                if re.match(r"([\dA-F]{2}(?:[:][\dA-F]{2}){5})",mac_var):
                                        self.allow_MAC(mac_var)
                                else:
                                        print "Invalid MAC"
                        elif ch==4:
                                print "******************************************************************"
                                mac_var=raw_input("Enter MAC you want to block : ")
                                if re.match(r"([\dA-F]{2}(?:[:][\dA-F]{2}){5})",mac_var):
                                        self.block_MAC(mac_var)
                                else:
                                        print "Invalid MAC"
                        elif ch==5:
                                exit()
                        else:
                                print "******************************************************************"
                                print "Invalid choice"
                except ValueError:
                        print "Invalid User Input"

        def allow_IP(self,ip_var):
                #tup_ip=(ip_var)
                flag=0
				print "Allowing ip :",ip_var
                #self.policy=if_(~match(srcip=IPAddr(ip_var)),drop,mac_learner)>>if_(~match(dstip=IPAddr(ip_var)),drop,mac_learner)
                self.policy=if_(match(srcip=IPAddr(ip_var)),mac_learner(),if_(match(dstip=IPAddr(ip_var)),mac_learner(),self.policy))
                print self.policy
                """result=checkAddress(0,ip_var)
                if result=="present":
                        print "IP %s is already allowed"%ip_var
                else:
                        UIFirewall.ips.append(ip_var)
                        self.policy=if_(match(srcip=IPAddr(ip_var)),mac_learner,self.policy)>>if_(match(dstip=IPAddr(ip_var)),mac_learner,self.policy)
                """


                """try:
                index=UIFirewall.ips.index(ip_var)
                print "IP %s is already allowed"%ip_var

                except:
                        UIFirewall.ips.append(ip_var)
                        self.policy=if_(match(srcip==IPAddr(ip_var)),mac_learner,self.policy)
                        print "IP %s is allowed "%ip_var

                finally:
                        print "List of allowed IPs : ",UIFirewall.ips
                """
        def block_IP(self,ip_var):
                tup_ip=(ip_var)
                flag=0
                print "Blocking ip :",ip_var
                self.policy=if_(match(srcip=IPAddr(ip_var)),drop,self.policy)>>if_(match(dstip=IPAddr(ip_var)),drop,self.policy)
                #print self.policy
                """result=checkAddress(0,ip_var)
                if result=="absent":
                        print "IP %s is already blocked"%ip_var
                elif result=="present":
                        UIFirewall.ips.remove(ip_var)
                        self.policy=if_(match(srcip=IPAddr(ip_var)),drop(),mac_learner)>>if_(match(dstip=IPAddr(ip_var)),drop(),mac_learner)
				"""
		
		def allow_MAC(self,mac_var):
                tup_mac=(mac_var)
                flag=1
                print "Allowing MAC:",mac_var
                self.policy=if_(match(srcmac=EthAddr(mac_var)),mac_learner(),if_(match(dstmac=EthAddr(mac_var)),mac_learner(),self.policy))
                """result=checkAddress(1,mac_var)
                if result=="present":
                        print "MAC %s is already allowed"%mac_var
                elif result=="absent":
                        UIFirewall.macs.append(mac_var)
                        self.policy=if_(match(srcmac=EthAddr(mac_var)),mac_learner,self.policy)>>if_(match(dstmac=EthAddr(mac_var)),mac_learner,self.policy)
                """
				
        def block_MAC(self,mac_var):
                tup_mac=(mac_var)
                flag=1
                print "Blocking MAC :",mac_var
                self.policy=if_(match(srcmac=EthAddr(mac_var)),drop,self.policy)>>if_(match(dstmac=EthAddr(mac_var)),drop,self.policy)
                """result=checkAddress(1,mac_var)
                if result=="absent":
                        print "MAC %s is already blocked"%mac_var
                elif result=="present":
                        UIFirewall.macs.append(mac_var)
                        self.policy=if_(match(srcmac=EthAddr(mac_var)),drop,self.policy)>>if_(match(dstmac=EthAddr(mac_var)),drop,self.policy)
                """

        def checkAddress(self,flag,addr):
                if flag==0: #ip
                        for address in UIFirewall.ips:
                                if address==addr:
                                        return "present"

                        return "absent"
                elif flag==1:#mac
                        for address in UIFirewall.macs:
                                if address==addr:
                                        return "present"
						
						 return "absent"
                elif flag==1:#mac
                        for address in UIFirewall.macs:
                                if address==addr:
                                        return "present"

                        return "absent"

def main():
        return UIFirewall()


