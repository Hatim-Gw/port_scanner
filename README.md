# Python port scanner

# Objective:
I made a simple tcp port scanner to understand how nmap works and to build my own tools.

# Description:
I started this project from scratch by adding  socket library to scan the target's ports, then implemented multi-threading to reduce scanning time. After that, I added banner detection. Moreover, I implemented argparse library to enhance usability,  and eventually I added error handling for many cases and tested them.


# Tool's features:
1. Multi-threading scanning.
2. Banner detection (on open ports)
3. CLI arguments (target, ports, timeout)
4. Input validation(target, ports)

## Usage

  python3 port_scanner.py <target_ip> -p <port-range> -t <timeout>

  Examples:
  python3 port_scanner.py 192.168.2.15 -p 1-1024
  python3 port_scanner.py 192.168.2.15 -p 22
  python3 port_scanner.py --help




# Results:
- before *threading*, to scan 30 ports it took 29.09s; with *threading* it took 1.05s for the same range.
- Banner detection confirmed working against SSH service (Ubuntu server), by identifying the exact version(note: from a defensive perspective, it's a real concern to think about in the future!)


# problem encountered:
Handling string input in the ports argument was a tough task; it wasn't enough to capture the string but to exit the program. Then I figured out that using sys.exit(1) can terminate with a clear error message as output.

