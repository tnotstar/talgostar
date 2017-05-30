cmake_minimum_required(VERSION 2.8)

project(solve-me-first)

add_executable(solve-me-first_c solve-me-first.c)
add_executable(solve-me-first_c++ solve-me-first.cpp)

find_package(Java REQUIRED)
include(UseJava)

add_jar(SolveMeFirst SolveMeFirst.java)
