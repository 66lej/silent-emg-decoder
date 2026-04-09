# C247A Final Project (Public Release)

This is the cleaned public GitHub release for our UCLA C247A final project on single-user EMG-to-text decoding.

## Team
- Jingze Fu
- Mu Li
- Maoqi Xu
- Kaiwen Zhao

## What is included
This public repository keeps the project logic and branch-specific experiment code while removing large intermediate artifacts that are not needed to understand the implementation.

### Main cleaned code tree
- `emg2qwerty/`: cleaned baseline-based code tree with our added models and scripts
- `report/`: final report PDF plus source files currently available locally
- `artifacts/`: summarized result records and checkpoint metadata

### Branch-specific code bundles
These folders mirror the branch-oriented submission structure used by the team:
- `BranchA/`: architecture branch files from the teammate public repo
- `BranchB/`: Dilated Residual TCN branch files
- `BranchC/`: fusion branch files from the teammate public repo

## Best results summary
| Branch | Best model / setting | Key idea | Val CER ↓ | Test CER ↓ |
|---|---|---|---:|---:|
| Shared | TDSConv baseline | Baseline model | 18.48 | 21.85 |
| A | CNN+GRU hybrid | Convolutional front-end with recurrent temporal modeling | 10.04 | 9.44 |
| B | Dilated Residual TCN | Dilated temporal convolutions with shared decoding | 17.77 | 19.47 |
| C | Dual-stream late fusion | Separate left/right streams with later fusion | 12.36 | 11.59 |

## Branch B checkpoint record
The best recorded Branch B checkpoint path and metrics are stored in:
- `artifacts/checkpoint_record.txt`

## Final report
- `report/EC_ENGR_247_Final_Project_final.pdf`

## Intentionally excluded
To keep the repository lightweight and public-friendly, this release excludes:
- raw datasets
- training logs and scratch outputs
- VM-only setup leftovers
- large language model binaries
- large checkpoint binaries and unrelated duplicate bundles

## Note on checkpoints
One teammate repository referenced a `best.ckpt` file through Git LFS. This cleaned public release does not mirror large binary weights. Instead, we keep checkpoint metadata and configuration needed to identify the relevant run.
