from web3 import Web3
import json
from time import sleep
import RPi.GPIO as GPIO

web_3=Web3(Web3.HTTPProvider("HTTP://192.168.1.104:7545"))
chainid=5777
address=input("Input your address: ")
private_key=input("Input your privatekey:0x")
host="0x325B899E9490f70af7A87b0d3494A4756eAeD13C"
private_key2="0x09694260e3d87528ebbab2d1fd61d9d24cfd4727ffedb0f6a355b1c8335c27b7"
licence_check = input("Have driving licence? ,yes/no: ")
def lock(x):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, x)
    #Wait 1 Seconds
    sleep(1)

nonce=web_3.eth.getTransactionCount(address)
nonce2=web_3.eth.getTransactionCount(host)

if licence_check =="yes":
    deposit = input("After confirmation you will have to pay a deposit for 30 ETH, yes/no: ")
    if deposit =="yes":
        pay = {
            'nonce': nonce,
            'to': host,
            'value': web_3.toWei(30, 'ether'),
            'gas': 2000000,
            'gasPrice': web_3.toWei('50', 'gwei')
        }

        #sign the transaction
        signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

        #send transaction
        pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
        print("Deposition succeed")   
    
        day=input("How many days: ")
        if day == "1":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(5, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 1 day")

        if day == "3":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(10, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 3 days")
            
        if day == "7":
            pay = {
                'nonce': nonce+1,
                'to': host,
                'value': web_3.toWei(20, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You rent 7 days")
            
        lock(0)
        
        late=input("Did you turn in late?, yes/no: ")
        if late == "yes":
            pay = {
                'nonce': nonce+2,
                'to': host,
                'value': web_3.toWei(5, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You have to pay 5 ETH for turn in late")
                        
        if late == "no":
            pay = {
                'nonce': nonce2,
                'to': address,
                'value': web_3.toWei(30, 'ether'),
                'gas': 2000000,
                'gasPrice': web_3.toWei('50', 'gwei')
            }

            #sign the transaction
            signed_pay = web_3.eth.account.sign_transaction(pay, private_key2)

            #send transaction
            pay_hash = web_3.eth.sendRawTransaction(signed_pay.rawTransaction)
            print("You recieved deposit back")
                       
    if deposit =="no":
        print("Deposition failed")
        
   lock(1)
    
if licence_check =="no":
    print("You don't have permission to drive")
    
lock(1)
