conan build . -pr:b default -pr:h default -b missing -of cmake-build-release
cd cmake-build-release
source conanrun.sh
cd deploy/TestCelixContainer/
./TestCelixContainer
