#
# Makefile - a common build script for native `fizzbuzz` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

LDLIBS = -lstdc++

PROGRAMS = fizzbuzz_c fizzbuzz_cpp
OBJECTS = fizzbuzz_c.o fizzbuzz_cpp.o

all: $(PROGRAMS)

clean:
	-@$(RM) $(OBJECTS)

distclean: clean
	-@$(RM) $(PROGRAMS)

fizzbuzz_c : fizzbuzz_c.o
fizzbuzz_c.o : fizzbuzz_c.c

fizzbuzz_cpp : fizzbuzz_cpp.o
fizzbuzz_cpp.o : fizzbuzz_cpp.cpp

# EOF
