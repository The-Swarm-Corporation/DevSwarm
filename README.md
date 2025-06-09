# DevSwarm

Develop production-grade applications effortlessly with a single prompt, powered by a swarm of AI-driven autonomous agents. DevSwarm combines the power of Swarms and v0.dev to create a seamless development experience.

## Features

| Feature | Description |
|---------|-------------|
| AI-Powered Development | Leverages v0.dev and Swarms for intelligent code generation |
| Product Specification Generation | Automatically creates detailed product specifications |
| Frontend Development | Generates complete frontend applications with modern best practices |
| Type-Safe Code | Generates TypeScript/React applications with proper type definitions |
| Automated File Structure | Creates organized project structures with all necessary files |

## Prerequisites

- Python 3.8 or higher
- v0.dev API key
- Node.js (for running generated frontend applications)

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/The-Swarm-Corporation/DevSwarm.git
   cd DevSwarm
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```plaintext
   V0_API_KEY=your_v0_api_key
   ```

## Usage

The DevSwarm package provides several key functions:

1. **Creating Product Specifications**:
   ```python
   from devswarm.main import create_product_spec
   
   spec = create_product_spec("Create a todo list application")
   ```

2. **Generating Frontend Applications**:
   ```python
   from devswarm.main import dev_swarm
   
   result = dev_swarm("Create a todo list application", output_dir="my_app")
   ```

3. **Running Generated Applications**:
   After generation, navigate to the output directory and run:
   
   ```bash
   cd my_app
   npm install
   npm run dev
   ```

## Configuration

DevSwarm uses the following AI models:
- Swarms: Uses Claude 3.5 Sonnet for product specification

- v0.dev: Uses v0-1.5-md model for code generation

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please open an issue on the GitHub repository.
