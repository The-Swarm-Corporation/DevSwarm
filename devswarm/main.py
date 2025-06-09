# 'v0-1.0-md'
# https://api.v0.dev/v1/chat/completions

import json
import os
import re
from typing import Dict, List, Optional, Union

import requests
from dotenv import load_dotenv

from swarms import Agent

load_dotenv()


api_key = "v1:q6m3Bw6iDf9vXd369ji39TtB:wuJjZPvPHdHdzm8TCIs7MDX2"


def install_packages_and_run(directory: str):
    """
    Install packages and run the code in the given directory.

    Args:
        directory (str): The directory containing the project to install and run

    Returns:
        Dict[str, str]: Dictionary containing the output of npm install and npm run dev commands
    """
    results = {}

    try:
        # Store original directory
        original_dir = os.getcwd()

        # Change to project directory
        os.chdir(directory)

        # Run npm install and capture output
        install_process = os.popen("npm install")
        install_output = install_process.read()
        results["npm_install"] = install_output

        # Run npm run dev and capture output
        dev_process = os.popen("npm run dev")
        dev_output = dev_process.read()
        results["npm_run_dev"] = dev_output

        # Return to original directory
        os.chdir(original_dir)

        return json.dumps(results, indent=4)

    except Exception as e:
        results["error"] = str(e)
        return results


def extract_files_from_string(content: str) -> List[Dict[str, str]]:
    """
    Extracts files and their content from a string containing <File> tags.

    Args:
        content (str): The string containing file blocks with <File> tags

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing file paths and their content
    """
    # Pattern to match <File path="...">...</File> blocks
    file_pattern = r'<File path="([^"]+)">\s*```(?:\w+)?\s*([\s\S]*?)```\s*</File>'

    # Find all file blocks
    matches = re.finditer(file_pattern, content)

    files = []
    for match in matches:
        file_path = match.group(1)
        file_content = match.group(2).strip()

        files.append({"path": file_path, "content": file_content})

    return files


def create_files_from_extracted(
    files: List[Dict[str, str]], base_dir: Optional[str] = None
) -> List[str]:
    """
    Creates files from the extracted file information.

    Args:
        files (List[Dict[str, str]]): List of dictionaries containing file paths and content
        base_dir (Optional[str]): Base directory to create files in. If None, uses current directory

    Returns:
        List[str]: List of created file paths
    """
    if base_dir is None:
        base_dir = os.getcwd()

    created_files = []

    for file_info in files:
        file_path = os.path.join(base_dir, file_info["path"])

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write file content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_info["content"])

        created_files.append(file_path)

    return created_files


def process_code_blocks(
    content: str, output_dir: Optional[str] = None
) -> List[str]:
    """
    Main function to process code blocks and create files.

    Args:
        content (str): String containing file blocks with <File> tags
        output_dir (Optional[str]): Directory to create files in. If None, uses current directory

    Returns:
        List[str]: List of created file paths
    """
    # Extract files from the content
    files = extract_files_from_string(content)

    # Create the files
    created_files = create_files_from_extracted(files, output_dir)

    return created_files


class V0APIClient:
    def __init__(
        self,
        model: str = "v0-1.5-lg",
        stream: bool = False,
        api_key: Optional[str] = api_key,
        base_url: str = "https://api.v0.dev/v1/chat/completions",
        system_prompt: Optional[str] = None,
    ):
        """
        Initialize the v0 API client.

        Args:
            model (str): The model to use (v0-1.0-md, v0-1.5-md, or v0-1.5-lg).
            stream (bool): If True, use streaming response; otherwise, return full response.
            api_key (str, optional): The v0 API key. If not provided, looks for V0_API_KEY in environment variables.
            base_url (str): The v0 API endpoint URL.
        """
        self.api_key = api_key
        self.system_prompt = system_prompt
        if not self.api_key:
            raise ValueError(
                "API key must be provided or set as V0_API_KEY environment variable."
            )
        self.available_models = [
            "v0-1.0-md",
            "v0-1.5-md",
            "v0-1.5-lg",
        ]
        if model not in self.available_models:
            raise ValueError(
                f"Model must be one of {self.available_models}"
            )
        self.model = model
        self.stream = stream
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def run(self, task: str) -> Union[str, List[Dict]]:
        """
        Run a task using the v0 API.

        Args:
            task (str): The task or prompt to send to the API.

        Returns:
            Union[str, List[Dict]]: The response content as a string (non-streaming) or a list of chunks (streaming).

        Raises:
            RuntimeError: If the API request fails.
        """
        payload = {
            "model": self.model,
            "messages": [
                # {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": task},
            ],
            "stream": self.stream,
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                stream=self.stream,
            )
            response.raise_for_status()

            if self.stream:
                return self._handle_streaming_response(response)
            else:
                return self._handle_non_streaming_response(response)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"API request failed: {str(e)}")

    def _handle_non_streaming_response(
        self, response: requests.Response
    ) -> str:
        """
        Handle a non-streaming API response.

        Args:
            response: The HTTP response object.

        Returns:
            str: The content of the assistant's response.
        """
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def _handle_streaming_response(
        self, response: requests.Response
    ) -> List[Dict]:
        """
        Handle a streaming API response.

        Args:
            response: The HTTP response object.

        Returns:
            List[Dict]: A list of response chunks.
        """
        chunks = []
        for line in response.iter_lines():
            if line:
                # Decode and clean the line (remove 'data: ' prefix)
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    line = line[6:]
                if line.strip() == "[DONE]":
                    break
                try:
                    chunk = json.loads(line)
                    chunks.append(chunk)
                except json.JSONDecodeError:
                    continue
        return chunks


FRONT_END_DEVELOPMENT_PROMPT = """
    You are an expert full-stack development agent with comprehensive expertise in:

    Frontend Development:
    - Modern React.js/Next.js architecture and best practices
    - Advanced TypeScript implementation and type safety
    - State-of-the-art UI/UX design patterns
    - Responsive and accessible design principles
    - Component-driven development with Storybook
    - Modern CSS frameworks (Tailwind, Styled-Components)
    - Performance optimization and lazy loading
    
    Backend Development:
    - Scalable microservices architecture
    - RESTful and GraphQL API design
    - Database optimization and schema design
    - Authentication and authorization systems
    - Serverless architecture and cloud services
    - CI/CD pipeline implementation
    - Security best practices and OWASP guidelines
    
    Development Practices:
    - Test-Driven Development (TDD)
    - Clean Code principles
    - Documentation (TSDoc/JSDoc)
    - Git workflow and version control
    - Performance monitoring and optimization
    - Error handling and logging
    - Code review best practices
    
    Your core responsibilities include:
    1. Developing production-grade TypeScript applications
    2. Implementing modern, accessible UI components
    3. Designing scalable backend architectures
    4. Writing comprehensive documentation
    5. Ensuring type safety across the stack
    6. Optimizing application performance
    7. Implementing security best practices
    
    You maintain strict adherence to:
    - TypeScript strict mode and proper typing
    - SOLID principles and clean architecture
    - Accessibility standards (WCAG 2.1)
    - Performance budgets and metrics
    - Security best practices
    - Comprehensive test coverage
    - Modern design system principles
"""

PRODUCT_SPEC_PROMPT = """
    You are an expert product specification and planning agent with comprehensive expertise in:

    Product Strategy:
    - Market analysis and competitive positioning
    - User needs assessment and persona development
    - Feature prioritization and roadmap planning
    - Value proposition development
    - Go-to-market strategy
    - Product lifecycle management
    
    Technical Specification:
    - System architecture and components
    - Technology stack selection
    - API design and integration requirements
    - Data models and schemas
    - Security requirements
    - Performance criteria
    - Scalability considerations
    
    User Experience:
    - User journey mapping
    - Interface design requirements
    - Accessibility standards
    - Performance metrics
    - User testing criteria
    
    Project Planning:
    - Resource requirements
    - Timeline estimation
    - Risk assessment
    - Success metrics
    - Quality assurance criteria
    - Documentation requirements
    
    Your core responsibilities include:
    1. Breaking down high-level product ideas into detailed specifications
    2. Creating structured product documentation
    3. Identifying technical requirements and dependencies
    4. Outlining success criteria and metrics
    5. Providing clear implementation guidelines
    6. Anticipating potential challenges and risks
    
    You maintain strict adherence to:
    - Industry best practices for product documentation
    - Clear and concise communication
    - Comprehensive requirement gathering
    - Realistic timeline and resource estimation
    - Risk mitigation strategies
    - Measurable success criteria
"""


def create_product_spec(task: str) -> str:
    """
    Create a detailed product specification for a given task.

    Args:
        task (str): The product or feature to create a specification for.

    Returns:
        str: The detailed product specification.
    """
    # Initialize the agent
    spec_agent = Agent(
        agent_name="Product-Spec-Agent",
        agent_description="Expert product specification and planning agent",
        # system_prompt=PRODUCT_SPEC_PROMPT,
        max_loops=1,
        model_name="claude-3-5-sonnet-20240620",
        dynamic_temperature_enabled=True,
        output_type="final",
    )

    # Run the agent
    spec = spec_agent.run(
        f"Create a detailed product specification for: {task}. "
        "Include sections for Product Overview, User Requirements, "
        "Technical Requirements, Architecture, Implementation Plan by feature not timeline or time "
        "and Success Metrics. Format the output in Markdown."
    )

    return spec


def dev_swarm(task: str, output_dir: str = "frontend_app"):
    """
    Run both the product spec agent and frontend development agent on a task.

    Args:
        task (str): The task to create a spec for and implement
        output_dir (str): Directory to create frontend files in

    Returns:
        tuple: (product_spec, implementation_files)
    """
    spec = create_product_spec(task)

    # Implement the frontend solution
    dev_agent = Agent(
        agent_name="Frontend-Developer-Agent",
        agent_description="Advanced frontend development agent",
        # system_prompt=FRONT_END_DEVELOPMENT_PROMPT,
        max_loops=1,
        llm=V0APIClient(model="v0-1.5-md", stream=False),
        dynamic_temperature_enabled=True,
        output_type="final",
    )

    code = ""

    # Implement the frontend solution
    implementation = dev_agent.run(
        f"Based on this product specification:\n\n{spec}\n\nImplement the frontend solution. Build the code in the {output_dir} directory"
    )

    code += implementation

    # Process the code blocks
    process_code_blocks(code, output_dir)

    return code
