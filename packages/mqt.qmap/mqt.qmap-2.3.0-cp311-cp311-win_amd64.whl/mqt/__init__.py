"""""" # start delvewheel patch
def _delvewheel_patch_1_5_0():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'mqt.qmap.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_5_0()
del _delvewheel_patch_1_5_0
# end delvewheel patch
