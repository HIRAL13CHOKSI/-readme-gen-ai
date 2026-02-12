This document provides a technical README for the `Multilingual_Text_to_Speech.py` script, inferred solely from its source code and immediate runtime output.

## Multilingual Text-to-Speech Training Script

### Overview

This Python script is designed for training a sophisticated Text-to-Speech (TTS) model, likely based on the Tacotron architecture, with support for multiple languages and speakers. It orchestrates the entire training process, including data loading, model initialization, optimization, evaluation, and logging. The script leverages PyTorch for deep learning operations and includes features for checkpointing and distributed training.

### Features

*   **Tacotron-based TTS Training**: Implements a full training pipeline for a Tacotron model.
*   **Multilingual and Multi-speaker Support**: Configurable to train models capable of synthesizing speech in multiple languages and for various speakers, adapting to dataset characteristics.
*   **Checkpointing**: Allows saving and loading model states, optimizer states, scheduler states, and hyperparameters to resume training or fine-tune models.
*   **Hyperparameter Management**: Supports loading custom hyperparameters from a JSON file and dynamically updates some parameters (e.g., speaker/language counts, normalization constants) based on the loaded dataset.
*   **GPU Acceleration**: Utilizes PyTorch for GPU-accelerated training, including `torch.nn.DataParallel` for multi-GPU setups.
*   **Comprehensive Logging**: Integrates with a `Logger` for detailed tracking of training and evaluation metrics (e.g., various loss components, gradient norms, learning rate, Mel Cepstral Distortion (MCD), speaker classification accuracy).
*   **Advanced Data Loading**: Employs custom `DataLoader` configurations with specialized samplers (`RandomImbalancedSampler`, `PerfectBatchSampler`) for handling multilingual and multi-speaker datasets efficiently.
*   **Teacher Forcing Decay**: Implements a cosine decay schedule for the teacher forcing ratio during training.
*   **Gradient Clipping**: Applies gradient clipping to prevent exploding gradients and stabilize the training process.
*   **Evaluation Metrics**: Calculates critical evaluation metrics such as Mel Cepstral Distortion (MCD) and adversarial speaker classification accuracy during validation.

### Installation

This script relies on several external Python libraries and assumes a specific project structure for its local modules.

1.  **Python Environment**: Ensure you have Python 3.x installed.
2.  **External Dependencies**: The primary external dependency is PyTorch, along with NumPy. Based on the runtime error, `torch` is missing.
    Install these using pip:
    ```bash
    pip install torch numpy
    # If using CUDA for GPU acceleration (recommended):
    # Follow instructions on the official PyTorch website to install the correct version for your CUDA setup.
    # Example for CUDA 11.8: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```
3.  **Project Structure**: This script expects to find local modules such as `dataset`, `params`, `utils`, and `modules` in a structured directory relative to its location. Ensure these modules are correctly set up as part of your overall project. For example:
    ```
    .
    ├── Multilingual_Text_to_Speech.py
    ├── dataset/
    │   └── dataset.py
    ├── params/
    │   └── params.py
    │   └── default_params.json  # Example hyperparameter file
    ├── utils/
    │   ├── audio.py
    │   ├── text.py
    │   └── logging.py
    └── modules/
        └── tacotron2.py
    ```

### Usage

The script is executed from the command line and accepts various arguments to configure the training process.

```bash
python Multilingual_Text_to_Speech.py [OPTIONS]
```

**Arguments:**

*   `--base_directory` (str, default: `.`): The base directory of the project.
*   `--checkpoint` (str, default: `None`): Name of the checkpoint file (e.g., `model_epoch_100.pt`) to load for resuming training.
*   `--checkpoint_root` (str, default: `checkpoints`): Base directory where checkpoints are stored/loaded, relative to `base_directory`.
*   `--data_root` (str, default: `data`): Base directory where datasets are located.
*   `--flush_seconds` (int, default: `60`): How often to flush pending summaries to TensorBoard (for logging).
*   `--hyper_parameters` (str, default: `None`): Name of the hyperparameters JSON file (e.g., `default_params`) located in the `params/` directory.
*   `--logging_start` (int, default: `1`): The first epoch from which training progress will be logged.
*   `--max_gpus` (int, default: `2`): Maximal number of GPUs on the local machine to use for parallel training.
*   `--loader_workers` (int, default: `2`): Number of subprocesses to use for data loading.

### Examples

**1. Start New Training with Custom Hyperparameters:**

To begin training a new model using hyperparameters defined in `params/my_config.json` and a dataset located in `my_tts_data/`, storing checkpoints in `my_checkpoints/`:

```bash
python Multilingual_Text_to_Speech.py \
    --hyper_parameters my_config \
    --data_root my_tts_data \
    --checkpoint_root my_checkpoints \
    --max_gpus 4 \
    --loader_workers 8
```

**2. Resume Training from a Checkpoint:**

To continue training from a previously saved checkpoint named `v1_loss-99-0.500` located in the `checkpoints` directory, using the original hyperparameters:

```bash
python Multilingual_Text_to_Speech.py \
    --checkpoint v1_loss-99-0.500 \
    --data_root path/to/your/dataset
```

**3. Fine-tuning an Existing Model with New Hyperparameters:**

To fine-tune a model from an existing checkpoint but with a different set of hyperparameters (e.g., lower learning rate) defined in `params/finetune_config.json`:

```bash
python Multilingual_Text_to_Speech.py \
    --checkpoint v1_loss-99-0.500 \
    --hyper_parameters finetune_config \
    --data_root path/to/your/dataset
```

### Limitations or Notes

*   **Training Script Only**: This script focuses solely on the training and evaluation phases of a TTS model. It does not include functionality for inference (generating audio from new text input) or exporting the trained model for deployment.
*   **Assumes Project Structure**: The script relies heavily on a specific project structure, importing modules like `dataset`, `params`, `utils`, and `modules`. It cannot run as a standalone file without these accompanying components.
*   **Data Format Dependency**: It expects datasets to be organized and processed in a format compatible with `TextToSpeechDatasetCollection`, likely requiring audio files and corresponding text transcripts.
*   **Hyperparameter File**: A `params.json` file is expected to exist in the `params/` directory, defining default or custom hyperparameters.
