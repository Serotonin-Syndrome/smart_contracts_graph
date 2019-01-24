#include "testnet.h"
#include "common.h"
#include <map>

class MyContract
{
    ITestnet *testnet_;

public:
    MyContract(ITestnet *testnet, Address /*creator*/, Address /*my*/, Balance /*amount*/)
        : testnet_(testnet)
    {
    }

    void ping(Address sender, Balance amount)
    {
        // send it back
        testnet_->pay(sender, amount);
    }
};

int main()
{
    static const Address CREATOR_ADDR    = 123;
    static const Address CONTRACT_ADDR   = 999;
    static const Address USER_ADDR_START = 500;
    static const int nusers = 5;

    auto balances = std::map<Address, Balance>{{CREATOR_ADDR, 5000}};
    for (int i = 0; i < nusers; ++i) {
        balances[USER_ADDR_START + i] = 1000;
    }

    auto testnet = new TestNet<MyContract>(balances);

    testnet->deploy(CREATOR_ADDR, CONTRACT_ADDR, 900);

    for (int i = 0; i < nusers; ++i) {
        testnet->call_method(&MyContract::ping, USER_ADDR_START + i, 500);
    }
}
