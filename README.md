# DevSwarm

Develop production-grade applications effortlessly with a single prompt, powered by a swarm of AI-driven autonomous agents. DevSwarm combines the power of Swarms and v0.dev to create a seamless development experience.

## Current Features

| Feature | Description |
|---------|-------------|
| AI-Powered Development | Leverages v0.dev and Swarms for intelligent code generation |
| Product Specification Generation | Automatically creates detailed product specifications |
| Frontend Development | Generates complete frontend applications with modern best practices |
| Type-Safe Code | Generates TypeScript/React applications with proper type definitions |
| Automated File Structure | Creates organized project structures with all necessary files |

## Upcoming Features 🚀

| Feature | Description | Status |
|---------|-------------|---------|
| Structured Multi-Agent Team | Team of 8 specialized developer agents collaborating on projects | In Development |
| CTO Agent Oversight | Dedicated CTO agent directing the team, ensuring strategic alignment | In Development |
| 24/7 Autonomous Development | Continuous code updates running around the clock | Planning |
| Autonomous Vercel Deployment | Seamless deployment to Vercel with zero manual intervention | Planning |
| Customizable Settings | Flexible parameters for agent behavior, testing frequency, and deployment | In Development |
| Autonomous Testing | Built-in unit tests and continuous improvement pipeline | Planning |

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

## Contributing 🤝

We strongly encourage and welcome contributions from the community! Here's how you can contribute:

### Ways to Contribute

1. **Code Contributions**
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/amazing-feature`)
   - Commit your changes (`git commit -m 'Add amazing feature'`)
   - Push to the branch (`git push origin feature/amazing-feature`)
   - Open a Pull Request

2. **Feature Development**
   - Pick an upcoming feature from our roadmap
   - Discuss implementation approaches in Issues
   - Collaborate with other developers

3. **Documentation**
   - Improve README and documentation
   - Add code comments
   - Create examples and tutorials

4. **Testing**
   - Write unit tests
   - Perform integration testing
   - Report bugs and issues

5. **Feature Requests**
   - Open Issues for new feature ideas
   - Participate in feature discussions
   - Help prioritize the roadmap

### Development Setup

1. Set up your development environment:
   ```bash
   git clone https://github.com/The-Swarm-Corporation/DevSwarm.git
   cd DevSwarm
   pip install -r requirements.txt
   ```

2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and test thoroughly

4. Submit a Pull Request with:
   - Clear description of changes
   - Screenshots/examples if applicable
   - Tests for new features
   - Updated documentation

### Contribution Guidelines

- Follow the existing code style and conventions
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Be respectful and collaborative
- Start with small contributions

### Getting Help

- Join our community discussions in Issues
- Ask questions in Pull Requests
- Check our documentation
- Reach out to maintainers

Your contributions help make DevSwarm better for everyone! 🌟

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions:
- Open an issue on GitHub
- Join our community discussions
- Check our documentation

Powered by [Swarms](https://github.com/swarms) x [v0.dev](https://v0.dev) 🚀
