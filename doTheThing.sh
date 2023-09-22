rm -rf build
mkdir build
cd build
conan build .. --build missing -s:h build_type=Release
cd Release/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer
