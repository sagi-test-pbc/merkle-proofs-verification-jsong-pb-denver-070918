
# Verifying a Merkle Root

### Try it

#### Verify a Merkle Proof
Transaction Hash:
```
e8270fb475763bc8d855cfe45ed98060988c1bdcad2ffc8364f783c98999a208
```

Index:
```
6
```

Merkle Root:
```
4297fb95a0168b959d1469410c7527da5d6243d99699e7d041b7f3916ba93301
```

Merkle Proof:
```
9ed0a5430b5b530822b1ce1b2b9a03d513c888aaa3f028f041bf143efd8c1b92
1dc4b438b3a842bcdd46b6ea5a4aac8d66be858b0ba412578027a1f1fe838c51
156f3662b07aaa4a0d9762faaa8c18afe4c211ff92eb1eae1952aa66627bbf2e
524c93c6dd0874c5fd9e4e57cfe83176e3c2841c973afb4043d225c22cc52983
```


```python
# Exercise 8.1

from block import Proof
from helper import double_sha256, merkle_root, merkle_path, merkle_parent

tx_hash = bytes.fromhex('e8270fb475763bc8d855cfe45ed98060988c1bdcad2ffc8364f783c98999a208')
merkle_root = bytes.fromhex('4297fb95a0168b959d1469410c7527da5d6243d99699e7d041b7f3916ba93301')
proof_hex_hashes = [
    '9ed0a5430b5b530822b1ce1b2b9a03d513c888aaa3f028f041bf143efd8c1b92',
    '1dc4b438b3a842bcdd46b6ea5a4aac8d66be858b0ba412578027a1f1fe838c51',
    '156f3662b07aaa4a0d9762faaa8c18afe4c211ff92eb1eae1952aa66627bbf2e',
    '524c93c6dd0874c5fd9e4e57cfe83176e3c2841c973afb4043d225c22cc52983',
]
proof_hashes = [bytes.fromhex(x) for x in proof_hex_hashes]
index = 6

# get the current hash (reverse tx_hash as it needs to be little endian)
current = tx_hash[::-1]
# initialize the current_index to the index
current_index = index
# loop through proof hashes
for proof_hash in proof_hashes:
    # if current_index is odd, proof_hash is on the left
    if current_index % 2 == 1:
        current = merkle_parent(proof_hash, current)
    # if current_index is even, proof_hash is on the right
    else:
        current = merkle_parent(current, proof_hash)
    # update current_index to be integer divide by 2
    current_index //= 2
# see if the current one reversed is the same as merkle root
print(current[::-1] == merkle_root)
```

### Test Driven Exercise


```python
from io import BytesIO
from block import Block, Proof

class Proof(Proof):

    def verify(self):
        '''Returns whether this proof is valid'''
        # current hash starts with self.tx_hash, reversed
        current = self.tx_hash[::-1]
        # initialize the current_index to be the index at at base level
        current_index = self.index
        # Loop through proof hashes
        for proof_hash in self.proof_hashes:
            # if current_index is odd, proof_hash goes on left
            if current_index % 2 == 1:
                # current hash becomes merkle parent of proof_hash and current
                current = merkle_parent(proof_hash, current)
            # if current_index is even, proof_hash goes on right
            else:
                # current hash becomes merkle parent of current and proof_hash
                current = merkle_parent(current, proof_hash)
            # update the current_index to be integer divide by 2
            current_index //= 2
        # if final result reversed is equal to merkle_root, return True
        return current[::-1] == self.merkle_root
```
