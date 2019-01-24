#ifndef rest_h_
#define rest_h_

#include <ios>
#include <string>
#include <sstream>

class PostRequest
{
    std::string endpoint_;
    std::stringstream data_;
    bool data_empty_;

public:
    PostRequest(const std::string &endpoint)
        : endpoint_(endpoint)
        , data_(std::ios_base::out)
        , data_empty_(true)
    {}

    template<class T>
    PostRequest& add_field(const std::string &key, const T &value)
    {
        if (!data_empty_) {
            data_ << '&';
        }
        data_ << key << '=' << value;
        data_empty_ = false;
        return *this;
    }

    void send();
};

#endif
