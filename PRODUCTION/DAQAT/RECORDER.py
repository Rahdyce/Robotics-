import serial
import os
import sys
import time
import keyboard

def addline(line, file):
    file.write(line + '\n')
def add(line, file):
    file.write(line)
def on_press(key): 
    print('Key %s pressed' % key) 

def on_release(key): 
    print('Key %s released' %key) 
try:
    while(True):
        try:
            print("Input UART COM number (COM#):")
            com ="COM" + input()
            print("Input UART baud rate: ")
            rate = int(input())
            timeout = 0.1
            ser = serial.Serial(com,rate,timeout=timeout)
            break
        except Exception as error:
            print("\nSERIAL COM FAILED TO OPEN. TRY AGAIN.\n")
            print(error)
            continue
    path = os.path.dirname(os.path.abspath(__file__))
    dir_list = os.listdir(path)
    logcounter = int(0)
    lognum = int(0)
    save = False
    saver = int(0)
    for x in dir_list:
        if(x[0:3] == "LOG"):
            lognum = int(x[3:x.index('.')])
            if(lognum > logcounter):
                logcounter = lognum
    filename = "LOG" + str(logcounter + 1) + ".txt"
    filepath = os.path.join(path,filename)
    file = open(filepath, 'a', encoding='utf-8')
    
    waycounter = int(0)
    waynum = int(0)
    for x in dir_list:
        if(x[0:6] == "WAYLOG"):
            waynum = int(x[6:x.index('.')])
            if(waynum > waycounter):
                waycounter = waynum
    wayname = "WAYLOG" + str(waycounter + 1) + ".txt"
    waypath = os.path.join(path,wayname)
    waylog = open(waypath, 'a', encoding='utf-8')
    
    counter = 0
    inbuffer = bytes()
    n = 1000000;
    print("\nBEGINNING LOG. PRESS CTRL-C TO EXIT. WILL CLOSE AFTER " + str(n) + " LINES OR " + str(n*timeout) + " SEC AUTOMATICALLY")
    time1 = time.time()
    while(True):
        if keyboard.is_pressed('g'):
            save = True
        inbuffer = ser.readline()
        instr = str(inbuffer,"UTF-8")
        instr = instr.replace("\r\n", "\n")
        if(str(inbuffer) != "b''"):
            print(instr)
            add(instr,file)
            counter += 1
            if(instr[0:3] == "CMD" and save):
                saver = 3
            if(saver > 0):
                add(instr, waylog)
                saver -= 1
                if(saver == 0):
                    save = False
        if(counter >= n):
            print("\nPRINTED TO " + filename + "\nGOODBYE")
            break
    file.close()
    ser.close()
except KeyboardInterrupt:
    dt = time.time() - time1
    print('Interrupted')
    print('Recorded: ' + str(counter) + ' lines.')
    print('Elapsed time: ' + str(int(dt)) + ' seconds.')
    file.close()
    waylog.close()
    ser.close()
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)
