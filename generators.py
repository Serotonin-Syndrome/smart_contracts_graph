import secrets
import os


if os.getenv('PleaseDeterministicIds'):
    _i = 0

    def gen_addr():
        global _i
        _i += 1
        return '{:08x}'.format(_i)


    def gen_txid():
        global _i
        _i += 1
        return '{:010x}'.format(_i)

else:
    def gen_addr():
        return secrets.token_hex(8)


    def gen_txid():
        return secrets.token_hex(10)
