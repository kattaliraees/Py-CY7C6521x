all:
	gcc -fPIC -o libcyusb.o -c cyusb.c -I ../common/header
	gcc -fPIC -o libcyuart.o -c cyuart.c -I ../common/header
	gcc -fPIC -o libcyi2c.o -c cyi2c.c -I ../common/header 
	gcc -fPIC -o libcyspi.o -c cyspi.c -I ../common/header
	gcc -fPIC -o libcyphdc.o -c cyphdc.c -I ../common/header
	gcc -fPIC -o libcyjtag.o -c cyjtag.c -I ../common/header
	gcc -fPIC -o libcymisc.o -c cymisc.c -I ../common/header  
	gcc -fPIC -dynamiclib -o libcyusbserial.0.1.dylib libcyusb.o libcyuart.o libcyi2c.o libcyspi.o libcyphdc.o libcyjtag.o libcymisc.o -l usb-1.0
	cp libcyusbserial.0.1.dylib /usr/local/lib    
	ln -sf /usr/local/lib/libcyusbserial.0.1.dylib /usr/local/lib/libcyusbserial.dylib
	rm -f libcyusbserial.o libcyusb.o libcyuart.o libcyi2c.o libcyspi.o libcyphdc.o libcyjtag.o libcymisc.o
clean:
	rm -f libcyusbserial.dylib libcyusbserial.0.1.dylib
help:
	@echo	'make		would compile and create the library and create a link'
	@echo	'make clean	would remove the library and the soft link to the library (soname)'
