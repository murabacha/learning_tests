input_file = "C:/Users/PC/Downloads/list.txt"   # your list of domains
output_file = "C:/Users/PC/Downloads/hosts_append.txt"

with open(input_file, "r") as f:
    domains = [line.strip() for line in f if line.strip()]

with open(output_file, "w") as f:
    for domain in domains:
        f.write(f"127.0.0.1 {domain}\n")
        print(f'wrote {domain}')
        #f.write(f"127.0.0.1 www.{domain}\n")  # cover www subdomains too
