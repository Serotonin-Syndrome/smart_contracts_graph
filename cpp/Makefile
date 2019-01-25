PKGCONFIG_LIBS := libcurl
PROGRAM := main

CXXFLAGS := -Wall -Wextra -std=c++14 -O2 $(shell pkg-config --cflags $(PKGCONFIG_LIBS))
LDLIBS := $(shell pkg-config --libs $(PKGCONFIG_LIBS))
SOURCES := $(wildcard *.cpp)
OBJECTS := $(patsubst %.cpp,%.o,$(SOURCES))

$(PROGRAM): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $@ $(LDLIBS)

%.o: %.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $<

clean:
	$(RM) $(PROGRAM) $(OBJECTS)

.PHONY: clean
