# Multilingual Text to Speech

## Overview
The `Multilingual_Text_to_Speech.py` script is a Python utility designed for training and evaluating a multilingual text-to-speech model using the Tacotron architecture. It leverages PyTorch for deep learning and supports various configurations for handling multiple languages and speakers.

## Features
- **Multilingual Support**: Train models capable of synthesizing speech in multiple languages.
- **Dynamic Sampling**: Implements both perfect and random sampling strategies for training data.
- **Checkpointing**: Save and load model states, allowing for resuming training or evaluation.
- **Logging**: Track training and evaluation metrics using a logging system.
- **GPU Support**: Utilize multiple GPUs for training if available.

## Installation
To run this script, ensure you have Python installed along with the following dependencies:
- PyTorch
- NumPy

You can install the required packages using pip:
```bash
pip install torch numpy
```

## Usage
Run the script from the command line with the necessary arguments. Here’s the basic command structure:

```bash
python Multilingual_Text_to_Speech.py --base_directory <BASE_DIR> --checkpoint <CHECKPOINT_NAME> --data_root <DATA_DIR>
```

### Example Command
```bash
python Multilingual_Text_to_Speech.py --base_directory ./project --checkpoint initial_checkpoint.pth --data_root ./data
```

## Examples
1. **Basic Training Command**:
   ```bash
   python Multilingual_Text_to_Speech.py --base_directory ./project --data_root ./data
   ```

2. **Using Checkpoints**:
   ```bash
   python Multilingual_Text_to_Speech.py --base_directory ./project --checkpoint initial_model.pth --data_root ./data
   ```

3. **Specifying Hyperparameters**:
   ```bash
   python Multilingual_Text_to_Speech.py --base_directory ./project --hyper_parameters my_hyperparams --data_root ./data
   ```

## Limitations or Notes
- Ensure that the `torch` library is installed, as the script will fail with a `ModuleNotFoundError` if it is not found.
- The script requires a properly structured dataset and configuration files for hyperparameters to function correctly.
- The performance may vary based on the hardware configuration, especially when using multiple GPUs.

This README provides a concise guide to understanding and using the `Multilingual_Text_to_Speech.py` script effectively.
