import faker
import random
import geoip2.database
import json

EVENT_COUNT = 120000

EVENT_TYPES = [
    "Authentication and Access Control",
    "Network Activities",
    "Endpoint and Malware Events",
    "Data Loss and Exfiltration",
    "System and Configuration Changes",
    "Intrusion and Exploit Activity",
    "Compliance and Policy Violations",
    "User Activity Monitoring",
    "Configuration Change Events",
    "Incident Tracking",
    "Host-Level Security Events",
    "Web Server Activity",
    "Log Source Activity",
    "Application Errors or Crashes",
    "Privilege Escalation Attempts",
    "File Integrity Monitoring Events",
    "System Health or Performance Issues",
    "Access to Critical or Sensitive Resources",
    "Unusual User/Entity Behavior (UEBA)",
    "Connection to Blacklisted or Malicious Destinations",
    "Policy and Compliance Violations",
    "Phishing Attack Detection",
    "Data Movement and Copy Events",
    "Malware and Ransomware Detection",
    "Unauthorized Application Usage",
    "Process and Memory Anomalies",
    "First-Time or Rare Network Activities",
    "Multiple Account Lockouts",
    "Service Downtime or Outage Events",
    "Port Scanning and Reconnaissance"
]

if __name__ == "__main__":
    reader = geoip2.database.Reader("GeoLite2-City.mmdb")
    fake = faker.Faker()
    data = []
    for i in range(EVENT_COUNT):
        source_ip = fake.ipv4_public()
        destination_ip = fake.ipv4_public()
        try:
            source = reader.city(source_ip)
            destination = reader.city(destination_ip)
            random.seed(random.randint(10000, 5000000))
            record = {
                "id": fake.uuid4(),
                "event": random.choice(EVENT_TYPES),
                "timestamp": int(str(fake.date_time_between(start_date="-1d" , end_date="now").timestamp()).split('.')[0]),
                "source_ip": source_ip,
                "destination_ip": destination_ip,
                "source_lat": float(source.location.latitude),
                "source_lon": float(source.location.longitude),
                "source_country": source.country.name,
                "destination_lat": float(destination.location.latitude),
                "destination_lon": float(destination.location.longitude),
                "destination_country": destination.country.name,
            }
            data.append(record)
        except:
            continue

    data.sort(key=lambda x: x["timestamp"])

    with open("mock_records.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)
