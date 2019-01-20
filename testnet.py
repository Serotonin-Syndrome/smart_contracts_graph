import requests
from generators import gen_txid
from collections import defaultdict


def _post(endpoint, data=None):
    r = requests.post('http://localhost:8080' + endpoint, data=data)
    r.raise_for_status()


class TestNet:
    def _add_vertex(self, addr, value, group):
        assert isinstance(addr, str)
        assert isinstance(value, int)
        assert isinstance(group, str)

        self._ids[addr] = len(self._ids)
        _post('/add-vertex', {'value': str(value), 'group': group, 'title': addr})

    def __init__(self, balances):
        assert isinstance(balances, dict)

        _post('/reset')

        self._ids = {}
        self._balances = {}
        self._contract_addr = None

        for k, v in balances.items():
            assert isinstance(k, str)
            assert isinstance(v, int)

            self._add_vertex(k, value=v, group='1')
            self._balances[k] = v

        _post('/ready')

    def _transfer(self, from_addr, to_addr, amount):
        assert isinstance(from_addr, str)
        assert isinstance(to_addr, str)
        assert isinstance(amount, int)

        if from_addr not in self._balances:
            raise ValueError('from_addr does not exist')

        if self._balances[from_addr] < amount:
            raise ValueError('not enough balance')

        self._balances[from_addr] -= amount
        if to_addr not in self._balances:
            self._balances[to_addr] = 0
            self._add_vertex(to_addr, value=0, group='2')
        self._balances[to_addr] += amount

        _post('/add-edge', {
            'from':     self._ids[from_addr],
            'to':       self._ids[to_addr],
            'value':    amount,
            'title':    '{amount} FTM at {txid}'.format(amount=amount, txid=gen_txid()),
        })

    def deploy(self, contract_cls, creator_addr, contract_addr, amount, *args, **kwargs):
        self._transfer(creator_addr, contract_addr, amount)
        self._contract_addr = contract_addr
        self._contract = contract_cls(self, creator_addr, contract_addr, amount, *args, **kwargs)

    def pay(self, addr, amount):
        assert self._contract_addr is not None
        self._transfer(self._contract_addr, addr, amount)

    def call_method(self, method, sender, amount, args):
        self._transfer(sender, self._contract_addr, amount)
        return getattr(self._contract, method)(sender, amount, *args)
