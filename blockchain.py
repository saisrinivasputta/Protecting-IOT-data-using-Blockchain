from datetime import datetime
import hashlib
import json
from uuid import uuid4
from ecdsa import keys,curves
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.transactions=[]

    # def create_genesis_block(self): 
    #     the_time= datetime.now()
    #     block = {}
    #     block['index'] = 1
    #     block['prev_hash'] = "0000000000"
    #     block['timestamp'] = the_time.strftime('%Y-%M-%d %H:%M:%S.%f')
    #     block['data'] = "This is the genesis black of skolo-online python blockchain"
    #     encoded_block = json.dumps(block, sort_keys = True).encode()
    #     new_hash=hashlib.sha256(encoded_block).hexdigest()
    #     block['hash'] = new_hash
    #     self.chain.append(block)

    def add_transaction_to_pool(self,transaction, public_key, signature):
        encoded_transaction = json.dumps(transaction,sort_keys=True).encode() 
        is_valid = public_key.verify(signature,encoded_transaction)
        if is_valid:
            self.transactions.append(transaction)
            return True
        else:
            return False

    def mine_new_block(self):
        the_time = datetime.now()
        block = {}
        if(len(self.chain)==0):
            block['index'] = 1
            block['prev_hash'] = "00000000"
            block['data'] = self.transactions
            block['timestamp'] = the_time.strftime('%Y-%M-%d %H:%M:%S.%f')
            encoded_block = json.dumps (block, sort_keys = True).encode()
            new_hash=hashlib.sha256(encoded_block).hexdigest()
            block['hash'] = new_hash
            self.chain.append(block)
            self.transactions=[]
        else:
            block['index'] = len(self.chain) + 1
            block['prev_hash'] = self.chain[-1]['hash']
            block['data'] = self.transactions
            block['timestamp'] = the_time.strftime('%Y-%M-%d %H:%M:%S.%f')
            encoded_block = json.dumps (block, sort_keys = True).encode()
            new_hash=hashlib.sha256(encoded_block).hexdigest()
            block['hash'] = new_hash
            self.chain.append(block)
            self.transactions=[]