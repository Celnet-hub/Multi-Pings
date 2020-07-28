import csv
import os
import time
start = "\033[1m"
end = "\033[0;0m"
'''
the code below will open the csv files in read-only format and assign files to respective nodes
'''
lagos = open('Lagos_DCN.csv', 'r',)  
accra = open('Accra_DCN.csv', 'r',)
seixal = open('Seixal_DCN.csv', 'r',)
civ = open('CIV_DCN.csv', 'r',)

'''
the code below will use the csv.reader() method to read contents of the csv files
'''
lagos_dcn = csv.reader(lagos)
accra_dcn = csv.reader(accra)
seixal_dcn = csv.reader(seixal)
civ_dcn = csv.reader(civ)

'''
LAGOS DCN Connectivity test
'''
print(start + '\nOpening LAGOS DCN Nodes...........' + end)
time.sleep(5)

for row in lagos_dcn:
    if row[0] == 'name':
        pass
    else:
        print(start+'\nPinging {}....'.format(row[0]) + end)
        ping_reply = os.system('ping -n 3 ' + row[1])
        print(ping_reply,'\n')
        time.sleep(1.9)
lagos.close()

connect = input(start + 'Begin Connectivity test for Accra [Y/N]: ' + end)

'''
ACCRA DCN Connectivity test
'''
if connect == 'y' or connect == 'Y':
    print(start+'\nOpening Accra DCN Nodes..............'+end)
    time.sleep(5)

    for row in accra_dcn:
        if row[0] == 'name':
            pass
        else:
            print('Pinging {}....'.format(row[0]))
            ping_reply = os.system('ping -n 3 ' + row[1])
            print(ping_reply, '\n')
            time.sleep(1.9)
else:
    accra.close()

'''
CIV DCN Connectivity test
'''
connect_accra = input(start+'Begin Connectivity test for CIV [Y/N]: '+end)

if connect_accra == 'y' or connect_accra == 'Y':
    print(start+'\nOpening CIV DCN Nodes...........'+end)
    time.sleep(5)

    for row in civ_dcn:
        if row[0] == 'name':
            pass
        else:
            print('\nPinging {}....'.format(row[0]))
            ping_reply = os.system('ping -n 3 ' + row[1])
            print(ping_reply, '\n')
            time.sleep(1.9)
else:
    civ.close()

'''
SEIXAL DCN Connectivity test
'''
connect_seixal = input(start+'Begin Connectivity test for SEIXAL [Y/N]: '+end)

if connect_seixal == 'y' or connect_seixal == 'Y':
    print(start+'\nOpening SEIXAL DCN Nodes...........'+end)
    time.sleep(5)
    
    for row in seixal_dcn:
        if row[0] == 'name':
            pass
        else:
            print('\nPinging {}....'.format(row[0]))
            ping_reply = os.system('ping -n 3 ' + row[1])
            print(ping_reply, '\n')
            time.sleep(1.9)
else:
    seixal.close()
