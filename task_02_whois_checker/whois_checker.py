import whois
import csv
from datetime import datetime

def fetch_whois_info(domain):
    try:
        info = whois.whois(domain)
        return {
            'Domain': domain,
            'Registrar': info.registrar,
            'Creation Date': str(info.creation_date),
            'Expiration Date': str(info.expiration_date),
            'Name Servers': ", ".join(info.name_servers) if info.name_servers else 'N/A'
        }
    except Exception as e:
        return {
            'Domain': domain,
            'Registrar': 'Error',
            'Creation Date': 'Error',
            'Expiration Date': 'Error',
            'Name Servers': 'Error - ' + str(e)
        }

def save_to_csv(data):
    filename = f"whois_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Domain', 'Registrar', 'Creation Date', 'Expiration Date', 'Name Servers']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
    print(f"✅ Saved WHOIS info to: {filename}")

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., google.com): ")
    result = fetch_whois_info(domain)
    print("\nWHOIS Info:")
    for key, value in result.items():
        print(f"{key}: {value}")
    save_to_csv(result)
