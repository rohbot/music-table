import serial
import rtmidi_python as rtmidi
import time

midi_out = rtmidi.MidiOut()
for port_name in midi_out.ports:
    print port_name

midi_out.open_port(1)


ser = serial.Serial('COM15', 115200)
while True:
	line  = ser.readline().strip()
	if len(line) == 2:
		pin = ord(line[0])
		val = ord(line[1])
		print pin, val
		if pin < 40:
			midi_out.send_message([0xb0,pin + 17, val]) # Note on
		else:
			note = pin #+ 40
			print 'Maracas', pin, note, val
				
			if val >= 1:
				midi_out.send_message([0x90, note, 100]) # Note on
			else:
				midi_out.send_message([0x80, note, 100]) # Note off
