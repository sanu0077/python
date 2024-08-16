# Q10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles 
# the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1
max_retries = 5
attemps = 0

while attemps <= max_retries:
    print("attemps",attemps+1,"-wait itme :", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemps +=1


# import time

# wait_time = 1  # Initial wait time in seconds
# max_retries = 5  # Maximum number of retries
# attempts = 0  # Counter for attempts

# while attempts < max_retries:
#     try:
#         # Simulate an operation that might fail
#         print(f"Attempt {attempts + 1}: Retrying in {wait_time} seconds...")
#         time.sleep(wait_time)  # Wait for the specified time before retrying

#         # Normally, here you'd have some code that might fail, and you'd catch an exception to retry
#         # For this example, we'll just assume the operation fails every time.
        
#         attempts += 1  # Increment the attempt counter
#         wait_time *= 2  # Double the wait time for the next attempt
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         break

# print("Max retries reached or operation succeeded.")
