math(EXPR NCS_VERSION_CODE "(${NCS_VERSION_MAJOR} << 16) + (${NCS_VERSION_MINOR} << 8)  + (${NCS_VERSION_PATCH})")
math(EXPR NCS_VERSION_NUMBER ${NCS_VERSION_CODE} OUTPUT_FORMAT HEXADECIMAL)

add_custom_command(
  OUTPUT ${PROJECT_BINARY_DIR}/include/generated/ncs_version.h
  COMMAND ${CMAKE_COMMAND} -DZEPHYR_BASE=${ZEPHYR_BASE}
    -DOUT_FILE=${PROJECT_BINARY_DIR}/include/generated/ncs_version.h
    -DVERSION_TYPE=NCS
    # We don't want Zephyr to parse the NCS VERSION file as it is not conforming to Zephyr VERSION
    # format. Pointing to a non-existing file allows us full control from CMake instead.
    -DVERSION_FILE=${NRF_DIR}/VERSIONFILEDUMMY
    -DNCS_VERSION_CODE=${NCS_VERSION_CODE}
    -DNCS_VERSION_NUMBER=${NCS_VERSION_NUMBER}
    -DNCS_VERSION_MAJOR=${NCS_VERSION_MAJOR}
    -DNCS_VERSION_MINOR=${NCS_VERSION_MINOR}
    -DNCS_PATCHLEVEL=${NCS_VERSION_PATCH}
    -DNCS_VERSION_STRING=${NCS_VERSION}
    -P ${ZEPHYR_BASE}/cmake/gen_version_h.cmake
    DEPENDS ${NRF_DIR}/VERSION ${git_dependency}
)
add_custom_target(ncs_version_h DEPENDS ${PROJECT_BINARY_DIR}/include/generated/ncs_version.h)
add_dependencies(version_h ncs_version_h)
