# TEMPer2
TEMPer2 USB temperature sensor (internal + external) by pcsensor read values with Python

# Linux setting
Instaling hidapi library needed by hid python module (debian based):

        # sudo apt install libhidapi-hidraw0 libhidapi-libusb0

Now install hidapi python module needed in the script readTEMPer2.py:

        pip install hidapi

With # lsusb I get:

        ...
        Bus 001 Device 011: ID 3553:a001 PCsensor TEMPer2
        ...
That is hexadecimal. In decimal:

        'vendor_id': 13651
        'product_id': 40961

Using Python in the conversion:

                >>> hex(13651)
                '0x3553'
                >>> hex(40961)
                '0xa001'

Run the script readTEMPer2.py as root, or as a normal user doing this:

Create the file /etc/udev/rules.d/99-temper.rules

with the content:

        # cat /etc/udev/rules.d/99-temper.rules
        SUBSYSTEM=="usb", ATTRS{idVendor}=="3553", ATTRS{idProduct}=="a001", MODE="0666"

Them run:

        # sudo udevadm control --reload-rules
        # sudo udevadm trigger

Then disconnect and connect again TEMPer2 sensor

Run:

         $ python ./readTEMPer2.py
         
