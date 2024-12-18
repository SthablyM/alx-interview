#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import signal

total_file_size = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0
def print_statistics():
    """
    Prints the current file size and status code metrics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def handle_interrupt(signal, frame):
    """
    Handles the keyboard interrupt to print stats before exit.
    """
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            file_size = int(parts[-1])
            status_code = parts[-2]
            
            total_file_size += file_size
            
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
            
            line_count += 1
            
            if line_count % 10 == 0:
                print_statistics()
        except (IndexError, ValueError):
            continue
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
