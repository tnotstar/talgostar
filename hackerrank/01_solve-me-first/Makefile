#
# Makefile - a common build script for native `solve-me-first` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

RM=del
JC=javac
JCFLAGS=
CC=gcc
LDLIBS = -lstdc++

PROGRAMS = $(OBJECTS:.exe=.o) SolveMeFirst.class
OBJECTS = solve-me-first_c.o solve-me-first_c++.o

all: $(PROGRAMS)

clean:
	-@$(RM) $(OBJECTS)

distclean: clean
	-@$(RM) $(PROGRAMS)

%.class : %.java
	$(JC) $(JCFLAGS) $<

solve-me-first_c.exe : solve-me-first_c.c

solve-me-first_c++.exe : solve-me-first_c++.cpp

SolveMeFirst.class : SolveMeFirst.java

# EOF