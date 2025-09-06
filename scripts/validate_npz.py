import os, argparse, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--src", required=True, help="Carpeta con npz")
args = parser.parse_args()

for fname in os.listdir(args.src):
    if fname.endswith(".npz"):
        path = os.path.join(args.src, fname)
        try:
            with np.load(path) as d:
                assert "signal" in d, "Falta 'signal'"
                assert "fs" in d, "Falta 'fs'"
                sig = d["signal"]
                fs = float(d["fs"])
                leads = d["leads"] if "leads" in d.files else None
            print(fname, "OK", sig.shape, fs, leads if leads is not None else "-")
        except Exception as e:
            print(fname, "ERROR:", e)
