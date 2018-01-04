from pyretic.lib.corelib import *
from pyretic.modules.mac_learner import *

def main():
	ip1=IPAddr('10.0.0.3')
	ip2=IPAddr('10.0.0.4')
	mac1=EthAddr('00:00:00:00:00:01')
	policy1=if_(match(srcip=ip1),drop,mac_learner)
	#policy1=if_(match(dstip=ip1),drop,mac_learner)
	policy2=if_(match(dstip=ip2),drop,mac_learner)
	#policy2=if_(match(dstip=ip2),drop,mac_learner)
	policy3=if_(match(srcmac=mac1),drop,mac_learner)
	policy4=if_(match(dstmac=mac1),drop,mac_learner)
	return policy1>>policy2>>policy3>>policy4