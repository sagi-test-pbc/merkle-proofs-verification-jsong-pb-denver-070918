from unittest import TestCase
from ipynb.fs.full.index import *

class BlockTest(TestCase):

    def test_verify_merkle_proof(self):
        merkle_root = bytes.fromhex('d6ee6bc8864e5c08a5753d3886148fb1193d4cd2773b568d5df91acc8babbcac')
        tx_hash = bytes.fromhex('77386a46e26f69b3cd435aa4faac932027f58d0b7252e62fb6c9c2489887f6df')
        index = 7
        proof_hex_hashes = [
            '8118a77e542892fe15ae3fc771a4abfd2f5d5d5997544c3487ac36b5c85170fc',
            'ade48f2bbb57318cc79f3a8678febaa827599c509dce5940602e54c7733332e7',
            '26906cb2caeb03626102f7606ea332784281d5d20e2b4839fbb3dbb37262dbc1',
            '00aa9ad6a7841ffbbf262eb775f8357674f1ea23af11c01cfb6d481fec879701',
        ]
        proof_hashes = [bytes.fromhex(x) for x in proof_hex_hashes]
        proof = Proof(merkle_root=merkle_root, tx_hash=tx_hash, index=index, proof_hashes=proof_hashes)
        self.assertTrue(proof.verify())
