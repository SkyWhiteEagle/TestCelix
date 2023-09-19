mkdir build
cd build
conan install .. --build missing
conan build ..
cd Release/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer
