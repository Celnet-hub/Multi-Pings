# Multi-Pings
This script will automate ping tests to multiple network nodes instead of having to ping 10 or 20 IP addresses individually. This script is my first project and my introduction to the realm of **software** :nerd_face:. Show me some encouragement by staring :smile:.

# Modules Used

```python
import csv
import os
import time
from datetime import datetime
```

# File Handling
The script runs by first opening a CSV file using the ```open()``` function then assigning the return value to a variable as seen below:
```python
lagos = open('Lagos_DCN.csv', 'r',)
accra = open('Accra_DCN.csv', 'r',)
seixal = open('Seixal_DCN.csv', 'r',)
civ = open('CIV_DCN.csv', 'r',)
```
#### Then these files are read using ```csv.reader()``` as seen below: 

```python
lagos_dcn = csv.reader(lagos)
accra_dcn = csv.reader(accra)
seixal_dcn = csv.reader(seixal)
civ_dcn = csv.reader(civ)
```
```csv.reader()``` will return an iterable object and assign it to variale as above. You can find more information in the [python documentation](https://docs.python.org/3/library/csv.html)

#### A function was now created to handle pings to IP addresses read from the CSV file as seen below:

```python
def run_ping(ip_address):
    ping_reply = os.system('ping -n 3 ' + ip_address)
    return ping_reply
```

#### Then the function below will save ping status of IP addresses that are not reachable to a .txt file then use the ```datetime``` module imported to include the current date to the filename. From the ```os``` module ```os.makedirs()``` function is used to create a directory within the script's directory. 

```python
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
```
* since ```f.write()``` function does not wirte list rather strings, there was a need to iterate through a list of ping status. 

# Usage
* #### Note: A list was created to hold ping status. 
```python
# * This list holds the nodes that are not reachable. 
statusList = []
```
#### The code below does the whole magic. So, with ```lagos_dcn = csv.reader(lagos)``` object:
```python
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
        time.sleep(2)
saveResult('Lagos_DCN', statusList)
statusList.clear()
lagos.close()
```
* #### Note: 
  * since I was dealing with network devices already in **production** and due to security, I didn't want to run simultanous pings to those devices which may cause the network       device to think that a DDOS attack is coming in then trigger a shutdown :cold_sweat:. So, I used ```time.sleep(2)``` to delay pings to the next device in the CSV file by **2 seconds**
  * since I am working with 4 CSV file, I decided to reuse the same ```statusList = []``` to hold the result of all unreachable nodes in each file. to achieve this, I clear the entire the **list** after each iteration using ```statusList.clear()```.

