import requests
import time

def test_summarization():
    print("Testing Summarization Service...")
    url = "http://localhost:8001/summarize"
    data = {
        "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
        "max_length": 60,
        "min_length": 20
    }
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Summary: {response.json()['summary']}")
    except Exception as e:
        print(f"Error: {e}")

def test_qa():
    print("\nTesting QA Service...")
    url = "http://localhost:8002/answer"
    data = {
        "question": "How tall is the Eiffel Tower?",
        "context": "The Eiffel Tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris."
    }
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Answer: {response.json()['answer']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Local ports: 8001 (Summarization), 8002 (QA)")
    print("Vercel Unified: /summarize, /answer")
    test_summarization()
    test_qa()
