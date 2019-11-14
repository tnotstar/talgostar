#
# Makefile - a common build script for native `sum-of-n-1` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

CC = gcc
CFLAGS =
LDLIBS = -lstdc++
O_SYM = .o
C_SYM = .c
CPP_SYM = .cpp
EXE_SYM = .exe

PROGRAMS = sum-of-n-1_c$(EXE_SYM) sum-of-n-1_cpp$(EXE_SYM)
OBJECTS = $(PROGRAMS:$(EXE_SYM)=$(O_SYM))

all: $(PROGRAMS)

clean:
	-@$(RM) $(OBJECTS)

distclean: clean
	-@$(RM) $(PROGRAMS)

sum-of-n-1_c$(EXE_SYM) : sum-of-n-1_c$(O_SYM)
	$(CC) $(LDFLAGS) $< $(LDLIBS) -o $@

sum-of-n-1_cpp$(EXE_SYM) : sum-of-n-1_cpp$(O_SYM)
	$(CC) $(LDFLAGS) $< $(LDLIBS) -o $@

sum-of-n-1_c$(O_SYM) : sum-of-n-1_c$(C_SYM)
sum-of-n-1_cpp$(O_SYM) : sum-of-n-1_cpp$(CPP_SYM)

$(CPP_SYM).$(O_SYM):
	$(CC) $(CFLAGS) $< -o $@

# EOF