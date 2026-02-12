# PyCat

## Overview
PyCat is a Python-based utility that serves as a replacement for Netcat, allowing users to create TCP connections, execute commands, and transfer files over the network. It provides a simple command-line interface for various networking tasks.

## Features
- **Listen Mode**: Set up a server to listen for incoming connections.
- **Command Execution**: Execute specified commands upon connection.
- **File Upload**: Upload files to a specified destination on the server.
- **Interactive Shell**: Open a command shell for interactive command execution.
- **Network Scanning**: Scan the local network for active hosts.

## Installation
To use PyCat, ensure you have Python installed on your system. No additional libraries are required beyond the standard library. Simply download the `PyCat.py` file and make it executable.

## Usage
Run the script from the command line with the following syntax:

```bash
python PyCat.py -t target_host -p port [options]
```

### Options
- `-h`, `--help`: Display help message.
- `-l`, `--listen`: Listen for incoming connections.
- `-c`, `--command`: Initialize a command shell.
- `-e`, `--execute=file_to_run`: Execute a specified file upon connection.
- `-u`, `--upload=destination`: Upload a file to the specified destination.
- `-p`, `--port`: Specify the port number to use.

### Example Commands
1. Start a listener and open a command shell:
   ```bash
   python PyCat.py -t 192.168.0.1 -p 5555 -l -c
   ```

2. Upload a file to the target host:
   ```bash
   python PyCat.py -t 192.168.0.1 -p 5555 -l -u=c:\target.exe
   ```

3. Execute a command upon connection:
   ```bash
   python PyCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"
   ```

4. Send data from standard input to the target host:
   ```bash
   echo 'ABCDEFGHI' | python PyCat.py -t 192.168.11.12 -p 135
   ```

## Examples
- To scan the local network, simply run:
  ```bash
  python PyCat.py
  ```
  This will display available options for interacting with hosts that are up.

## Limitations or Notes
- The script currently uses Python 2 syntax (e.g., `print` statements without parentheses). Ensure you run it in a compatible environment or modify the code for Python 3 compatibility.
- The network scanning feature references an external `scanner` module, which is not included in this script. Ensure that this module is available in your environment if you wish to use the scanning functionality.
- Use caution when executing commands or uploading files, as this tool can be used for both legitimate and malicious purposes. Always ensure you have permission to interact with the target systems.
