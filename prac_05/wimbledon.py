DATA_FILE = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Read the data file and print information about Wimbledon champions and countries."""
    records = fetch_records(DATA_FILE)
    champion_counts, participating_countries = analyze_records(records)
    present_results(champion_counts, participating_countries)

def analyze_records(records):
    """Generate a dictionary of champions and a set of countries from the provided records (a list of lists)."""
    champion_counts = {}
    countries_set = set()

    for record in records:
        countries_set.add(record[COUNTRY_INDEX])
        try:
            champion_counts[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_counts[record[CHAMPION_INDEX]] = 1

    return champion_counts, countries_set

def present_results(champion_counts, countries_set):
    """Display information about champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_counts.items():
        print(name, count)
    print(f"\nThese {len(countries_set)} countries have achieved victory at Wimbledon: ")
    print(", ".join(country for country in sorted(countries_set)))

def fetch_records(file_name):
    """Retrieve records from the file and represent them as a list of lists."""
    records_list = []

    with open(file_name, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()  # Exclude the header
        for line in input_file:
            parts = line.strip().split(",")
            records_list.append(parts)

    return records_list

main()
