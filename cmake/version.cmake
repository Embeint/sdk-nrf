add_custom_command(
  OUTPUT ${PROJECT_BINARY_DIR}/include/generated/ncs_version.h
  COMMAND ${CMAKE_COMMAND} -DZEPHYR_BASE=${ZEPHYR_BASE}
    -DOUT_FILE=${PROJECT_BINARY_DIR}/include/generated/ncs_version.h
    -DVERSION_TYPE=NCS
    -DVERSION_FILE=${NRF_DIR}/VERSION
    -P ${ZEPHYR_BASE}/cmake/gen_version_h.cmake
    DEPENDS ${NRF_DIR}/VERSION ${git_dependency}
)
add_custom_target(ncs_version_h DEPENDS ${PROJECT_BINARY_DIR}/include/generated/ncs_version.h)
add_dependencies(version_h ncs_version_h)
