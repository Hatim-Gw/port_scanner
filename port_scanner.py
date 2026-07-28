import socket
import threading
import argparse
import sys

def scanner(target, port, timeout):
  try:
    kali_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kali_socket.settimeout(timeout)
    result = kali_socket.connect_ex((target,port))

    if result == 0:
      banner = grab_banner(kali_socket)
      print(f"port {port}: open - service: {banner}")

    kali_socket.close()

  except socket.gaierror:
    print(f"Error: could not reslove target ip address: {target}")
  except Exception as e:
    print(f"Error: error occur while scanning the port: {port}")


def grab_banner(sock):
  try:
    banner = sock.recv(1024).decode().strip()
    return banner if banner else "Banner not found"
  except:
    print(f"No banner")

def parse_args():
  parser = argparse.ArgumentParser(description = "TCP port scanner - made by Hatim")
  parser.add_argument("target", help = "target ip address")
  parser.add_argument("-p", "--ports", default = "1-1024",  help = "ports range. e.g: 1-1024")
  parser.add_argument("-t", "--timeout", type = float, default = 1.0,  help = "timeout in second per port")

  return parser.parse_args()

def parse_port_range(port_str):
  try:
    if "-" in port_str:
      start, end = port_str.split("-")
      return range(int(start), int(end) + 1)
    else:
      return [int(port_str)]
  except Exception as e:
    print(f"Error: unexpected port argument: {port_str}, {e}")
    sys.exit(1)

if __name__ == "__main__":
  args = parse_args()
  ports = parse_port_range(args.ports)

  threads = []
  for port in ports:
    t = threading.Thread( target = scanner, args = (args.target, port, args.timeout))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
    
