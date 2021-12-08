set(CMAKE_CXX_STANDARD 11)

if(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-pedantic -Wno-unused-function")
elseif(${CMAKE_CXX_COMPILER_ID} EQUAL "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-pedantic -Wno-unused-function")
endif()

CPMAddPackage(
  NAME fmt
  GIT_TAG 7.1.3
  GITHUB_REPOSITORY fmtlib/fmt
  OPTIONS "FMT_INSTALL YES" # create an installable target
)

CPMAddPackage(
    NAME nlohmann_json
    GITHUB_REPOSITORY nlohmann/json
    VERSION 3.10.4
    DOWNLOAD_ONLY YES
    GIT_SHALLOW ON
)

if (nlohmann_json_ADDED)
    add_library(nlohmann_json INTERFACE)
    target_include_directories(nlohmann_json SYSTEM INTERFACE "${nlohmann_json_SOURCE_DIR}/include")
endif()
