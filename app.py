import io
from iot import IoT
from blockchain import Blockchain
import csv

iot = IoT()
blockchain = Blockchain()
list1=[]
iotdetails=[]
line_num = 1
def addedtransaction():
    with open('beach-weather-stations-automated-sensors-1.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            len1=0 
            global line_num
            for lines in csvFile:
                if(len1==line_num):
                    if(len(iotdetails)==0):
                        pk,pbk=iot.generate_ECDSA_keys()
                        iotdetails.append([lines[0],pk,pbk])
                        sign = iot.get_signature(" ".join(lines),pk)
                        success = blockchain.add_transaction_to_pool(" ".join(lines),pbk,sign)
                    else:
                        names=[]
                        for l in iotdetails:
                            names.append(l[0])
                        if lines[0] not in names:
                            pk,pbk=iot.generate_ECDSA_keys()
                            iotdetails.append([lines[0],pk,pbk])
                            sign = iot.get_signature(" ".join(lines),pk)
                            success = blockchain.add_transaction_to_pool(" ".join(lines),pbk,sign)
                        else:
                            for l in iotdetails:
                                if lines[0] == l[0]:
                                    sign = iot.get_signature(" ".join(lines),l[1])
                                    success = blockchain.add_transaction_to_pool(" ".join(lines),l[2],sign)
                len1 = len1+1
            line_num = line_num+1
    return success

while True:
    print('1 to send data')
    print('2 to mine block')
    print('3 to print entire blockchain')
    print('4 to print iot deatils')
    print('5 to exit')
    I = input('Enter your choice')
    if I == '1':
        su = addedtransaction()
        if(su):
            print("Transaction added to pool",'\n')
            print(blockchain.transactions)
        else:
            print("Dont change data")
    if I == '2':
        blockchain.mine_new_block()
    if I == '3':
        print('-'*50)
        for bloc in blockchain.chain:
            print(bloc)
            print('-'*50)
    if I == '4':
        print("All iot devices on blockchain")
        for i in iotdetails:
            print(i)
            print('-'*50)
    if I == '5':
        break
