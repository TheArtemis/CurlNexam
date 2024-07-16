#!/bin/bash

# Function to display usage
usage() {
  echo "Usage: $0 <directory> [-download | -d] [-p port | -port port] [-h | --help]"
  echo
  echo "Arguments:"
  echo "  <directory>        The desired exam course to see"
  echo
  echo "Options:"
  echo "  -download, -d      Execute download.py and start.py."
  echo "  -p, -port          Specify the port number to pass to start.py."
  echo "  -h, --help         Display this help message and exit."
  exit 1
}

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
  usage
fi

# Initialize variables
DOWNLOAD=false
PORT=""
DIRECTORY=""

# Get the directory from the first argument
DIRECTORY=$1
shift

# Parse the remaining arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    -h|--help)
      usage
      ;;
    -download|-d)
      DOWNLOAD=true
      ;;
    -p|-port)
      shift
      if [ -z "$1" ]; then
        echo "Error: Missing port number."
        usage
      fi
      PORT=$1
      ;;
    *)
      echo "Unknown option: $1"
      usage
      ;;
  esac
  shift
done

# Check if directory is provided
if [ -z "$DIRECTORY" ]; then
  usage
fi

# Execute download.py if -download or -d flag is provided
if [ "$DOWNLOAD" = true ]; then
  python3 "${DIRECTORY}/download.py"
fi

# Build the command to execute start.py with optional port argument
START_CMD="python3 ${DIRECTORY}/start.py"
if [ -n "$PORT" ]; then
  START_CMD="$START_CMD -p $PORT"
fi

# Execute start.py
$START_CMD