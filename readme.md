Conan profiles:
```text
$ cat ~/.conan2/profiles/default 
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=12
os=Linux

$ cat ~/.conan2/profiles/debug
[settings]
arch=x86_64
build_type=Debug
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=12
os=Linux
```

Commands:
```shell
mkdir build
cd build
conan install .. --build missing
conan build ..
cd Release/deploy/TestCelixContainer/
source ../../generators/conanrun.sh
./TestCelixContainer 
```

Error from running the container:
```text
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_framework_utils_extractBundlePath:217] No such file or directory(0x2): "Could not extract bundle zip file `bundles/celix_ShellCxx.zip` to `.cache/bundle2/resources`";
 Cause: No such file or directory
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_bundleArchive_extractBundle:164] Failed to initialize archive. Failed to extract bundle zip to revision directory.
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_bundleArchive_createCacheDirectory:198] Failed to initialize archive. Failed to extract bundle.
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_bundleArchive_create:322] No such file or directory(0x2): "Could not create archive.";
 Cause: Failed to initialize archive or create manifest.
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_bundleCache_createArchive:222] No such file or directory(0x2): Failed to create archive.
[2023-09-19T18:50:41] [  error] [celix_framework] [celix_framework_installBundleInternalImpl:686] No such file or directory(0x2): Could not install bundle
[2023-09-19T18:50:41] [  error] [celix_framework] [framework_autoInstallConfiguredBundlesForList:538] Could not install bundle from location 'celix_ShellCxx.zip'.
HTTP Admin started at port 8080
-> [2023-09-19T18:50:41] [  error] [celix_framework] [framework_start:471] Could not auto start or install all configured bundles
[2023-09-19T18:50:41] [   info] [celix_framework] [framework_start:476] Celix framework started
[2023-09-19T18:50:41] [   info] [celix_framework] Framework error event received -> registering framework.error condition service
```

Profiles listed by Conan install:
```text
======== Input profiles ========
Profile host:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=12
os=Linux

Profile build:
[settings]
arch=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=12
os=Linux
```
