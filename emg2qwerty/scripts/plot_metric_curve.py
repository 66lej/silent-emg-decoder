#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _series(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    cols = ["epoch", metric]
    sub = df.loc[df[metric].notna(), cols].copy()
    if sub.empty:
        return sub
    return sub.groupby("epoch", as_index=False)[metric].last()


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: plot_metric_curve.py <metrics.csv>")

    csv_path = Path(sys.argv[1])
    df = pd.read_csv(csv_path)

    train_cer = _series(df, "train/CER") if "train/CER" in df.columns else pd.DataFrame()
    val_cer = _series(df, "val/CER") if "val/CER" in df.columns else pd.DataFrame()

    if train_cer.empty and val_cer.empty:
        raise SystemExit("No train/CER or val/CER columns found in metrics.csv")

    plt.figure(figsize=(8, 5))
    if not train_cer.empty:
        plt.plot(train_cer["epoch"], train_cer["train/CER"], label="train/CER", linewidth=2)
    if not val_cer.empty:
        plt.plot(val_cer["epoch"], val_cer["val/CER"], label="val/CER", linewidth=2)

    plt.xlabel("Epoch")
    plt.ylabel("CER")
    plt.title("Training Curve")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    out_path = csv_path.with_name("cer_curve.png")
    plt.savefig(out_path, dpi=200)

    print(f"Saved plot to: {out_path}")
    if not train_cer.empty:
        print("Last train/CER values:")
        print(train_cer.tail(10).to_string(index=False))
    if not val_cer.empty:
        print("Last val/CER values:")
        print(val_cer.tail(10).to_string(index=False))


if __name__ == "__main__":
    main()
