#ifndef itestnet_h_
#define itestnet_h_

#include "common.h"

class ITestnet
{
public:
    virtual void pay(Address whom, Balance amount) = 0;
};

#endif
