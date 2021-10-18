import os


c = 1
for f in os.listdir("aesthetic_o_vibes"):
    ext = f.rpartition(".")
    print(f"{f}",f"{c}.{ext[-1]}")
    try:
        os.rename(f"{os.getcwd()}\\aesthetic_o_vibes\\{f}",f"{os.getcwd()}\\aesthetic_o_vibes\\{c}.{ext[-1]}")
    except Exception as e:
        print(e)
    c += 1