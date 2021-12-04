# ESMB unit tests root CMakeLists.txt
cmake_minimum_required(VERSION 3.14)

project(Tests LANGUAGES CXX)

add_definitions(-DGTEST_LANGUAGE_CXX11)

enable_testing()
