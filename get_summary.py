import pandas as pd
from pathlib import Path

data_dir = Path("/Users/ludvig/Developer/CBS/Applied ML/Project/data")
rows = []

for file in sorted(data_dir.glob("*.xls")): # Assuming only .xls files for now
    size_mb = file.stat().st_size / (1024 ** 2)
    try:
        df = pd.read_excel(file)
        n_rows, n_cols = df.shape
        col_names = ", ".join(df.columns)
    except Exception as exc:
        n_rows = n_cols = "error"
        col_names = str(exc)
    rows.append(
        dict(
            name=file.name,
            rows=n_rows,
            cols=n_cols,
            column_names=col_names,
            size_mb=size_mb,
        )
    )

summary = pd.DataFrame(rows)
summary["size_mb"] = summary["size_mb"].round(3)
summary.to_csv("data_summary.csv", index=False)
print("Data summary saved to data_summary.csv")
