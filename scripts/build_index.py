import os, argparse, numpy as np, pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--src", required=True, help="Carpeta con npz")
parser.add_argument("--out", required=True, help="Archivo de salida index.csv")
args = parser.parse_args()

rows = []
for fname in os.listdir(args.src):
    if fname.endswith(".npz"):
        path = os.path.join(args.src, fname)
        with np.load(path) as d:
            sig = d["signal"]
            fs = float(d["fs"])
            leads = d["leads"] if "leads" in d.files else [f"L{i+1}" for i in range(sig.shape[1])]
            rows.append({
                "record_id": os.path.splitext(fname)[0],
                "fs": fs,
                "n_samples": sig.shape[0],
                "n_leads": sig.shape[1] if sig.ndim > 1 else 1,
                "leads": ",".join(leads),
                "npz_path": path
            })

pd.DataFrame(rows).to_csv(args.out, index=False)
print("Index guardado en", args.out)
