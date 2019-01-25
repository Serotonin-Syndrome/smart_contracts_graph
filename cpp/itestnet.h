#ifndef itestnet_h_
#define itestnet_h_

#include "common.h"
#include "fmtr.h"
#include <exception>
#include <string>

class NotEnoughBalance : public std::exception
{
    std::string msg_;
public:

    NotEnoughBalance(Address from, Address to, Balance amount)
        : msg_(Fmtr()
            .append("not enough balance to transfer ").append(amount)
            .append("from ").append(from)
            .append("to ").append(to)
            .get())
    {}

    virtual const char * what() const noexcept override
    {
        return msg_.c_str();
    }
};

class ITestnet
{
public:
    virtual void pay(Address whom, Balance amount) = 0;
};

#endif
