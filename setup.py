import cx_Freeze

executables = [cx_Freeze.Executable("gaming1.py")]

cx_Freeze.setup(
    name="A Bit Racy",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["car.png", "road2.png", "car2.png"]}},

    executables=executables

)