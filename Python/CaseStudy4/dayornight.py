import time

def is_dark():
    current_time = time.localtime().tm_hour
    if current_time >= 6 and current_time < 18:
        return "It's day."
    else:
        return "It's night."

# Example usage:
print(is_dark())
