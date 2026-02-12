```markdown
# PyCat

## Overview
PyCat is a Python-based utility that serves as a replacement for Netcat. It allows users to create TCP/UDP connections, execute commands remotely, upload files, and listen for incoming connections.

## Features
- **Listen Mode**: Set the script to listen on a specified host and port for incoming connections.
- **Command Execution**: Execute a specified command upon connection.
- **File Upload**: Upload files to the target machine.
- **Interactive Shell**: Open a command shell on the target machine for interactive command execution.

## Installation
To use PyCat, ensure you have Python installed on your system. You can run the script directly without any additional installation steps.

## Usage
Run the script with the following command-line options:

```
PyCat.py -t target_host -p port [options]
```

### Options
- `-h`, `--help`: Display help message.
- `-l`, `--listen`: Listen for incoming connections.
- `-c`, `--command`: Initialize a command shell.
- `-e`, `--execute=file_to_run`: Execute a specified file upon connection.
- `-u`, `--upload=destination`: Upload a file to the specified destination on the target machine.

### Example Commands
1. To listen for incoming connections and open a command shell:
   ```
   PyCat.py -t 192.168.0.1 -p 5555 -l -c
   ```
2. To listen for incoming connections and upload a file:
   ```
   PyCat.py -t 192.168.0.1 -p 5555 -l -u=c:\target.exe
   ```
3. To execute a command upon connection:
   ```
   PyCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"
   ```
4. To send data from standard input to a target:
   ```
   echo 'ABCDEFGHI' | python PyCat.py -t 192.168.11.12 -p 135
   ```

## Examples
- **Listening and Executing Commands**: 
   ```
   PyCat.py -t 0.0.0.0 -p 9999 -l -c
   ```
   This command listens on all interfaces and opens a command shell for any connecting clients.

- **File Upload**:
   ```
   PyCat.py -t 192.168.0.1 -p 5555 -l -u=/path/to/uploaded_file
   ```
   This command allows a client to upload a file to the specified path on the server.

## Limitations or Notes
- The script is designed for Python 2.x due to the print statement syntax. Ensure you run it in an appropriate Python environment.
- The script may require administrative privileges for certain operations, especially when binding to low-numbered ports or executing commands.
- Use responsibly and ensure you have permission to connect to and interact with the target hosts.
```
