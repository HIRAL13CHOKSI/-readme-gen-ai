This README provides an overview and usage instructions for the `PyCat.py` script, inferred directly from its source code.

---

# PyCat.py

PyCat is a Python-based utility designed to replicate some functionalities of the popular network tool, Netcat. It supports both client and server modes for TCP communication, enabling tasks such as sending data, executing commands remotely, providing interactive shells, and uploading files.

## Overview

PyCat acts as a versatile network tool capable of initiating connections (client mode) or listening for incoming connections (server mode). In client mode, it can send data from standard input to a specified target. In server mode, it can host an interactive shell, execute arbitrary commands, or facilitate file uploads to the listening host upon connection.

## Features

*   **Client Mode:** Connect to a remote host and port, sending data from `stdin` and receiving output.
*   **Server Mode (`-l`):** Listen on a specified host and port for incoming TCP connections.
*   **Remote Command Execution (`-e`):** Execute a predefined command on the remote system immediately upon connection.
*   **Remote Command Shell (`-c`):** Establish an interactive command shell on the remote system after a connection is established.
*   **File Upload (`-u`):** Receive and save an uploaded file to a specified destination path on the listening system upon connection.
*   **Local Network Scanning (Conditional):** When run without any arguments, the script attempts to initiate a local network scan. This feature requires an additional `scanner.py` module to be present.

## Installation

This script is written in Python 2. It requires the `netaddr` library, which can be installed via pip:

1.  **Python 2 Environment:** Ensure you have a Python 2 environment.
2.  **Install `netaddr`:**
    ```bash
    pip install netaddr
    ```
3.  **Optional: `scanner.py`:** If you intend to use the local network scanning feature (by running `PyCat.py` without arguments), an external `scanner.py` module containing a `Scan` class is expected in the same directory. This module is not provided with `PyCat.py`.

## Usage

Run the script from your terminal using `python PyCat.py`.

### Basic Help

To display the help message and available options:

```bash
python PyCat.py -h
```
or
```bash
python PyCat.py --help
```

### Client Mode

To connect to a target host and port, sending data from `stdin`:

```bash
echo 'Hello, PyCat!' | python PyCat.py -t 192.168.1.10 -p 1234
```
You can type interactively as well; use `CTRL-D` to signal end-of-input for `stdin.read()`.

### Server Mode (`-l`)

To listen for incoming connections:

```bash
python PyCat.py -t 0.0.0.0 -p 5555 -l
```
(Listening on `0.0.0.0` will bind to all available network interfaces.)

### Server Mode with Command Shell (`-l -c`)

To listen and provide an interactive command shell upon connection:

```bash
python PyCat.py -t 0.0.0.0 -p 5555 -l -c
```

### Server Mode with Command Execution (`-l -e`)

To listen and execute a specific command upon connection:

```bash
python PyCat.py -t 0.0.0.0 -p 5555 -l -e="ls -la"
```

### Server Mode with File Upload (`-l -u`)

To listen and upload a file to a specified destination upon connection:

```bash
python PyCat.py -t 0.0.0.0 -p 5555 -l -u=./received_file.txt
```

## Examples

```bash
# Listen on 192.168.0.1 on port 5555 and provide a command shell
PyCat.py -t 192.168.0.1 -p 5555 -l -c

# Listen on 192.168.0.1 on port 5555 and upload a file to c:\target.exe
PyCat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe

# Listen on 192.168.0.1 on port 5555 and execute "cat /etc/passwd"
PyCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"

# Send 'ABCDEFGHI' to 192.168.11.12 on port 135
echo 'ABCDEFGHI' | ./PyCat.py -t 192.168.11.12 -p 135
```

## Limitations or Notes

*   **Python 2 Required:** The script utilizes Python 2 `print` statement syntax. Running it with Python 3 will result in a `SyntaxError`.
*   **Server Mode Initialization Bug:** The `main` function contains a bug where `server_loop` is referenced but not called (`server_loop()`) when in listen mode. This prevents the server from actually starting and listening for connections.
*   **Network Scanning Feature Inoperable:**
    *   This feature, triggered by running `PyCat.py` without arguments, requires an external `scanner.py` module, which is not provided.
    *   Even if `scanner.py` were present, the code `run = scanner.Scan; run` in the `scan()` function does not correctly invoke the scanning logic as it assigns the class but does not call it (`run()`). As such, the network scanning functionality, as written, will not execute.
