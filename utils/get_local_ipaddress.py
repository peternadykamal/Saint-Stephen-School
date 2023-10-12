import socket


def get_ip_address():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  ipaddress = s.getsockname()[0]
  s.close()
  return ipaddress
