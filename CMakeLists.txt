cmake_minimum_required(VERSION 2.6)

project(SomeProject)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

include_directories(${CMAKE_SOURCE_DIR})

find_package(PythonInterp REQUIRED)
include_directories(${PythonInterp_INCLUDE_DIRS})

add_custom_command(
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/A
	COMMAND ${PYTHON_EXECUTABLE} preparing.py
	DEPENDS A/preparing.py
	OUTPUT ${CMAKE_SOURCE_DIR}/A/index.h
)

set(SOURCE C/main.cpp C/main.h A/index.h)

add_executable(SomeProject ${SOURCE})

add_subdirectory(B)

target_link_libraries(SomeProject library)
