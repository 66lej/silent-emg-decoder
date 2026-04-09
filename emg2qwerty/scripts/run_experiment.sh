#!/usr/bin/env bash
set -euo pipefail

EXP_NAME="${1:-baseline_tds}"
MAX_EPOCHS="${2:-40}"

if [[ ! -d "data" ]]; then
  echo "[ERROR] data directory not found at $(pwd)/data"
  echo "Place subject data under emg2qwerty/data before training."
  exit 1
fi

TS="$(date +"%Y%m%d_%H%M%S")"
RUN_DIR="logs/${EXP_NAME}_${TS}"
mkdir -p "${RUN_DIR}"
LOG_FILE="${RUN_DIR}/train.out"

echo "[INFO] Starting run: ${EXP_NAME}"
echo "[INFO] Max epochs: ${MAX_EPOCHS}"
echo "[INFO] Log file: ${LOG_FILE}"

python -m emg2qwerty.train \
  user=single_user \
  trainer.accelerator=gpu \
  trainer.devices=1 \
  trainer.max_epochs="${MAX_EPOCHS}" \
  hydra.run.dir="${RUN_DIR}" \
  2>&1 | tee "${LOG_FILE}"

python scripts/extract_cer.py "${LOG_FILE}" > "${RUN_DIR}/cer_summary.json"
echo "[INFO] CER summary written to ${RUN_DIR}/cer_summary.json"
