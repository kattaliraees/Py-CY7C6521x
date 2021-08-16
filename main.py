#GPIO Test

from device import CyUSBSerial, CyGPIO

def main():
    print("Starting...")

    #below line will throw error if driver is not installed
    lib = CyUSBSerial(lib="cyusbserial")

    #Getting the connected Cy7c65215 device
    dev = lib.find().next()

    #GPIO Test
    gpio = CyGPIO(dev)
    gpio.set(5, 1)
    gpio.get(5)

if __name__ == "__main__":
    main()