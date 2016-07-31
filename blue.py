import bluetooth

target_name = "HC-05" 
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
	if target_name == bluetooth.lookup_name( bdaddr ):
	        target_address = bdaddr	
		break
	


port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((target_address, port))

sock.send("H")

sock.close()
