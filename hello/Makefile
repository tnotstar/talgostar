#
# Makefile - a common build script for native `hello` implementations
#

.DEFAULT: all
.PHONY: all clean distclean

all: hello_c

clean:
	-@$(RM) hello.o

distclean: clean
	-@$(RM) hello_c

hello_c : hello.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

hello.o : hello.c

# EOF
