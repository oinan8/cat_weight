import serial
import time
import csv

# Adjust COM port and baud rate
ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1)

while True:
    line = ser.readline().decode().strip()
    if line == "READY":
        break

ser.reset_input_buffer()

with open(f'{time.strftime("%m-%d")}cat_weight.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'SensorValue'])  # Header

    try:
        while True:
            line = ser.readline().decode().strip()
            if line:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"{timestamp}, {line}")
                writer.writerow([timestamp, line])
    except KeyboardInterrupt:
        print("Logging stopped.")
        ser.close()
