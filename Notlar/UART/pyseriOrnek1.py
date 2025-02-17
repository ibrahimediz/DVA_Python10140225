## pip install pyserial
import serial
port = 'COM3' #dev/ttyUSB0 
baud_rate = 9600

seri_port = serial.Serial(
    port = port,
    baudrate=baud_rate,
    timeout=1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print("Seri Port Bağlantısı Kuruldu")
while True:
    seri_port.write("DVAPython".encode("utf-8"))
    seri_port.readline()