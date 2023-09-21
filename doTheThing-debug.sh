mkdir build
cd build
conan build .. --build missing -pr default -s:h build_type=Debug
cd Debug/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer
# This one works
