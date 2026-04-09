# EMG-to-Text Final Project (Public Release)

This repository contains the cleaned public release of our UCLA final project on single-user EMG-to-text decoding based on the `emg2qwerty` codebase.

## Included
- A cleaned source tree under `emg2qwerty/`
- Our report source under `report/`
- Branch B artifacts and result summaries under `artifacts/`
- The custom Dilated Residual TCN implementation used for our best Branch B result

## Excluded
To keep the public repository focused on code, logic, and reproducibility, we intentionally excluded:
- raw datasets
- training logs and scratch outputs
- VM setup leftovers and update tarballs
- large pretrained checkpoints and LM binaries
- unrelated course handouts and duplicate zip bundles

## Branch B best result
- Model: Dilated Residual TCN CTC
- Validation CER: 17.7669
- Test CER: 19.4727
- Checkpoint record: `artifacts/checkpoint_record.txt`

## Repository layout
- `emg2qwerty/`: cleaned training code and configs
- `report/`: LaTeX report source
- `artifacts/`: metrics summary and checkpoint record

## Notes
This public release is meant to document the implementation and results. Some heavyweight files referenced by the original research workflow are intentionally omitted and would need to be regenerated or provided separately for exact end-to-end reruns.
