from collections import deque

# Read input for robots and their processing times
robots_data = input().split(";")
robots = []
for data in robots_data:
    name, process_time = data.split("-")
    # Initialize available_at with the start time '08:00:00' in total seconds (0 seconds past start time)
    robots.append({
        "name": name,
        "process_time": int(process_time),
        "available_at": 0  # Start time in seconds from '08:00:00'
    })

# Read start time and split it into hours, minutes, and seconds
start_time = input()
hours, minutes, seconds = map(int, start_time.split(":"))

# Convert the start time to total seconds
current_time = hours * 3600 + minutes * 60 + seconds

# Initialize the queue for products
products = deque()

# Read products until 'End' is encountered
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

# Helper to format time into a string
def format_time(total_seconds):
    h = (total_seconds // 3600) % 24
    m = (total_seconds // 60) % 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

# Processing the products
while products:
    # Increment the time by one second
    current_time += 1

    # Check each robot's availability
    available = False
    for robot in robots:
        # Check if robot is available
        if robot["available_at"] <= current_time:
            # Assign product to the robot
            product = products.popleft()
            print(f"{robot['name']} - {product} [{format_time(current_time)}]")

            # Calculate next available time for the robot in total seconds
            robot["available_at"] = current_time + robot["process_time"]
            available = True
            break

    # If no robot was available, requeue the product
    if not available:
        products.append(products.popleft())
