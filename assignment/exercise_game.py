"""
Response time - single-threaded
"""

from machine import Pin
import time
import random
import json

# Added import for Cloud Solution:
import urequests as requests

# Added os import for GitHub actions usage
import os

N: int = 10  # Changed 3 -> 10, requires 10 flashes
sample_ms = 10.0
on_ms = 500

# Added oauth_token:
oauth_token = os.getenv("FIREBASE_OAUTH_TOKEN") 

# Cloud function to connect to Firestore DB
def send_to_firestore(data: dict) -> None:
    firebase_url = "https://firestore.googleapis.com/v1/projects/mini-c686c/databases/(default)/documents/responses"
    headers = {
        'Authorization': f'Bearer {oauth_token}',  # Use the OAuth token here
        'Content-Type': 'application/json',
    }
    now = time.localtime()
    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    
    firestore_data = {
        "fields": {
            "avg_resp_time": {"doubleValue": data["avg_resp_time"]},
            "min_resp_time": {"doubleValue": data["min_resp_time"]},
            "max_resp_time": {"doubleValue": data["max_resp_time"]},
            "score": {"doubleValue": data["score"]},
            "timestamp": {
                "timestampValue": f"{now[0]}-{now[1]:02d}-{now[2]:02d}T{now[3]:02d}:{now[4]:02d}:{now[5]:02d}Z"
            }
        }
    }

    # POST the JSON data to Firestore
    response = requests.post(firebase_url, data=json.dumps(firestore_data), headers=headers)
    print("Response from Firestore:", response.text)

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    
    
    # TODO: Add error caatching if len(t_good) is 0 will still run
    data = {
        "avg_resp_time": sum(t_good) / len(t_good),
        "min_resp_time": min(t_good),
        "max_resp_time": max(t_good),
        "score": 1 - misses / len(t),
    }
    
    # Also write to Firestore DB:
    send_to_firestore(data)


    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)
