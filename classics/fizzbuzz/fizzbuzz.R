#!/usr/bin/Rscript

cat(paste(
    c(sapply(1:100, function(n) {
        ifelse(n %% 15 == 0, "fizzbuzz",
        ifelse(n %%  5 == 0, "buzz",
        ifelse(n %%  3 == 0, "fizz", n)))
    }), ""),
    collapse="\n")
)

# EOF
