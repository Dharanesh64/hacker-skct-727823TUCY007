# student_name: Dharanesh A
# roll_number: 727823TUCY007

import datetime
import subprocess

print("Roll Number: 727823TUCY007")
print("Timestamp:", datetime.datetime.now())

print("Running Vulnerability Scanner...\n")

target = "192.168.56.101"

subprocess.run(["python3", "code/tool_main.py"], input=target.encode())
