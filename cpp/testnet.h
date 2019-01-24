#ifndef testnet_h_
#define testnet_h_

#include <stdlib.h>
#include <assert.h>
#include <map>
#include <utility>
#include <memory>
#include <exception>
#include <string>
#include "common.h"
#include "fmtr.h"
#include "rest.h"
#include "itestnet.h"

class NotEnoughBalance : public std::exception
{
    std::string msg_;
public:

    NotEnoughBalance(Address from, Address to, Balance amount)
        : msg_(Fmtr()
            .append("not engouh balance to transfer ").append(amount)
            .append("from ").append(from)
            .append("to ").append(to)
            .get())
    {}

    virtual const char * what() const noexcept override
    {
        return msg_.c_str();
    }
};

template<class Contract>
class TestNet : public ITestnet
{
    std::map<Address, Balance> balances_;
    std::map<Address, size_t> ids_;
    std::unique_ptr<Contract> contract_;
    Address contract_addr_;

    void add_vertex_(Address addr, Balance value, char group)
    {
        const auto size = ids_.size();
        ids_[addr] = size;

        PostRequest{"/add-vertex"}
            .add_field("value", value)
            .add_field("group", group)
            .add_field("title", addr)
        .send();
    }

    void transfer_(Address from, Address to, Balance amount)
    {
        if (!amount) {
            return;
        }

        auto F = balances_.find(from);
        if (F == balances_.end() || F->second < amount) {
            throw NotEnoughBalance{from, to, amount};
        }

        auto T = balances_.find(to);
        if (T == balances_.end()) {
            add_vertex_(to, 0, '2');
            T = balances_.insert({to, 0}).first;
        }

        F->second -= amount;
        T->second += amount;

        PostRequest{"/add-edge"}
            .add_field("from",  ids_[from])
            .add_field("to",    ids_[to])
            .add_field("value", amount)
            .add_field("title", amount)
        .send();
    }

public:
    TestNet(const std::map<Address, Balance> &balances)
        : balances_(balances)
    {
        PostRequest{"/reset"}.send();
        for (const auto &p : balances) {
            add_vertex_(p.first, p.second, '1');
        }
        PostRequest{"/ready"}.send();
    }

    template<class ...Args>
    void deploy(Address creator_addr, Address contract_addr, Balance amount, Args&& ...args)
    {
        assert(!contract_);
        transfer_(creator_addr, contract_addr, amount);
        contract_addr_ = contract_addr;
        contract_.reset(new Contract(
            this, creator_addr, contract_addr, amount, std::forward<Args>(args)...));
    }

    void pay(Address whom, Balance amount) override
    {
        assert(contract_);
        transfer_(contract_addr_, whom, amount);
    }

    template<class Method, class ...Args>
    void call_method(Method method, Address sender, Balance amount, Args&& ...args)
    {
        assert(contract_);
        transfer_(sender, contract_addr_, amount);
        (contract_.get()->*method)(sender, amount, std::forward<Args>(args)...);
    }
};

#endif
