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
            print("Input number of LOG file to ingest: ")
            lognum = int(input())
            print("Input number of tolerable repeated ticks: ")
            tolerance = int(input())
            break
        except Exception as error:
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
        if(x[0:4] == "CLOG"):
            lognum = int(x[4:x.index('.')])
            if(lognum > logcounter):
                logcounter = lognum
    logname = "CLOG" + str(logcounter + 1) + ".txt"
    logpath = os.path.join(path,logname)
    clog = open(logpath, 'a', encoding='utf-8')
    
    
    outbuffer = bytes()
    command1 = "STR"
    command2 = "STR"
    repcount = 0
    for ln in range(len(filearr)):
        if(filearr[ln][0:3] == "CMD" and ln < len(filearr) - 6):
            command1 = filearr[ln][filearr[ln].index('A'):filearr[ln].index('Z')+1] + '\n'
            command2 = filearr[ln + 3][filearr[ln + 3].index('A'):filearr[ln + 3].index('Z')+1] + '\n'
            if (command1 == command2):
                repcount += 1
            else:
                repcount = 0
            if(not repcount > tolerance):
                #print(repcount)
                add(filearr[ln], clog)
                add(filearr[ln + 1], clog)
                add(filearr[ln + 2], clog)
            else:
                #print("SKIPPED")
                continue
    clog.close()
    clog = open(logpath, 'r', encoding='utf-8')
    clogarr = clog.readlines()
    print('\nCondensed ' + filename + ' and saved as ' + logname +'.')
    print('\nOf ' + str(len(filearr)) + ' lines, ' + str(len(clogarr)) + ' lines were removed.')
    print('\nA reduction of ' + str(int((float(len(filearr) - len(clogarr)))/float(len(filearr)) * 100.0)) + '%.')
    file.close()
    clog.close()
except KeyboardInterrupt:
    print('Interrupted')
    file.close();
    clog.close();
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)

