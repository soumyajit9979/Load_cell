import serial
import requests

# Configure the serial port
port = "COM32"  # Replace with the actual port name
baud_rate = 57600  # Replace with the baud rate of your serial connection

# Configure ThingSpeak
api_key = "IR5CN84QSL6IO9YV"  # Replace with your ThingSpeak API key
api_url = f"https://api.thingspeak.com/update?api_key={api_key}"

# Open the serial port
ser = serial.Serial(port, baud_rate)
count = 0
# Read data from the serial port and send it to ThingSpeak
while True:
    try:
        # Read a line from the serial monitor
        line = ser.readline().decode().strip()
        print(line)

        # Print the received data
        print(f"Received: {line}")
        count = count + 1

        if count == 100:
            # Send the data to ThingSpeak
            payload = {"field1": line}
            response = requests.get(api_url, params=payload)

            # Print the response from ThingSpeak
            print(f"ThingSpeak response: {response.text}")
            count = 0

    except KeyboardInterrupt:
        # Close the serial port on keyboard interrupt
        ser.close()
        break
