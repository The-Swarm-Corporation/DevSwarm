from devswarm.main import dev_swarm

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    task = "Build a simple web app that says hello world in a cyberpunk style"
    out = dev_swarm(task, "frontend_app")
    print(out)
