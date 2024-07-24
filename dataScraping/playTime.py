from datetime import datetime, timezone

# timestamp_str = "2024-07-20T19:45:40.000Z"
def bhaiTimeKyaHai(watch):
    watch = datetime.strptime(watch, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    timeHai = int(watch.timestamp())

    # current_utc = int(datetime.now(timezone.utc).timestamp())
    return timeHai