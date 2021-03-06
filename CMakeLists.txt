CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(doubleconversion_version v${DOUBLECONVERSION_VERSION})

set(url_doubleconversion https://github.com/google/double-conversion.git)

set(make_args -j1 VERBOSE=on)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

message(STATUS "INSTALL? ${REZ_BUILD_INSTALL}" )

ExternalProject_add(
    doubleconversion
    GIT_REPOSITORY ${url_doubleconversion}
    GIT_TAG ${doubleconversion_version}
    PREFIX doubleconversion
    BUILD_COMMAND make -j1 VERBOSE=on
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/doubleconversion.cmake
    DESTINATION .
)
