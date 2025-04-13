# OrcBlock - Website Blocker

A simple and effective Python-based website blocker that helps you stay focused by blocking access to distracting websites. It works by modifying your system's hosts file to redirect specified websites to localhost.

## Features

- Add websites to block list
- Remove websites from block list
- Make certain websites overridable
- Real-time blocking and unblocking
- Simple command-line interface

## Requirements

- Python 3.x
- Typer (for CLI)
- Administrative privileges (to modify hosts file)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/orcblock.git
cd orcblock
```

2. Install the required dependencies:
```bash
pip install typer
```

3. Make the script executable:
```bash
chmod +x src/wblock.py
```

## Usage

### Adding a Website to Block
```bash
./src/wblock.py add "example.com"
```

To make a website overridable (can be unblocked temporarily):
```bash
./src/wblock.py add "example.com" --overridable
```

### Removing a Website from Block List
```bash
./src/wblock.py remove "example"
```

### Running the Blocker
```bash
./src/wblock.py run
```

The blocker will run continuously until you stop it (Ctrl+C). When stopped, it will automatically unblock all websites.

## How It Works

The application works by modifying your system's `/etc/hosts` file to redirect specified websites to localhost (127.0.0.1). This effectively blocks access to the websites on your system.

## Notes

- Requires administrative privileges to modify the hosts file
- The websites.json file stores your block list configuration
- Use Ctrl+C to stop the blocker and unblock all websites

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
