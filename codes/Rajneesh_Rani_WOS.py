import pandas as pd
import json

json_data = {
    "QueryResult": {
        "RecordsSearched": 0,
        "RecordsFound": 1,
        "RecordsAvailable": 1,
        "Warnings": []
    },
    "Data": {
        "Records": [
            {
                "author_name": "Rani, Rajneesh",
                "publication_summary": {
                    "nonIndexedPublications": 1,
                    "totalPublications": 40,
                    "pprnPublications": 1,
                    "wosccPublications": 38,
                    "pqdtPublications": 0,
                    "indexedPublications": 39
                },
                "fullJournalsList": [
                    {"count": "3", "value": "2018 FIRST INTERNATIONAL CONFERENCE ON SECURE CYBER COMPUTING AND COMMUNICATIONS (ICSCCC 2018)"},
                    {"count": "2", "value": "INTERNATIONAL JOURNAL OF AGRICULTURAL AND ENVIRONMENTAL INFORMATION SYSTEMS"},
                    {"count": "2", "value": "ACM TRANSACTIONS ON ASIAN AND LOW-RESOURCE LANGUAGE INFORMATION PROCESSING"},
                    {"count": "2", "value": "MULTIMEDIA TOOLS AND APPLICATIONS"},
                    {"count": "2", "value": "2016 INTERNATIONAL CONFERENCE ON ADVANCES IN COMPUTING, COMMUNICATIONS AND INFORMATICS (ICACCI)"},
                    {"count": "2", "value": "INTERNATIONAL JOURNAL OF IMAGE AND GRAPHICS"},
                    {"count": "1", "value": "SADHANA-ACADEMY PROCEEDINGS IN ENGINEERING SCIENCES"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF MULTIMEDIA INFORMATION RETRIEVAL"},
                    {"count": "1", "value": "MULTIDIMENSIONAL SYSTEMS AND SIGNAL PROCESSING"},
                    {"count": "1", "value": "SECURITY AND PRIVACY"},
                    {"count": "1", "value": "VISUAL COMPUTER"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF INTELLIGENT COMPUTING AND CYBERNETICS"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL ON DOCUMENT ANALYSIS AND RECOGNITION"},
                    {"count": "1", "value": "ARABIAN JOURNAL FOR SCIENCE AND ENGINEERING"},
                    {"count": "1", "value": "PERTANIKA JOURNAL OF SCIENCE AND TECHNOLOGY"},
                    {"count": "1", "value": "2015 INTERNATIONAL CONFERENCE ON COMPUTING, COMMUNICATION & AUTOMATION (ICCCA)"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF INTELLIGENT INFORMATION TECHNOLOGIES"},
                    {"count": "1", "value": "ARTIFICIAL INTELLIGENCE REVIEW"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF SYSTEM ASSURANCE ENGINEERING AND MANAGEMENT"},
                    {"count": "1", "value": "ARCHIVES OF COMPUTATIONAL METHODS IN ENGINEERING"},
                    {"count": "1", "value": "CYBERNETICS AND INFORMATION TECHNOLOGIES"},
                    {"count": "1", "value": "COMMUNICATIONS IN COMPUTER AND INFORMATION SCIENCE"},
                    {"count": "1", "value": "2013 12TH INTERNATIONAL CONFERENCE ON DOCUMENT ANALYSIS AND RECOGNITION (ICDAR)"},
                    {"count": "1", "value": "PROCEEDINGS OF THE INTERNATIONAL CONFERENCE ON DOCUMENT ANALYSIS AND RECOGNITION"},
                    {"count": "1", "value": "PATTERN ANALYSIS AND APPLICATIONS"},
                    {"count": "1", "value": "LECTURE NOTES IN ENGINEERING AND COMPUTER SCIENCE"},
                    {"count": "1", "value": "IET IMAGE PROCESSING"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF SOFTWARE INNOVATION"},
                    {"count": "1", "value": "INFORMATION SYSTEMS FOR INDIAN LANGUAGES"},
                    {"count": "1", "value": "WORLD CONGRESS ON ENGINEERING AND COMPUTER SCIENCE, WCECS 2012, VOL I"},
                    {"count": "1", "value": "2016 IEEE INTERNATIONAL CONFERENCE ON COMPUTING, COMMUNICATION AND AUTOMATION (ICCCA)"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF COMPUTER APPLICATIONS IN TECHNOLOGY"},
                    {"count": "1", "value": "ARXIV"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF IMAGING SYSTEMS AND TECHNOLOGY"},
                    {"count": "1", "value": "INTERNATIONAL JOURNAL OF BIOMEDICAL ENGINEERING AND TECHNOLOGY"}
                ],
                "authorAliasName": "Rani, Rajneesh",
                "affiliations": [
                    {"value": "National Institute of Technology (NIT System)", "count": 13, "maxYear": 2024, "minYear": 2013},
                    {"value": "Dr B R Ambedkar National Institute of Technology Jalandhar", "count": 25, "maxYear": 2023, "minYear": 2011}
                ],
                "primaryAffiliationLocation": "JALANDHAR, PUNJAB, INDIA",
                "rid": "Y-2242-2019",
                "institution": "National Institute of Technology (NIT System)",
                "photoUrlLarge": "https://publons.com/media/initialcon/RR200.png",
                "publonsBasicMetricsData": {
                    "publonsProfileData": {
                        "institutions": [
                            {"institution": "Dr B R Ambedkar National Institute of Technology Jalandhar", "department": "Computer Science and Engineering", "role": "Assistant Professor", "startDate": "2007", "endDate": "present", "url": "/wos-op/institution/352999/"}
                        ],
                        "researchFields": [],
                        "awards": [],
                        "institutionsUrl": "/wos-op/dashboard/settings/affiliations/",
                        "researchFieldsUrl": "/wos-op/dashboard/settings/profile/"
                    },
                    "publonsIndividualStatsData": {
                        "ready": True,
                        "citationsPerYear": {"2024": "41", "2023": "65", "2022": "48", "2021": "34", "2020": "7", "2019": "2", "2018": "7", "2017": "5", "2016": "0", "2015": "2", "2014": "1"},
                        "averagePerItem": 5.58,
                        "averagePerYear": 19.27,
                        "hIndex": 8.0,
                        "timesCited": 212,
                        "dedupedTimesCited": 184,
                        "numPublicationsInWosCc": 38,
                        "timesCitedInDiidw": 1,
                        "dedupedTimesCitedInDiidw": 1,
                        "numPqdtPublications": 0
                    }
                },
                "showPublishedNames": True,
                "categories": [
                    "Computer Science", "Engineering", "Telecommunications", "Imaging Science & Photographic Technology", "Science & Technology - Other Topics", "Optics", "Mathematics", "Automation & Control Systems"
                ],
                "alternativeName": [{"value": "Rani, Rajneesh", "count": 38}],
                "academy": {"isAcademyGraduate": None, "isAcademySupervisor": None},
                "diidw_stats": {
                    "total_times_cited": 1,
                    "total_citing_articles_without_self_citations": 1,
                    "h_index": 0,
                    "total_citing_articles": 1,
                    "total_articles": 38,
                    "total_times_cited_without_self_citations": 1
                },
                "claim_status": True,
                "showOrganizationNames": True,
                "orcid": "0000-0003-2104-227X",
                "publishingName": "Rajneesh Rani",
                "authorId": "1856047",
                "primaryAffiliation": "National Institute of Technology (NIT System)",
                "primaryInstitutionAffiliation": {
                    "institution": "Dr B R Ambedkar National Institute of Technology Jalandhar",
                    "department": "Computer Science and Engineering",
                    "role": "Assistant Professor",
                    "startDate": "2007",
                    "endDate": "present",
                    "url": "/wos-op/institution/352999/"
                },
                "primaryAffiliationDepartment": ["Dept Comp Sci & Engn"],
                "excellentReviews": {"excellentReviewsCount": 0, "isExcellentReviewer": False},
                "wos_stats": {
                    "total_times_cited": 212,
                    "total_citing_articles_without_self_citations": 173,
                    "h_index": 8,
                    "total_citing_articles": 184,
                    "total_articles": 38,
                    "total_times_cited_without_self_citations": 195
                }
            }
        ]
    }
}


record = json_data["Data"]["Records"][0]

general_info = {
    "Author Name": record["author_name"],
    "Primary Affiliation Location": record["primaryAffiliationLocation"],
    "Institution": record["institution"],
    "Photo URL": record["photoUrlLarge"],
    "ORCID": record["orcid"],
    "Publishing Name": record["publishingName"],
    "Author ID": record["authorId"],
    "Claim Status": record["claim_status"]
}
general_df = pd.DataFrame([general_info])


pub_summary = {
    "Non-Indexed Publications": record["publication_summary"]["nonIndexedPublications"],
    "Total Publications": record["publication_summary"]["totalPublications"],
    "PPRN Publications": record["publication_summary"]["pprnPublications"],
    "WoS CC Publications": record["publication_summary"]["wosccPublications"],
    "PQDT Publications": record["publication_summary"]["pqdtPublications"],
    "Indexed Publications": record["publication_summary"]["indexedPublications"]
}
pub_summary_df = pd.DataFrame([pub_summary])

journals_df = pd.DataFrame(record["fullJournalsList"])


affiliations_df = pd.DataFrame(record["affiliations"])


pub_metrics = {
    "Average Citations Per Item": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["averagePerItem"],
    "Average Citations Per Year": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["averagePerYear"],
    "hIndex": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["hIndex"],
    "Times Cited": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["timesCited"],
    "Deduped Times Cited": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["dedupedTimesCited"],
    "Num Publications in WoS CC": record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["numPublicationsInWosCc"]
}
pub_metrics_df = pd.DataFrame([pub_metrics])


citations_per_year_df = pd.DataFrame(list(record["publonsBasicMetricsData"]["publonsIndividualStatsData"]["citationsPerYear"].items()), columns=['Year', 'Citations'])


with pd.ExcelWriter('Rajneesh_Rani_web_of_sciences_2.xlsx', engine='openpyxl') as writer:
    general_df.to_excel(writer, sheet_name='General Info', index=False)
    pub_summary_df.to_excel(writer, sheet_name='Publication Summary', index=False)
    journals_df.to_excel(writer, sheet_name='Journals List', index=False)
    affiliations_df.to_excel(writer, sheet_name='Affiliations', index=False)
    pub_metrics_df.to_excel(writer, sheet_name='Publishing Metrics', index=False)
    citations_per_year_df.to_excel(writer, sheet_name='Citations Per Year', index=False)
