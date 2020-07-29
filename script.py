import csv
import os
import time
from datetime import datetime
asterisks = '*' * 100
asterisks1 = '*' * 10
'''
the code below will open the csv files in read-only format and assign files to respective nodes
'''
lagos = open('Lagos_DCN.csv', 'r',)
accra = open('Accra_DCN.csv', 'r',)
seixal = open('Seixal_DCN.csv', 'r',)
civ = open('CIV_DCN.csv', 'r',)

# Function to ping IP addresses.
def run_ping(ip_address):
    ping_reply = os.system('ping -n 1 ' + ip_address)
    return ping_reply
# Function to save ping results. 
def saveResult(nodeName, NodeStatus):
    name = nodeName + ' on ' + datetime.now().strftime('%d-%m-%Y')
    filename = "Result/%s.txt"% name
    if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError:
                   pass
    with open(filename, "x") as f:
        for items in NodeStatus:
            f.write(items + '\n')

# * This list holds the nodes that are not reachable. 
statusList = []

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
print('\n'+ asterisks + '\nLAGOS DCN Connectivity test' + '\n'+ asterisks)
print('\nOpening LAGOS DCN Nodes...........')
time.sleep(3)
for row in lagos_dcn:
    if row[0] == 'name':
        pass
    else:
        print('\n' + asterisks1 + ' Running pings on {} '.format(row[0]) + asterisks1)
        if run_ping(row[1]) == 1:
            stat = '{}'.format(row[0]) + ' is not reachable'
            statusList.append(stat)
        time.sleep(1.9)
saveResult('Lagos_DCN', statusList)
statusList.clear()
lagos.close()



'''
ACCRA DCN Connectivity test
'''
print('\n' + asterisks + '\nACCRA DCN Connectivity test' + '\n' + asterisks)
print('\nOpening Accra DCN Nodes...........')
time.sleep(5)
for row in accra_dcn:
    if row[0] == 'name':
        pass
    else:
        print('\n' + asterisks1 + ' Running pings on {} '.format(row[0]) + asterisks1)
        if run_ping(row[1]) == 1:
            stat = '{}'.format(row[0]) + ' is not reachable'
            statusList.append(stat)
        time.sleep(1.9)
saveResult('Accra_DCN', statusList)
statusList.clear()
accra.close()



'''
CIV DCN Connectivity test
'''
print('\n' + asterisks + '\nCIV DCN Connectivity test' + '\n' + asterisks)
print('\nOpening CIV DCN Nodes..........')
time.sleep(5)
for row in civ_dcn:
    if row[0] == 'name':
        pass
    else:
        print('\n' + asterisks1 + ' Running pings on {} '.format(row[0]) + asterisks1)
        if run_ping(row[1]) == 1:
            stat = '{}'.format(row[0]) + ' is not reachable'
            statusList.append(stat)        
        time.sleep(1.9)
saveResult('CIV_DCN', statusList)
statusList.clear()   
civ.close()


'''
SEIXAL DCN Connectivity test
'''
print('\n' + asterisks + '\nSEIXAL DCN Connectivity test'+ '\n' + asterisks)
print('\nOpening SEIXAL DCN Nodes..........')
time.sleep(5)
for row in seixal_dcn:
    if row[0] == 'name':
        pass
    else:
        print('\n' + asterisks1 + ' Running pings on {} '.format(row[0]) + asterisks1)
        if run_ping(row[1]) == 1:
            stat = '{}'.format(row[0]) + ' is not reachable'
            statusList.append(stat)  
saveResult('Seixal_DCN',statusList)
statusList.clear()
seixal.close()
