Celix commit:
```text
3710082906a1847f0594729ccc247db7301aec13
```

Debug:
```text
libs/utils/src/celix_file_utils.c:224 => celix_utils_writeOrCreateString returns ".cache/bundle1/resources/libShellCxx.so.2"
libs/utils/src/celix_file_utils.c:230 => the if is false, celix_utils_createDirectory is not called, no resources folder
libs/utils/src/celix_file_utils.c:234 => resources folder missing, fopen errors out

In bundle 2, ".cache/bundle2/resources/META-INF/" is the path returned by celix_utils_writeOrCreateString on the first iteration, which triggers the if and the folder creation. 

Note that it is working correctly for bundle 2 (TUI I believe). 
Also, manually creating the resources folder right before the fopen fixes the issue.
```

Error from running the container: (looks the same, did not re-copy/paste)
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

Profiles listed by Conan install: (no modification to profile, did not re-copy/paste)
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

## Versions
```text
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 23.04
Release:        23.04
Codename:       lunar
```

```text
$ conan --version
Conan version 2.0.10
```

```text
$ gcc --version
gcc (Ubuntu 12.3.0-1ubuntu1~23.04) 12.3.0
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

```text
$ cmake --version
cmake version 3.27.5

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```
