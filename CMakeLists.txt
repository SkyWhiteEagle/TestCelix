cmake_minimum_required(VERSION 3.26)

project(TestCelix)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Celix)

find_package(libzip)

add_celix_container(TestCelixContainer CXX
    BUNDLES
        Celix::http_admin
        Celix::ShellCxx
        Celix::shell_tui
        Celix::shell_wui
)

target_link_libraries(TestCelixContainer
    PRIVATE
        libzip::zip
)
