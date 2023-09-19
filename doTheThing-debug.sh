conan build . -pr:b debug -pr:h debug -b missing -of cmake-build-debug
cd cmake-build-debug
source conanrun.sh
cd deploy/TestCelixContainer/
./TestCelixContainer
# This one works
