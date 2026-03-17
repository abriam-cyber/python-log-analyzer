def analyze_log(file_path):
    failed_logins = 0
    successful_logins = 0
    suspicious_ips = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if "FAILED LOGIN" in line:
                failed_logins += 1

                parts = line.split("IP:")
                if len(parts) > 1:
                    ip = parts[1].strip()
                    suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1

            elif "SUCCESSFUL LOGIN" in line:
                successful_logins += 1

    print("=== Log Analysis Summary ===")
    print(f"Failed logins: {failed_logins}")
    print(f"Successful logins: {successful_logins}")
    print("\nSuspicious IPs:")
    
    for ip, count in suspicious_ips.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts (HIGH RISK)")
    elif count >= 2:
        print(f"{ip} - {count} failed attempts (MEDIUM RISK)")


if __name__ == "__main__":
    analyze_log("sample_log.txt")
