import serial

# Replace 'COM3' with the serial port your Arduino is connected to
# For example, if your Arduino is connected to COM7, use 'COM7'
port = serial.Serial('COM3', baudrate=115200, timeout=3.0)

while True:
    try:
        # Read a line from the serial port
        line = port.readline().decode('utf-8').strip()
        # Print the received line
        print(line)
    except KeyboardInterrupt:
        # Exit the loop when Ctrl+C is pressed
        break

port.close()
