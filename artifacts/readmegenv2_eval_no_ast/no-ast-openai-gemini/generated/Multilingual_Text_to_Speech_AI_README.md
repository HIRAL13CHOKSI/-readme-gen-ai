# Multilingual Text to Speech

## Overview
The `Multilingual_Text_to_Speech.py` script implements a training and evaluation pipeline for a multilingual text-to-speech (TTS) model using PyTorch. The model is designed to synthesize speech from text in multiple languages, leveraging advanced techniques such as Tacotron for generating mel-spectrograms.

## Features
- Multilingual support for text-to-speech synthesis.
- Training and evaluation procedures for the Tacotron model.
- Logging of training and evaluation metrics.
- Support for loading checkpoints and hyperparameters for model fine-tuning.
- Utilization of GPU for accelerated training (if available).

## Installation
To run this script, ensure you have Python and the required libraries installed. You can set up a virtual environment and install the necessary dependencies as follows:

1. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv tts-env
   source tts-env/bin/activate  # On Windows use `tts-env\Scripts\activate`
   ```

2. **Install PyTorch:**
   Follow the instructions on the [PyTorch website](https://pytorch.org/get-started/locally/) to install the appropriate version for your system.

3. **Install other dependencies:**
   You may need additional libraries such as NumPy. Install them using:
   ```bash
   pip install numpy
   ```

## Usage
To run the script, use the following command line syntax:

```bash
python Multilingual_Text_to_Speech.py --base_directory <BASE_DIR> --checkpoint <CHECKPOINT_NAME> --data_root <DATA_DIR> --hyper_parameters <HYPERPARAM_FILE>
```

### Example Command
```bash
python Multilingual_Text_to_Speech.py --base_directory ./project --checkpoint initial_model.pth --data_root ./data --hyper_parameters hyperparams
```

## Examples
- **Training a model with specific parameters:**
  ```bash
  python Multilingual_Text_to_Speech.py --base_directory ./project --checkpoint initial_model.pth --data_root ./data --hyper_parameters hyperparams.json
  ```

- **Using default parameters:**
  ```bash
  python Multilingual_Text_to_Speech.py --base_directory . --data_root ./data
  ```

## Limitations or Notes
- Ensure that you have the `torch` library installed; otherwise, the script will raise a `ModuleNotFoundError`.
- The script assumes the existence of a dataset structured according to the expected input format.
- Hyperparameters must be defined in a JSON file if you wish to customize training settings.
- The script is designed to work with multiple GPUs if available, but it can also run on a single GPU or CPU.

This README provides a comprehensive guide to understanding and using the `Multilingual_Text_to_Speech.py` script effectively.
