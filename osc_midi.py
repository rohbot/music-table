from OSC import OSCServer
import sys
from time import sleep
import rtmidi_python as rtmidi


midi_out = rtmidi.MidiOut()
for port_name in midi_out.ports:
    print port_name

midi_out.open_port(1)


server = OSCServer( ('0.0.0.0', 9995) )
server.timeout = 0
run = True

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

# funny python's way to add a method to an instance of a class
import types
server.handle_timeout = types.MethodType(handle_timeout, server)

def bottle_callback(path, tags, args, source):
	bottle = int(path[7:])
	val = args[0]
	note = bottle + 40
	print 'bottle', bottle, note, val
		
	if val >= 1:
		midi_out.send_message([0x91, note, 100]) # Note on
	else:
		midi_out.send_message([0x81, note, 100]) # Note off
	
	#print bottle, val
	
def drum_callback(path, tags, args, source):
    print path, tags, args, source

def laser_callback(path, tags, args, source):
    print path, tags, args, source

	
def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

server.addMsgHandler( "/bottle0", bottle_callback )
server.addMsgHandler( "/bottle1", bottle_callback )
server.addMsgHandler( "/bottle2", bottle_callback )
server.addMsgHandler( "/bottle3", bottle_callback )
server.addMsgHandler( "/bottle4", bottle_callback )
server.addMsgHandler( "/bottle5", bottle_callback )
server.addMsgHandler( "/bottle6", bottle_callback )
server.addMsgHandler( "/bottle7", bottle_callback )
server.addMsgHandler( "/bottle8", bottle_callback )


server.addMsgHandler( "/drum0", drum_callback )
server.addMsgHandler( "/drum1", drum_callback )
server.addMsgHandler( "/drum2", drum_callback )
server.addMsgHandler( "/drum3", drum_callback )
server.addMsgHandler( "/drum4", drum_callback )

server.addMsgHandler( "/laser0", laser_callback )
server.addMsgHandler( "/laser1", laser_callback )
server.addMsgHandler( "/laser2", laser_callback )
server.addMsgHandler( "/laser3", laser_callback )
server.addMsgHandler( "/laser4", laser_callback )
server.addMsgHandler( "/laser5", laser_callback )
server.addMsgHandler( "/laser6", laser_callback )
server.addMsgHandler( "/laser7", laser_callback )
server.addMsgHandler( "/laser8", laser_callback )
server.addMsgHandler( "/laser9", laser_callback )
server.addMsgHandler( "/laser10", laser_callback )


server.addMsgHandler( "/quit", quit_callback )

# user script that's called by the game engine every frame
def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

# simulate a "game engine"
while run:
    # do the game stuff:
    #sleep(1)
    # call user script
    each_frame()

server.close()