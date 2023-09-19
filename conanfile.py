from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout


class Recipe(ConanFile):
    name = "test_celix"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"

    requires = (
        "celix/2.3.0",
    )

    default_options = {
        "celix/*:build_shell_tui": True,
        "celix/*:build_shell_wui": True,
    }

    generators = "VirtualRunEnv"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
