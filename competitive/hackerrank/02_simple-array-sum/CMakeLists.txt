cmake_minimum_required(VERSION 2.8)

project(simple-array-sum)

add_executable(simple-array-sum_c simple-array-sum.c)
add_executable(simple-array-sum_c++ simple-array-sum.cpp)

find_package(Java REQUIRED)
include(UseJava)

add_jar(SimpleArraySum SimpleArraySum.java)
