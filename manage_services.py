import subprocess
import time
import requests
import sys
import os

def start_service(name, path, port):
    print(f"Starting {name} on port {port}...")
    log_file = open(f"{name}.log", "w")
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", str(port)],
        cwd=path,
        stdout=log_file,
        stderr=log_file
    )
    return process

def wait_for_health(port, name, timeout=120):
    start_time = time.time()
    url = f"http://localhost:{port}/health"
    print(f"Waiting for {name} to be healthy at {url}...")
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{name} is UP!")
                return True
        except:
            pass
        time.sleep(5)
    print(f"Timeout waiting for {name}")
    return False

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sum_path = os.path.join(base_dir, "services/summarization")
    qa_path = os.path.join(base_dir, "services/question_answering")

    p1 = start_service("summarization", sum_path, 8001)
    p2 = start_service("qa", qa_path, 8002)

    s1 = wait_for_health(8001, "Summarization")
    s2 = wait_for_health(8002, "QA")

    if s1 and s2:
        print("\nBoth services are running! Running tests...")
        subprocess.run([sys.executable, "test_services.py"], cwd=base_dir)
    else:
        print("\nFailed to start services within timeout. Check logs.")
        p1.terminate()
        p2.terminate()
