#
# Makefile - a common build script for native `hello` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

JC=javac
JCFLAGS=
LDLIBS = -lstdc++

PROGRAMS = hello_c hello_cpp Hello.class
OBJECTS = hello_c.o hello_cpp.o Hello.class

all: $(PROGRAMS)

clean:
	-@$(RM) $(OBJECTS)

distclean: clean
	-@$(RM) $(PROGRAMS)

%.class : %.java
	$(JC) $(JCFLAGS) $<

hello_c : hello_c.o
hello_c.o : hello_c.c

hello_cpp : hello_cpp.o
hello_cpp.o : hello_cpp.cpp

Hello.class : Hello.java

# EOF
