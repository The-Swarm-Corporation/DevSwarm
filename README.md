DevSwarm
 
Develop production-grade applications effortlessly with a single prompt, powered by a swarm of v0-driven autonomous agents operating 24/7 for fully autonomous software development.
Prompt → App
DevSwarm leverages a structured multi-agent system, orchestrated by a CTO agent, to deliver seamless, high-quality software development with continuous updates, autonomous deployment, and customizable configurations.
Features

Structured Multi-Agent Team: Eight specialized developer agents collaborate to build robust applications.
CTO Agent Oversight: A dedicated CTO agent directs the team, ensuring strategic alignment and efficiency.
24/7 Autonomous Development: Continuous code updates run around the clock for rapid development cycles.
Autonomous Deployment: Seamlessly deploy applications on Vercel with zero manual intervention.
Fully Customizable Settings: Flexible parameters allow tailored workflows to meet specific project needs.
Autonomous Testing & Improvement: Built-in unit tests and continuous improvement ensure code quality.

Powered By

Swarms for multi-agent orchestration
v0 for AI-driven development

Installation

Note: DevSwarm is currently in early access. Follow these steps to set up the environment.

Prerequisites

Node.js (v16 or higher)
Vercel CLI (npm install -g vercel)
Git
API keys for Swarms and v0 (request access via their respective platforms)

Steps

Clone the repository:git clone https://github.com/devswarm/devswarm.git
cd devswarm


Install dependencies:npm install


Configure environment variables:
Create a .env file in the root directory.
Add the following:SWARMS_API_KEY=your_swarms_api_key
V0_API_KEY=your_v0_api_key
VERCEL_TOKEN=your_vercel_token




Start the DevSwarm CLI:npm run start



Usage

Initialize a Project:Run the following command and provide a prompt describing your application:devswarm init "Create a full-stack e-commerce platform with React and Node.js"


Monitor Development:The CTO agent will assign tasks to developer agents, and code updates will be logged in real-time.
Deploy to Vercel:Once the application is ready, DevSwarm automatically deploys to Vercel. Access the deployment URL in the logs.
Customize Settings:Modify configurations in config/devswarm.json to adjust agent behavior, testing frequency, or deployment options.

Example Prompt
"Build a task management app with a React frontend, Express backend, and MongoDB integration."

Configuration
Customize DevSwarm via the config/devswarm.json file. Key options include:

agentCount: Number of developer agents (default: 8)
updateInterval: Frequency of code updates (in seconds)
testCoverage: Minimum unit test coverage percentage
deploymentPlatform: Target platform (default: "vercel")

Example configuration:
{
  "agentCount": 8,
  "updateInterval": 3600,
  "testCoverage": 90,
  "deploymentPlatform": "vercel"
}

Contributing
We welcome contributions to DevSwarm! To get started:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please follow our Code of Conduct and review the Contributing Guidelines.
License
DevSwarm is licensed under the MIT License.
Contact
For support or inquiries, reach out to us at:

Email: support@devswarm.dev
Twitter: @DevSwarm

Join the future of autonomous software development with DevSwarm! 🚀
