from conans import ConanFile, CMake, tools


class LibserialConan(ConanFile):
    name = "libserial"
    version = "latest"
    license = "BSD 3-Clause"
    author = "Eduard Sargsyan edward.sarkisyan@gmail.com"
    url = "https://github.com/edwardoid/libserial_conan"
    description = "libserial is a library to interact with serial ports on Linux"
    topics = ("Linux", "Serial port")
    settings = "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
#    source_folder = "libserial"

    def source(self):
        self.run("git clone --depth 1 https://github.com/crayzeewulf/libserial.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["LIBSERIAL_BUILD_DOCS"] = "NO"
        cmake.definitions["LIBSERIAL_ENABLE_TESTING"] = "NO"
        cmake.definitions["LIBSERIAL_BUILD_EXAMPLES"] = "NO"
        cmake.definitions["LIBSERIAL_PYTHON_ENABLE"] = "NO"
        if self.options.shared:
            cmake.definitions["INSTALL_STATIC"] = "NO"
        else:
            cmake.definitions["INSTALL_SHARED"] = "NO"
        cmake.configure(source_folder="libserial")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
    
    def package_info(self):
        self.cpp_info.libs = ["libserial"]

