import socket

def load_endpoints(file_path):
    """Load endpoints from a file."""
    try:
        with open("/home/kali/Documents/VPN/THM/Machines/008-Pyrat/endpoints.txt", "r") as file:
            endpoints = [line.strip() for line in file.readlines()]
        return endpoints
    except Exception as e:
        print(f"Error loading endpoints: {e}")
        return []

def fuzz_endpoints(ip, port, endpoints):
    for endpoint in endpoints:
        url = f"http://{ip}:{port}/{endpoint}"  # Constructing the URL
        print(f"Testing URL: {url}")  # Display the formed URL

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, port))
            print(f"EndPoint: {endpoint}")
            client_socket.sendall(endpoint.encode() + b'\n')
            response = client_socket.recv(1024)
            print(f"Response from EndPoint {endpoint}: {response.decode()}\n")
            client_socket.close()
        except Exception as e:
            print(f"Error with EndPoint {endpoint}: {e}")

# Load endpoints from a file
endpoint_file = "endpoints.txt"
endpoint_list = load_endpoints(endpoint_file)

# Target IP and port
target_ip = "10.10.197.160"
target_port = 8000

# Fuzz the endpoints
fuzz_endpoints(target_ip, target_port, endpoint_list)
