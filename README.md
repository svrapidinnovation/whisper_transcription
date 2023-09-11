# whisper_transcription

This codebase utilizes the Whisper ASR model to transcribe audio files. It segments longer audio into 20-minute chunks, and it can also convert MP4 videos to MP3 for transcription.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

# Clone the repository:

```
git clone https://github.com/svrapidinnovation/whisper_transcription
cd whisper_transcription

```

# Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

# Install Dependecies

```
pip install -r requirements.txt

```

# It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

```

# Run the project

```
python app.py

```
