```markdown
# PyCat

## Overview

PyCat is a Python-based utility that aims to replicate some of the core functionality of Netcat. It can act as both a client and a server, allowing you to send and receive data over a network. It supports command execution, file uploads, and establishing a command shell on a target machine.

## Features

*   **Client Mode:** Connect to a specified target and port, send data, and receive responses.
*   **Server Mode:** Listen on a specified port for incoming connections.
*   **Command Execution:** Execute a specified command on the target machine upon connection.
*   **File Upload:** Upload a file to a specified destination on the target machine upon connection.
*   **Command Shell:** Initialize a command shell on the target machine, allowing interactive command execution.

## Installation

No installation is necessary.  The script is self-contained. Ensure you have Python installed.

## Usage

```
PyCat.py -t target_host -p port
```

### Options

*   `-h, --help`: Display the help message.
*   `-l, --listen`: Listen on `[host]:[port]` for incoming connections.
*   `-c, --command`: Initialize a command shell.
*   `-e --execute=file_to_run`: Execute file upon connection.
*   `-u --upload=destination`: Upon connection upload a file and write to `[destination]`.
*   `-t --target`: Specify the target host.
*   `-p --port`: Specify the port number.

## Examples

### Listen for a connection and start a command shell:

```bash
PyCat.py -t 192.168.0.1 -p 5555 -l -c
```

### Listen for a connection and upload a file to a specific location:

```bash
PyCat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe
```

### Listen for a connection and execute a command:

```bash
PyCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"
```

### Send data to a target host:

```bash
echo 'ABCDEFGHI' | ./PyCat.py -t 192.168.11.12 -p 135
```

## Limitations or Notes

*   The script may require adjustments to be compatible with different operating systems, especially regarding file paths and command execution.
*   Error handling is basic; the script might exit abruptly in some situations.
*   The script contains a call to `scan()` if no command-line arguments are provided which then leads to a `SyntaxError` due to the usage of `print` as a statement instead of a function.
*   The ASCII logo contains `print` statements as a statement rather than a function, which is a `SyntaxError`.
*   The server loop is assigned to the `server_loop` variable but is never called.
```
