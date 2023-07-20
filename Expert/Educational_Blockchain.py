import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    return hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}".encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def is_valid_block(new_block, previous_block):
    if previous_block.index + 1 != new_block.index:
        return False
    if previous_block.hash != new_block.previous_hash:
        return False
    if calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data) != new_block.hash:
        return False
    return True

# Create the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add to the chain
num_blocks_to_add = 10

# Mining process
for i in range(num_blocks_to_add):
    new_block_data = f"Block #{i + 1}"
    new_block = create_new_block(previous_block, new_block_data)
    if is_valid_block(new_block, previous_block):
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} has been added to the blockchain!")
    else:
        print("Invalid block! The blockchain is compromised.")
        break
