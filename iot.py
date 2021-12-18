from datetime import datetime
import hashlib
import json
from uuid import uuid4
from ecdsa import curves,keys
import ecdsa
import base64
from ecdsa import SigningKey

class IoT:

    def generate_ECDSA_keys(self):
        # sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        # private_key = sk.to_string().hex()
        # vk = sk.get_verifying_key() 
        # public_key = vk.to_string().hex()
        private_key = SigningKey.generate() # uses NIST192p
        public_key = private_key.verifying_key
        return [private_key,public_key]

    def create_transaction(self, data):
        transaction_id = str(uuid4()).replace('-','')
        timestamp = str(datetime.now())
        transaction = {}
        transaction ['transaction_id'] = transaction_id 
        transaction ['timestamp'] = timestamp
        transaction['data'] = data
        return transaction

    def get_signature(self, transaction, private):
        encoded_transaction = json.dumps(transaction, sort_keys = True).encode()
        # sk = ecdsa.SigningKey.from_string(bytes.fromhex(private),curve=ecdsa.SECP256k1)
        # signature = base64.b64encode(sk.sign(encoded_transaction))
        signature = private.sign(encoded_transaction)
        return signature