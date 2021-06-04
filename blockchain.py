

import hashlib
# previous hash , tag , transaction amount , next hash
h = hashlib.sha256('GENESIS'.encode())
blockchain = [[1, 'GENESIS BLOCK', 1000000000, h.hexdigest()]]

def generate_hash(a):
    h = hashlib.sha256(a.encode())
    return h.hexdigest()

def add_value(transaction = []):
    if len(transaction) < 4:
        raise ValueError('Empty transaction')
    blockchain.append(transaction)
    


add_value([blockchain[-1][-1], 'Wire transfer for lemons', 5000.00, generate_hash('lemons')])
add_value([blockchain[-1][-1], 'Wire transfer for leather belts', 502.00, generate_hash('belts')])
add_value([blockchain[-1][-1], 'Card purchase of burger', 8.00, generate_hash('burger')])

print(blockchain)