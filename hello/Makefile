#
# Makefile - a common build script for native `hello` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

LDLIBS = -lstdc++

PROGRAMS = hello_c hello_cpp
OBJECTS = hello_c.o hello_cpp.o

all: $(PROGRAMS)

clean:
	-@$(RM) $(OBJECTS)

distclean: clean
	-@$(RM) $(PROGRAMS)

hello_c : hello_c.o
hello_c.o : hello_c.c

hello_cpp : hello_cpp.o
hello_cpp.o : hello_cpp.cpp

# EOF
