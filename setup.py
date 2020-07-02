import cx_Freeze

executables = [ cx_Freeze.Executable(script="game.py",icon="imgs/icone.ico") ]

cx_Freeze.setup(
    name= "Qual a classe?",
    options={"build_exe": {"packages": ["pygame"],
                            "include_files": ["imgs"]
                            }}, executables=executables
)