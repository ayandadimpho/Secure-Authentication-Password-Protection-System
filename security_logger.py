from datetime import datetime



def log_event(message):
    timestamp = datetime.now()

    with open("security.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")
    print(timestamp, "-", message)

log_event("Test security event")