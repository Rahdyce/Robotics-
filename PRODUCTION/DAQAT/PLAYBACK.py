import serial
import os
import sys
import time

def addline(line, file):
    file.write(line + '\n')
def add(line, file):
    file.write(line)
def record(line, file):
    file.write(line + '\n')
    print(line)
try:
    while(True):
        try:
            print("Input UART COM number (COM#):")
            com ="COM" + input()
            print("Input UART baud rate: ")
            rate = int(input())
            timeout = 0.1
            ser = serial.Serial(com,rate,timeout=timeout)
            print("Input number of LOG file to playback: ")
            lognum = int(input())
            break
        except Exception as error:
            print("\nSERIAL COM FAILED TO OPEN. TRY AGAIN.\n")
            print(error)
            continue
    path = os.path.dirname(os.path.abspath(__file__))
    dir_list = os.listdir(path)
    filename = "LOG" + str(lognum) + ".txt"
    filepath = os.path.join(path,filename)
    file = open(filepath, 'r', encoding='utf-8')
    filearr = file.readlines()
    
    logcounter = int(0)
    lognum = int(0)
    for x in dir_list:
        if(x[0:7] == "PLAYLOG"):
            lognum = int(x[7:x.index('.')])
            if(lognum > logcounter):
                logcounter = lognum
    logname = "PLAYLOG" + str(logcounter + 1) + ".txt"
    logpath = os.path.join(path,logname)
    playlog = open(logpath, 'a', encoding='utf-8')
    
    
    outbuffer = bytes()
    print("PRESS CTRL-C TO EXIT.")
    command = "STR"
    dc = 40
    time1 = 0.0
    time2 = 0.0
    for ln in range(len(filearr)):
        if(filearr[ln][0:3] == "CMD" and ln < len(filearr) - 3):
            time1 = time.time()
            command = filearr[ln][filearr[ln].index('A'):filearr[ln].index('Z')+1] + '\n'
            dc = int(filearr[ln + 2][filearr[ln + 2].index('DC: ') + 4:filearr[ln + 2].index('\n')])
            dc = float(dc / 1000.0)
            outbuffer = command.encode('utf-8')
            record("sending: " + str(outbuffer), playlog)
            ser.write(outbuffer)
            while(True):
                inbuffer = ser.readline()
                instr = str(inbuffer,"UTF-8")
                instr = instr.replace("\r\n", "\n")
                if(str(inbuffer) != "b''"):
                    record(instr, playlog)
                    break
            time2 = time.time()
            dt = time2 - time1
            delay = dc - dt
            if(delay < 0):
                delay = 0.04
            time.sleep(delay)
    file.close()
    ser.close()
except KeyboardInterrupt:
    print('Interrupted')
    file.close();
    ser.close();
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)

