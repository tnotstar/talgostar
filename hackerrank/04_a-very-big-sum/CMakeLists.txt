cmake_minimum_required(VERSION 2.8)

project(a-very-big-sum)

add_executable(a-very-big-sum_c a-very-big-sum.c)
add_executable(a-very-big-sum_c++ a-very-big-sum.cpp)

find_package(Java REQUIRED)
include(UseJava)

add_jar(AVeryBigSum AVeryBigSum.java)
