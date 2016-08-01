name = "doubleconversion"

version = "1.1.5"

variants = [
    ["platform-linux"]
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
