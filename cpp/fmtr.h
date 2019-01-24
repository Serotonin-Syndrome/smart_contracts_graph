#ifndef fmtr_h_
#define fmtr_h_

#include <ios>
#include <sstream>
#include <string>

class Fmtr
{
    std::stringstream ss_;
public:

    Fmtr()
        : ss_(std::ios_base::out)
    {}

    template<class T>
    Fmtr& append(const T &value)
    {
        ss_ << value;
        return *this;
    }

    std::string get() const
    {
        return ss_.str();
    }
};

#endif
