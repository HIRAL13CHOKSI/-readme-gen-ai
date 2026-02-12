# Multilingual Text-to-Speech
A robust training and evaluation framework for multilingual text-to-speech models.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Tests](https://github.com/your-org/your-repo/actions/workflows/test.yml/badge.svg)

## Overview
This project provides a comprehensive system for training and evaluating multilingual text-to-speech (TTS) models. It's designed to handle large datasets, manage checkpoints, and leverage GPU resources efficiently. Key features include:

*   **Configurable Paths**: Easily specify directories for data, checkpoints, and hyperparameter files.
*   **Multi-GPU Support**: Utilizes available GPUs for accelerated training.
*   **TensorBoard Integration**: Flushes summaries for real-time monitoring of training progress.
*   **Modular Design**: Structured with distinct functions for training (`train`), evaluation (`evaluate`), and utility functions like `cos_decay`.

## Requirements
*   **Python**: `3.8` or newer.
*   **Operating System**: Linux, macOS, or Windows.

## Dependencies

### Python Packages
The following Python packages are required:

*   `dataset`
*   `google-generativeai`
*   `groq`
*   `modules`
*   `numpy`
*   `openai`
*   `params`
*   `torch`
*   `utils`

### External Tools
None specified.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-org/your-repo.git
    cd your-repo
    ```

2.  **Install dependencies**:
    Dependencies are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **For development (editable install)**:
    If you plan to modify the code, install in editable mode:
    ```bash
    pip install -e .
    ```

## Usage
Run the script from your terminal, specifying arguments as needed.

```bash
python Multilingual_Text_to_Speech.py --base_directory <value> --checkpoint <value> --checkpoint_root <value> --data_root <value> --flush_seconds <value> --hyper_parameters <value> --logging_start <value> --max_gpus <value> --loader_workers <value>
```

## Flags
This script uses `argparse` for command-line argument parsing.

| Flag               | Alias | Type | Required | Default     | Help                                                          |
| :----------------- | :---- | :--- | :------- | :---------- | :------------------------------------------------------------ |
| `--base_directory` |       | str  | False    | `.`         | Base directory of the project.                                |
| `--checkpoint`     |       | str  | False    | `None`      | Name of the initial checkpoint.                               |
| `--checkpoint_root`|       | str  | False    | `checkpoints` | Base directory of checkpoints.                                |
| `--data_root`      |       | str  | False    | `data`      | Base directory of datasets.                                   |
| `--flush_seconds`  |       | int  | False    | `60`        | How often to flush pending summaries to tensorboard.          |
| `--hyper_parameters`|      | str  | False    | `None`      | Name of the hyperparameters file.                             |
| `--logging_start`  |       | int  | False    | `1`         | First epoch to be logged                                      |
| `--max_gpus`       |       | int  | False    | `2`         | Maximal number of GPUs of the local machine to use.           |
| `--loader_workers` |       | int  | False    | `2`         | Number of subprocesses to use for data loading.               |

## Environment Variables
None specified.

## Examples

### 1. Basic Training Run
Start a training session using default directories for data and checkpoints, leveraging up to 2 GPUs.
```bash
python Multilingual_Text_to_Speech.py
```

### 2. Resuming Training with Custom Paths
Resume training from a specific checkpoint, define custom data and checkpoint roots, and specify a hyperparameter file.
```bash
python Multilingual_Text_to_Speech.py \
    --data_root /mnt/datasets/tts_data \
    --checkpoint_root /mnt/models/tts_checkpoints \
    --checkpoint latest_model.pt \
    --hyper_parameters config/hparams_v2.json \
    --max_gpus 4
```

## Input/Output

| Type   | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| **Input** | Audio-text paired datasets, model checkpoints, hyperparameter files. |
| **Output** | Trained model checkpoints, TensorBoard logs, evaluation metrics.     |

## Testing
This project includes tests to ensure code correctness and functionality.
To run tests, make sure you have `pytest` installed (`pip install pytest`):

```bash
pytest
```

## Troubleshooting

1.  **"ModuleNotFoundError"**: Ensure all dependencies are installed. Run `pip install -r requirements.txt`. If you encounter issues with specific packages like `torch`, refer to their official installation guides for system-specific instructions (e.g., CUDA versions).
2.  **GPU Issues / "CUDA out of memory"**: If using GPUs, verify your CUDA drivers are up to date and `torch` is installed with CUDA support. Reduce the `max_gpus` flag or adjust batch sizes within your hyperparameter configuration if you run out of memory.
3.  **Data Loading Errors**: Check the `data_root` path. Ensure your dataset is correctly formatted and accessible by the script.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
Placeholder.
