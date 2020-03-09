import serial
import serial.tools.list_ports


def Find_port():
    """
    find_port()：寻找可用端口，返回端口名
    """
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        return 1
    else:
        port_0 = list(port_list[0])
        serialName = port_0[0]  # 端口名
        # print(serialName)
        return serialName


"""
操作端口

"""
ser = serial.Serial("COM3", 9600, timeout=30)
i = 1
while True:
    # 写入AT指令
    ser.write('AT+CMGD={0}\r'.format(i).encode('utf-8'))
    i = i + 1
    if i == 50:
        print("succ")
        break
