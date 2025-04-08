# CRACEN drivers
zephyr_library()
zephyr_library_sources_ifdef(CONFIG_CRACEN_LIB_KMU lib_kmu.c)
