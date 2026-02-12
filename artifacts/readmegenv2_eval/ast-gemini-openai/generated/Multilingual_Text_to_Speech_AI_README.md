# Multilingual Text-to-Speech

A Python script for training a multilingual text-to-speech model.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/your-username/your-repo/actions/workflows/test.yml/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/test.yml)

## Overview

This script implements a training pipeline for a multilingual text-to-speech (TTS) model. It provides functionalities for data loading, model training, evaluation, and checkpoint management. The script uses PyTorch for model definition and training, and it leverages command-line arguments for configuration.

Key features:

*   Training and evaluation loops for TTS models
*   Checkpoint saving and loading
*   Configuration via command-line arguments

## Requirements

*   Python 3.7+
*   Operating System: Platform independent

## Dependencies

### Python Packages (Third-Party)

*   `dataset`
*   `modules`
*   `numpy`
*   `params`
*   `torch`
*   `utils`
*   `google-generativeai`
*   `groq`
*   `openai`

### Standard Library

*   `argparse`
*   `datetime`
*   `math`
*   `os`
*   `re`
*   `time`

## Installation

The project dependencies are managed using `requirements.txt`.

```bash
pip install -r ../requirements.txt
```

For editable installs:

```bash
git clone <repository_url>
cd <repository_directory>
pip install -e .
```

## Usage

```
python Multilingual_Text_to_Speech.py --base_directory <value> --checkpoint <value> --checkpoint_root <value> --data_root <value> --flush_seconds <value> --hyper_parameters <value> --logging_start <value> --max_gpus <value> --loader_workers <value>
```

## Flags

| Flag               | Alias | Type   | Required | Default   | Help                                              |
| ------------------ | ----- | ------ | -------- | --------- | ------------------------------------------------- |
| `--base_directory` |       | `str`  | No       | `.`       | Base directory of the project.                    |
| `--checkpoint`     |       | `str`  | No       | `null`    | Name of the initial checkpoint.                   |
| `--checkpoint_root`|       | `str`  | No       | `checkpoints` | Base directory of checkpoints.                  |
| `--data_root`      |       | `str`  | No       | `data`    | Base directory of datasets.                       |
| `--flush_seconds`  |       | `int`  | No       | `60`      | How often to flush pending summaries to tensorboard. |
| `--hyper_parameters`|       | `str`  | No       | `null`    | Name of the hyperparameters file.                 |
| `--logging_start`  |       | `int`  | No       | `1`       | First epoch to be logged                          |
| `--max_gpus`       |       | `int`  | No       | `2`       | Maximal number of GPUs of the local machine to use.|
| `--loader_workers` |       | `int`  | No       | `2`       | Number of subprocesses to use for data loading.   |

## Environment Variables

None specified.

## Examples

1.  **Basic training run:**

    ```bash
    python Multilingual_Text_to_Speech.py --base_directory /path/to/project --data_root /path/to/data --hyper_parameters hparams.json
    ```

2.  **Training from a checkpoint:**

    ```bash
    python Multilingual_Text_to_Speech.py --checkpoint_root /path/to/checkpoints --checkpoint latest.pth --data_root /path/to/data --hyper_parameters hparams.json
    ```

## Input/Output

| Input                                   | Output                                |
| --------------------------------------- | ------------------------------------- |
| Training datasets (audio, transcripts) | Trained model checkpoints, TensorBoard logs |

## Testing

This project includes tests. It is recommended to use `pytest` for running the tests.

```bash
pytest
```

## Troubleshooting

1.  **CUDA out of memory error:** Reduce the batch size or use a smaller model.
2.  **Data loading issues:** Ensure the dataset is correctly formatted and accessible.

## Contributing

Coming soon.

## License

Coming soon.
