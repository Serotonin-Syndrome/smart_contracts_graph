#include "rest.h"
#include "fmtr.h"
#include <curl/curl.h>
#include <stdlib.h>
#include <exception>
#include <string>

class CurlError : public std::exception
{
    std::string msg_;

public:
    CurlError(const char *func, const char *msg)
        : msg_(Fmtr()
            .append(func)
            .append(": ")
            .append(msg)
            .get())
    {}

    virtual const char * what() const noexcept override
    {
        return msg_.c_str();
    }
};

class BadHttpStatus : public std::exception
{
    std::string msg_;

public:
    BadHttpStatus(const std::string &url, long status)
        : msg_(Fmtr()
            .append(url)
            .append(": HTTP status ")
            .append(status)
            .get())
    {}

    virtual const char * what() const noexcept override
    {
        return msg_.c_str();
    }
};

static bool global_curl_inited = false;

static const std::string URL_BASE = "http://localhost:8080";

static size_t ignore_body(char *ptr, size_t size, size_t nmemb, void *userdata)
{
    (void) ptr;
    (void) userdata;
    return size * nmemb;
}

void PostRequest::send()
{
    if (!global_curl_inited) {
        curl_global_init(CURL_GLOBAL_ALL);
        global_curl_inited = true;
    }

    CURL *curl = curl_easy_init();
    if (!curl) {
        throw CurlError("curl_easy_init", "returned nullptr");
    }
    CURLcode r;

    std::string url = URL_BASE + endpoint_;
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

    std::string data = data_.str();
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());

    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, ignore_body);

    if ((r = curl_easy_perform(curl)) != CURLE_OK) {
        throw CurlError("curl_easy_perform", curl_easy_strerror(r));
    }

    long status;
    if ((r = curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &status)) != CURLE_OK) {
        throw CurlError("curl_easy_getinfo", curl_easy_strerror(r));
    }
    if (status != 200) {
        throw BadHttpStatus(url, status);
    }

    curl_easy_cleanup(curl);
}
