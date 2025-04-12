# CRACEN drivers
if(CONFIG_CRACEN_LIB_KMU)
  zephyr_library()
  zephyr_library_sources(lib_kmu.c)
endif()
