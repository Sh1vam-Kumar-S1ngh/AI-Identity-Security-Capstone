from datetime import datetime, timedelta

print("=" * 70)
print("SECURENOVA PROJECT 4 - ANOMALY DETECTION")
print("=" * 70)

identity = "SecureNova-AI-Agent"
threshold = 20
window_seconds = 60

events = []

start_time = datetime.now()

for i in range(25):
    events.append({
        "timestamp": start_time + timedelta(seconds=i),
        "identity": identity,
        "event_type": "LLM_API_CALL"
    })

print("\nMonitoring LLM API requests...")
print("Threshold: more than 20 requests in 60 seconds")
print("Identity:", identity)

request_count = len(events)

print("\nRequests detected:", request_count)

if request_count > threshold:
    print("\n" + "!" * 70)
    print("ANOMALY DETECTED")
    print("!" * 70)
    print("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Identity:", identity)
    print("Event Type: LLM_API_CALL_VOLUME_SPIKE")
    print("Requests in 60 seconds:", request_count)
    print("Threshold:", threshold)
    print("ALERT: API call volume exceeded allowed threshold")
    print("!" * 70)
else:
    print("\nNo anomaly detected.")

print("\n" + "=" * 70)
print("ANOMALY DETECTION TEST COMPLETE")
print("=" * 70)
