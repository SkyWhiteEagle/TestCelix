cmake_minimum_required(VERSION 3.15)
project(cxx_shell_example CXX)

# MODIFICATION: use Celix to build bundle container
find_package(Celix)

add_celix_container(TestCelixContainer CXX
        BUNDLES
        Celix::ShellCxx
        Celix::shell_tui
)
