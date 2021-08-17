#GPIO Test

from logging import info
from device import CyUSBSerial, CyGPIO
from cffi import FFI

from header import src as cdef_src


def main():
    print("Starting...")

    #below line will throw error if driver is not installed
    lib = CyUSBSerial(lib="cyusbserial")

    #Getting the connected Cy7c65215 device
    dev = lib.find()

    ffi = FFI()
    ffi.cdef(cdef_src)
    info = ffi.new("CY_DEVICE_INFO *")
    api = ffi.dlopen("cyusbserial")
    api.CyLibraryInit()
    
    dev_handle = ffi.new("CY_HANDLE *")

    print(api.CyGetDeviceInfo(0, info))
    print(info.vidPid.vid)
    print(info.manufacturerName)
    print(info.vidPid.pid)

    nr = ffi.new("UINT8 *")


    rc = api.CyOpen(0, 5, dev_handle)
    rc = api.CySetGpioValue(dev_handle, 16, 1)
    

    print("end")
    #GPIO Test
    #gpio = CyGPIO(dev)
    #gpio.get(6)
    #gpio.set(6, 1)
    #gpio.get(6)

if __name__ == "__main__":
    main()