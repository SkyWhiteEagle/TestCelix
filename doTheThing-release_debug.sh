rm -rf build
mkdir build
cd build
conan build .. --build missing -s:h build_type=RelWithDebInfo
cd RelWithDebInfo/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer
