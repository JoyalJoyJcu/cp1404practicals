FILENAME = 'wimbledon.csv'


def main():
    """Main function to execute the program,
    it loads the data from the csv file then process the data to
    count the wins for each champion,
    then prints the champions country and total win count"""

    data = load_file(FILENAME)
    champion_wins, champion_countries = process_data(data)
    display_results(champion_countries, champion_wins)


def display_results(champion_countries, champion_wins):
    """display all processed results"""

    print("Wimbledon Champions: ")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
    print(",".join(sorted(champion_countries)))


def process_data(data):
    """process the data to count the champions wins"""

    champion_wins = {}
    champion_countries = set()
    for entry in data:
        champion_country = entry[1]
        champion = entry[2]
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
        champion_countries.add(champion_country)
    return champion_wins, champion_countries


def load_file(filename):
    """loads the data from the file and returns it into a lists of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = []
        for line in in_file:
            line = line.strip().split(',')
            data.append(line)
    return data


main()
