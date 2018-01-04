import time
from threading import Thread
class UIFirewall:
    ips=[]
    macs=[]
    
    def __init__(self):
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
                self.allow_IP(ip_var)
            elif ch==2:
                print "******************************************************************"
                ip_var=raw_input("Enter IP address you want to block : ")
                self.block_IP(ip_var)
            elif ch==3:
                print "******************************************************************"
                mac_var=raw_input("Enter MAC you want to allow : ")
                self.allow_MAC(mac_var)
            elif ch==4:
                print "******************************************************************"
                mac_var=raw_input("Enter MAC you want to block : ")
                self.block_MAC(mac_var)
            elif ch==5:
                exit()
            else:
                print "******************************************************************"
                print "Invalid choice"
        except ValueError:
            print "Invalid User Input"

    def allow_IP(self,ip_var):
        tup_ip=(ip_var)
        print "Allowing ip :",tup_ip
        try:
            index=UIFirewall.ips.index(ip_var)
            print "IP %s is already allowed"%ip_var
            
        except:
            UIFirewall.ips.append(ip_var)
            print "IP %s is allowed "%ip_var
            
        finally:
            print "List of allowed IPs : ",UIFirewall.ips

    def block_IP(self,ip_var):
        tup_ip=(ip_var)
        print "Blocking ip :",tup_ip
        try:
            index=UIFirewall.ips.index(ip_var)
            UIFirewall.ips.remove(ip_var)
            print "IP %s is blocked"%ip_var
            
        except:
            print "IP %s is already blocked "%ip_var

        finally:
            print "List of allowed IPs : ",UIFirewall.ips


    def allow_MAC(self,mac_var):
        tup_mac=(mac_var)
        print "Allowing MAC:",tup_mac
        try:
            index=UIFirewall.macs.index(mac_var)
            print "MAC %s is already allowed"%mac_var
            
        except:
            UIFirewall.macs.append(mac_var)
            print "MAC %s is allowed "%mac_var

        finally:
            print "List of allowed MACs : ",UIFirewall.macs

    def block_MAC(self,mac_var):
        tup_mac=(mac_var)
        print "Blocking MAC :",tup_mac
        try:
            index=UIFirewall.macs.index(mac_var)
            UIFirewall.macs.remove(mac_var)
            print "MAC %s is blocked"%mac_var
            
        except:
            print "MAC %s is alredy blocked "%mac_var

        finally:
            print "List of allowed MACs : ",UIFirewall.macs

UI1=UIFirewall()
