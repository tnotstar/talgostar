#
# Makefile - a common build script for native `fizzbuzz` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

all: fizzbuzz_c

clean:
	-@$(RM) fizzbuzz.o

distclean: clean
	-@$(RM) fizzbuzz_c

fizzbuzz_c : fizzbuzz.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

fizzbuzz.o : fizzbuzz.c

# EOF
