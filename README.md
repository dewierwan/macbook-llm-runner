# MacBook LLM Runner

A Python framework for running open-weights Language Learning Models (LLMs) efficiently on MacBooks. This project provides optimizations for both Intel and Apple Silicon processors, making it easy to run inference with popular open-source models locally.

## Features

- Efficient model loading and inference using llama.cpp
- Memory optimization techniques for resource-constrained environments
- Support for both Intel and Apple Silicon MacBooks
- Easy-to-use Python interface for model interaction
- Automatic model downloading and management

## Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate    # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```python
from llm_runner import LocalLLM

# Initialize the model
llm = LocalLLM('path/to/model.gguf')

# Generate text
response = llm.generate('Tell me about quantum computing:')
print(response)
```

## Hardware Requirements

- Minimum 8GB RAM (16GB recommended)
- MacBook with Intel processor or Apple Silicon
- At least 5GB free disk space for model storage

## Supported Models

- Mistral 7B (recommended for most users)
- TinyLlama
- Phi-2
- Other GGUF format models

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License