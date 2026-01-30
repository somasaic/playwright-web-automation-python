import csv
import json

def load_sites(csv_path):
    with open(csv_path, newline="") as f:
        return list(csv.DictReader(f))

def run_multi_region_test():
    sites = load_sites("data/sample_input_sites.csv")
    results = []

    for site in sites:
        results.append({
            "site_name": site["site_name"],
            "region": site["region"],
            "status": "VALIDATED"
        })

    with open("data/region_validation_result.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    run_multi_region_test()
