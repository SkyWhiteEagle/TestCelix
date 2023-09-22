cmake_minimum_required(VERSION 3.15)
project(cxx_shell_example CXX)

set(CMAKE_C_FLAGS "-g ${CMAKE_C_FLAGS}")
set(CMAKE_CXX_FLAGS "-g ${CMAKE_CXX_FLAGS}")

# MODIFICATION: use Celix to build bundle container
find_package(Celix)

add_celix_container(TestCelixContainer CXX
        BUNDLES
        Celix::ShellCxx
        Celix::shell_tui
)
