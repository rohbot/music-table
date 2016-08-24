import OSC
import time
c = OSC.OSCClient()
c.connect(('127.0.0.1', 9995))   # connect to SuperCollider

NUM_BOTTLES = 8
def send_msg(addr, val):
	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/" + addr)
	oscmsg.append(val)
	c.send(oscmsg)
	print oscmsg
	
for i in range(NUM_BOTTLES):
	send_msg('bottle' + str(i), 120)
	time.sleep(1)
	send_msg('bottle' + str(i), 0)
	