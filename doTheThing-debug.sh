mkdir build
cd build
conan install .. --build missing -pr debug
conan build .. -pr debug
cd Debug/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer
# This one works
