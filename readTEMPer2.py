import hid
import time
VENDOR_ID=13651 # This is TEMPer2 vendor_id, change as needed
PRODUCT_ID=40961 # This is TEMPer2 product_id, change as needed

# TEMPer2 has 2 interfaces: interface_number 1 and 2
# Seems that number 1 is the one
devices = hid.enumerate()
interfaces=[]
for device in devices:
        if device['vendor_id'] == VENDOR_ID and device['product_id'] == PRODUCT_ID:
            interfaces.append(device)
print(interfaces)

# Getting interface_number 1
for i in interfaces:
    if i['interface_number'] == 1:
        sensor=i
print("Interface_number 1:")
print(sensor)

# Open interface 1
device = hid.device()
device.open_path(sensor["path"])
COMMAND = [0x01, 0x80, 0x33, 0x01, 0x00, 0x00, 0x00, 0x00]
device.write(COMMAND) # ask TEMPer2 for data
time.sleep(0.1) # wait some little time 
data0 = device.read(8) # Internal sensor
data1 = device.read(8) # External sensor
print(data0)
print(data1)

temp0 = ((data0[2] << 8) + data0[3]) / 100 # To Celsius
temp1 = ((data1[2] << 8) + data1[3]) / 100 # To Celsius
print(f"Temperatura Int.: {temp0:.2f}°C")
print(f"Temperatura Ext.: {temp1:.2f}°C")
