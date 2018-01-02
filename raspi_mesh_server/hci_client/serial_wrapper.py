import serial
import binascii

ser = serial.Serial()
on_line_function = None

def run():
    res = None
    line = ser.readline().decode("utf-8")
    if(len(line)):
        line = line.replace('\r','')
        line = line.replace('\n','')
        on_line_function(line)
    return res

def read_serial_line():
    res = None
    line_type = ser.read()
    if(len(line_type)):
        if(line_type == 'b'):
            print("getting a binary line:")
            line_size = ser.read()
            line = ser.read(line_size)
            print(binascii.hexlify(line))
        else:
            print("getting a text line:")
            #line = ser.readline().decode("utf-8")[1:]
            line = ser.readline()
            print(binascii.hexlify(line))
            #print(line)
    return res

def send(data):
    msg = bytearray(b'b')
    print("data:",data)
    print("type:",type(data))
    if(isinstance(data,tuple)):
        msg.append(len(data)+1)
        for d in data:
            msg.append(d)
    else:
        #in this case it is one byte, so + size = 2
        msg.append(2)
        msg.append(data)
    print(msg)
    ser.write(msg)         # then comes the data
    return

def serial_start(config,serial_on_line):
    global on_line_function
    on_line_function = serial_on_line
    global ser
    ser = serial.Serial(config["serial"]["port"],
                        config["serial"]["baud"],
                        timeout=0.1)
    print(ser.name)
    return ser
