from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps


class cxx_shell_exampleRecipe(ConanFile):
    name = "cxx_shell_example"
    version = "0.1"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of cxx_shell_example package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    # MODIFICATION: setup environment for me
    generators = "VirtualRunEnv"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        # MODIFICATION: minimal requirement
        self.options["celix"].build_shell_tui = True

    def requirements(self):
        self.requires("celix/2.3.0")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        # MODIFICATION: workaround for 642
        if self.settings.os == "Linux":
            tc.cache_variables["CMAKE_EXE_LINKER_FLAGS"] = "-Wl,--unresolved-symbols=ignore-in-shared-libs"
        elif self.settings.os == "Macos":
            tc.cache_variables["CMAKE_EXE_LINKER_FLAGS"] = "-Wl,-undefined -Wl,dynamic_lookup"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
