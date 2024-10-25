#!/usr/bin/env python3
""""script that reads stdin line by line and computes metrics"""

import sys
import signal

total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """Prints the total file size and status code statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (Ctrl + C) gracefully by printing the stats.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            ip_address = parts[0]
            date = parts[3][1:]
            request_method = parts[5][1:]
            request_path = parts[6]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            if request_method == "GET" and request_path == "/projects/260":
                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                line_count += 1
                if line_count % 10 == 0:
                    print_stats()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print_stats
    sys.exit(0)
