import requests
#Install the "requests" using 'pip install requests'

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an error for bad status
        ip_data = response.json()
        print(f"Your public IP address is: {ip_data['ip']}")
    except requests.RequestException as e:
        print(f"An error occurred while trying to get the IP address: {e}")

if __name__ == "__main__":
    get_public_ip()
