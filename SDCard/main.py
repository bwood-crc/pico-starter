import machine
import sdcard
import os

# Set the Chip Select (CS) pin high
cs = machine.Pin(17, machine.Pin.OUT)

# Intialize the SD Card
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(19),
                  miso=machine.Pin(16))
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

# Create a file in write mode and write something
with open("/sd/sdtest.txt", "w") as file:
    file.write("Hello World!\r\n")
    file.write("This is a test\r\n")

# Open the file in read mode and read from it
with open("/sd/sdtest.txt", "r") as file:
    data = file.read()
    print(data)
