from device import CyUSBSerial, CyGPIO
def main():
    lib = CyUSBSerial(lib="cyusbserial")
    dev = lib.find().next()
    print("Hello World!")
    print(dev)
    gpio = CyGPIO(dev)
    print(gpio)

if __name__ == "__main__":
    main()