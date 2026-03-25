def get_behavior_flags(ctx):

    flags = []

    if ctx["mic"]:
        flags.append("MIC")

    if ctx["cam"]:
        flags.append("CAM")

    if ctx["screen"]:
        flags.append("SCREEN")

    if ctx["network"]:
        flags.append("NETWORK")

    if ctx["cpu"] and ctx["cpu"] > 50:
        flags.append("HIGH_CPU")

    return flags