cmake_minimum_required(VERSION 2.8)

project(compare-the-triplets)

add_executable(compare-the-triplets_c compare-the-triplets.c)
add_executable(compare-the-triplets_c++ compare-the-triplets.cpp)

find_package(Java REQUIRED)
include(UseJava)

add_jar(CompareTheTriplets CompareTheTriplets.java)
