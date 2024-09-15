import json
import pandas as pd
from collections import Counter

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['Data']['Records'][0]

def create_citations_sheet(author_data, writer):
    citations_per_year = author_data['publonsBasicMetricsData']['publonsIndividualStatsData']['citationsPerYear']
    df = pd.DataFrame(list(citations_per_year.items()), columns=['Year', 'Citations'])
    df['Year'] = pd.to_numeric(df['Year'])
    df['Citations'] = pd.to_numeric(df['Citations'])
    df = df[df['Year'] >= 2000]  # Filter for years 2000 and later
    df = df.sort_values('Year')
    
    # Calculate cumulative citations
    df['Cumulative Citations'] = df['Citations'].cumsum()
    
    df.to_excel(writer, sheet_name='amrit_lal_sangal_Citations', index=False)

def create_journals_sheet(author_data, writer):
    journals = author_data['fullJournalsList']
    df = pd.DataFrame(journals)
    df['count'] = pd.to_numeric(df['count'])
    df = df.sort_values('count', ascending=False)
    df.columns = ['Publications', 'Journal']
    df = df[['Journal', 'Publications']]
    df.to_excel(writer, sheet_name='Journals', index=False)

def create_category_sheet(author_data, writer):
    categories = author_data['categories']
    category_counts = Counter(categories)
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Publications'])
    df = df.sort_values('Publications', ascending=False)
    df.to_excel(writer, sheet_name='amrit_lal_sangal_Categories', index=False)

def create_affiliations_sheet(author_data, writer):
    affiliations = author_data['affiliations']
    df = pd.DataFrame(affiliations)
    df['count'] = pd.to_numeric(df['count'])
    df['minYear'] = pd.to_numeric(df['minYear'])
    df['maxYear'] = pd.to_numeric(df['maxYear'])
    df = df.sort_values('count', ascending=False)
    df.columns = ['Affiliation', 'Publications', 'Max Year', 'Min Year']
    df = df[['Affiliation', 'Publications', 'Min Year', 'Max Year']]
    df.to_excel(writer, sheet_name='amrit_lal_sangal_Affiliations', index=False)

def create_summary_sheet(author_data, writer):
    summary_data = {
        'Metric': [
            'Total Publications',
            'Total Citations',
            'H-index',
            'Average Citations per Item',
            'Average Citations per Year'
        ],
        'Value': [
            author_data['publication_summary']['totalPublications'],
            author_data['wos_stats']['total_times_cited'],
            author_data['wos_stats']['h_index'],
            author_data['publonsBasicMetricsData']['publonsIndividualStatsData']['averagePerItem'],
            author_data['publonsBasicMetricsData']['publonsIndividualStatsData']['averagePerYear']
        ]
    }
    df = pd.DataFrame(summary_data)
    df.to_excel(writer, sheet_name='amrit_lal_sangal_Summary', index=False)

def main():
    file_path = 'amrit_lal_sangal.json'  # Replace with the actual path to your JSON file
    output_file = 'amrit_lal_sangal2.xlsx'
    
    author_data = load_data(file_path)
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        create_summary_sheet(author_data, writer)
        create_citations_sheet(author_data, writer)
        create_journals_sheet(author_data, writer)
        create_category_sheet(author_data, writer)
        create_affiliations_sheet(author_data, writer)
    
    print(f"Excel file '{output_file}' has been generated with author metrics suitable for visualization.")

if __name__ == "__main__":
    main()
