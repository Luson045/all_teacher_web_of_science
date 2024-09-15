import json
import matplotlib.pyplot as plt
from collections import Counter

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['Data']['Records'][0]

def plot_publications_over_time(author_data):
    citations_per_year = author_data['publonsBasicMetricsData']['publonsIndividualStatsData']['citationsPerYear']
    years = [int(year) for year in citations_per_year.keys() if int(year) >= 2000]
    citations = [int(citations_per_year[str(year)]) for year in years if int(year) >= 2000]
    print(citations_per_year)
    plt.figure(figsize=(12, 6))
    plt.bar(years, citations)
    plt.title(f"Citations per Year for {author_data['publishingName']}")
    plt.xlabel("Year")
    plt.ylabel("Number of Citations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.savefig("citations_per_year.png")
    plt.close()

def plot_top_journals(author_data):
    journals = author_data['fullJournalsList']
    journal_counts = Counter({journal['value']: int(journal['count']) for journal in journals})
    top_journals = dict(journal_counts.most_common(10))

    plt.figure(figsize=(12, 6))
    plt.bar(top_journals.keys(), top_journals.values())
    plt.title(f"Top 10 Journals for {author_data['publishingName']}")
    plt.xlabel("Journal")
    plt.ylabel("Number of Publications")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    plt.savefig("top_journals.png")
    plt.close()

def plot_category_distribution(author_data):
    categories = author_data['categories']
    category_counts = Counter(categories)

    plt.figure(figsize=(10, 10))
    plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
    plt.title(f"Research Category Distribution for {author_data['publishingName']}")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    plt.savefig("category_distribution.png")
    plt.close()

def main():
    file_path = 'amrit_lal_sangal.json'  # Replace with the actual path to your JSON file
    author_data = load_data('amrit_lal_sangal.json')

    plot_publications_over_time(author_data)
    plot_top_journals(author_data)
    plot_category_distribution(author_data)

    print("Visualizations have been generated and saved as PNG files.")

if __name__ == "__main__":
    main()
