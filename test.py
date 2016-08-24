import rtmidi_python as rtmidi
import time
import OSC
midi_out = rtmidi.MidiOut()
available_ports = midi_out.ports
print available_ports

midi_out.open_port(1)

def on_note(note):
	print "On: ", note 
	midi_out.send_message([0x91, note, 100]) # Note on

def off_note(note):
	midi_out.send_message([0x81, note, 100]) # Note off

def laser(num, val):
	if val > 0:
		val = 127
	print num,val 
	midi_out.send_message([0xb0,num, val]) # Note on

def laserOff():
	for cc in range(1,11):
		laser(cc,0)

def notesOff():
	for note in range(36,48):
		off_note(note)
		
def knobChange(num, val):
	print num,val
	midi_out.send_message([0xb0,num, val]) # Note on

def knobsOff():
	for i in range(17,23):
		knobChange(i,0)

def bottle(num,val):
	note = num + 40
	print 'bottle', num, note, val
		
	if val >= 1:
		midi_out.send_message([0x91, note, 100]) # Note on
	else:
		midi_out.send_message([0x81, note, 100]) # Note off
		


		
#laserOff()
notesOff()
#knobsOff()

for i in range(4):
	bottle(i,1)
	time.sleep(1)
	bottle(i,0)
	time.sleep(1)


# for i in range(128):
	# knobChange(20,i)
	# knobChange(22,i)
	# knobChange(19,i)

	# time.sleep(0.1)
# knobsOff()

	
# knobChange(17,30)
# time.sleep(3)
# knobChange(17,1)
# time.sleep(3)
# knobChange(17,30)
# time.sleep(3)
# knobChange(17,1)


# for note in range(36,48):
	# on_note(note)
	# time.sleep(1)
	# off_note(note)

# for i in range(1,11):		
	# laser(i,1)	
	# time.sleep(1)	
	# laser(i,0)
	
# laserOff()

	#midi_out.send_message([0xb0, cc, 0]) # Note on
	
	#off_note(i)
