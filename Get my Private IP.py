import socket

def get_private_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"Your private IP address is: {local_ip}")
    except socket.error as e:
        print(f"An error occurred while getting the private IP address: {e}")

if __name__ == "__main__":
    get_private_ip()
