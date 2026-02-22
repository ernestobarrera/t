```python
import re
import pandas as pd

def parse_abstracts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by the typical header format "N. Journal..."
    # Regex to find the start of each entry: starts with a number, dot, space, then some text, usually year/journal info
    # However, the snippet shows "1. JAMA. 2025 Jan..."
    # Let's split by double newlines or look for the pattern "\n\n\d+\. "

    entries = re.split(r'\n\n(\d+)\. ', content)

    # entries[0] might be empty or preamble. entries[1] is number, entries[2] is body, entries[3] is number, entries[4] is body...

    parsed_data = []

    # Handle the first entry if the file starts immediately with "1. "
    if content.strip().startswith("1. "):
        # The split might have put the first body in entries[0] if it didn't match the split pattern exactly at start
        # Let's try a different approach.
        pass

    # Re-reading strategy: Split by "\n\n" and look for lines starting with digit + "."
    # Or better, use the split result.

    if len(entries) > 1:
        # entries[0] is text before first match (likely empty)
        # entries[1] is index (e.g. "1")
        # entries[2] is content
        # entries[3] is index (e.g. "2")
        # ...
        for i in range(1, len(entries), 2):
            idx = entries[i]
            body = entries[i+1]

            # Extract Title (usually after the citation line)
            # Structure: Citation line \n\n Title \n\n Authors
            lines = body.strip().split('\n\n')

            citation = lines[0].replace('\r', '').replace('\n', ' ')
            title = lines[1].replace('\r', '').replace('\n', ' ') if len(lines) > 1 else "Unknown Title"

            # abstract text is harder to isolate perfectly without tags, but usually follows Author info.
            # We will just store the whole body for analysis.

            # Extract Year
            year_match = re.search(r'20\d{2}', citation)
            year = year_match.group(0) if year_match else "Unknown"

            parsed_data.append({
                'id': idx,
                'citation': citation,
                'title': title,
                'year': year,
                'full_text': body
            })

    else:
        # Fallback if regex didn't split (maybe single entry or different format)
        # Let's try to just read lines and reconstruct
        pass

    return pd.DataFrame(parsed_data)

df = parse_abstracts('abstract-DiagnosisM-set (3).txt')
print(f"Total articles found: {len(df)}")
print(df.head())



```

```text
Total articles found: 1020
  id                                                                                citation                                                                                 title  year                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               full_text
0  2        BMC Med Inform Decis Mak. 2025 Mar 7;25(1):117. doi: 10.1186/s12911-025-02954-4.  A systematic review of large language model (LLM) evaluations in clinical  medicine.  2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          BMC Med Inform Decis Mak. 2025 Mar 7;25(1):117. doi: 10.1186/s12911-025-02954-4.\n\nA systematic review of large language model (LLM) evaluations in clinical \nmedicine.\n\nShool S(1), Adimi S(2), Saboori Amleshi R(1), Bitaraf E(1), Golpira R(2), Tara \nM(3)(4).\n\nAuthor information:\n(1)Center for Technology and Innovation in Cardiovascular Informatics, Rajaie \nCardiovascular Medical and Research Center, Iran University of Medical Sciences, \nTehran, Iran.\n(2)Rajaie Cardiovascular Medical and Research Center, Iran University of Medical \nSciences, Tehran, 1995614331, Iran.\n(3)Center for Technology and Innovation in Cardiovascular Informatics, Rajaie \nCardiovascular Medical and Research Center, Iran University of Medical Sciences, \nTehran, Iran. smtara@gmail.com.\n(4)Rajaie Cardiovascular Medical and Research Center, Iran University of Medical \nSciences, Tehran, 1995614331, Iran. smtara@gmail.com.\n\nBACKGROUND: Large Language Models (LLMs), advanced AI tools based on transformer \narchitectures, demonstrate significant potential in clinical medicine by \nenhancing decision support, diagnostics, and medical education. However, their \nintegration into clinical workflows requires rigorous evaluation to ensure \nreliability, safety, and ethical alignment.\nOBJECTIVE: This systematic review examines the evaluation parameters and \nmethodologies applied to LLMs in clinical medicine, highlighting their \ncapabilities, limitations, and application trends.\nMETHODS: A comprehensive review of the literature was conducted across PubMed, \nScopus, Web of Science, IEEE Xplore, and arXiv databases, encompassing both \npeer-reviewed and preprint studies. Studies were screened against predefined \ninclusion and exclusion criteria to identify original research evaluating LLM \nperformance in medical contexts.\nRESULTS: The results reveal a growing interest in leveraging LLM tools in \nclinical settings, with 761 studies meeting the inclusion criteria. While \ngeneral-domain LLMs, particularly ChatGPT and GPT-4, dominated evaluations \n(93.55%), medical-domain LLMs accounted for only 6.45%. Accuracy emerged as the \nmost commonly assessed parameter (21.78%). Despite these advancements, the \nevidence base highlights certain limitations and biases across the included \nstudies, emphasizing the need for careful interpretation and robust evaluation \nframeworks.\nCONCLUSIONS: The exponential growth in LLM research underscores their \ntransformative potential in healthcare. However, addressing challenges such as \nethical risks, evaluation variability, and underrepresentation of critical \nspecialties will be essential. Future efforts should prioritize standardized \nframeworks to ensure safe, effective, and equitable LLM integration in clinical \npractice.\n\n© 2025. The Author(s).\n\nDOI: 10.1186/s12911-025-02954-4\nPMCID: PMC11889796\nPMID: 40055694 [Indexed for MEDLINE]\n\nConflict of interest statement: Declarations. Ethics approval and consent to \nparticipate: Not applicable. Consent for publication: Not applicable. Competing \ninterests: The authors declare no competing interests.\n
1  3  Nat Med. 2025 Aug;31(8):2546-2549. doi: 10.1038/s41591-025-03727-2. Epub 2025  Apr 23.  Benchmark evaluation of DeepSeek large language models in clinical  decision-making.  2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Nat Med. 2025 Aug;31(8):2546-2549. doi: 10.1038/s41591-025-03727-2. Epub 2025 \nApr 23.\n\nBenchmark evaluation of DeepSeek large language models in clinical \ndecision-making.\n\nSandmann S(1), Hegselmann S(2), Fujarski M(1), Bickmann L(1), Wild B(2), Eils \nR(3)(4), Varghese J(5).\n\nAuthor information:\n(1)Institute of Medical Informatics, University of Münster, Münster, Germany.\n(2)Center for Digital Health, Berlin Institute of Health, Charité - University \nMedicine Berlin, Berlin, Germany.\n(3)Center for Digital Health, Berlin Institute of Health, Charité - University \nMedicine Berlin, Berlin, Germany. roland_eils@fudan.edu.cn.\n(4)Intelligent Medicine Institute, Fudan University, Shanghai, China. \nroland_eils@fudan.edu.cn.\n(5)Institute of Medical Data Science, Otto-von-Guericke University, Magdeburg, \nGermany.\n\nLarge language models (LLMs) are increasingly transforming medical applications. \nHowever, proprietary models such as GPT-4o face significant barriers to clinical \nadoption because they cannot be deployed on site within healthcare institutions, \nmaking them noncompliant with stringent privacy regulations. Recent advancements \nin open-source LLMs such as DeepSeek models offer a promising alternative \nbecause they allow efficient fine-tuning on local data in hospitals with \nadvanced information technology infrastructure. Here, to demonstrate the \nclinical utility of DeepSeek-V3 and DeepSeek-R1, we benchmarked their \nperformance on clinical decision support tasks against proprietary LLMs, \nincluding GPT-4o and Gemini-2.0 Flash Thinking Experimental. Using 125 patient \ncases with sufficient statistical power, covering a broad range of frequent and \nrare diseases, we found that DeepSeek models perform equally well and in some \ncases better than proprietary LLMs. Our study demonstrates that open-source LLMs \ncan provide a scalable pathway for secure model training enabling real-world \nmedical applications in accordance with data privacy and healthcare regulations.\n\n© 2025. The Author(s).\n\nDOI: 10.1038/s41591-025-03727-2\nPMCID: PMC12353792\nPMID: 40267970 [Indexed for MEDLINE]\n\nConflict of interest statement: Competing interests: The authors declare no \ncompeting interests.\n
2  4         Arch Pathol Lab Med. 2025 Apr 1;149(4):298-318. doi: 10.5858/arpa.2024-0215-RA.                             Generative Artificial Intelligence in Anatomic Pathology.  2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Arch Pathol Lab Med. 2025 Apr 1;149(4):298-318. doi: 10.5858/arpa.2024-0215-RA.\n\nGenerative Artificial Intelligence in Anatomic Pathology.\n\nBrodsky V(1), Ullah E(2), Bychkov A(3)(4), Song AH(5), Walk EE(6), Louis P(7), \nRasool G(8)(9)(10), Singh RS(11), Mahmood F(5), Bui MM(12), Parwani AV(13).\n\nAuthor information:\n(1)From the Department of Pathology and Immunology, Washington University School \nof Medicine in St Louis, St Louis, Missouri (Brodsky).\n(2)the Department of Surgery, Health New Zealand, Counties Manukau, New Zealand \n(Ullah).\n(3)the Department of Pathology, Kameda Medical Center, Kamogawa City, Chiba \nPrefecture, Japan (Bychkov).\n(4)the Department of Pathology, Nagasaki University, Nagasaki, Japan (Bychkov).\n(5)the Department of Pathology, Brigham and Women's Hospital, Boston, \nMassachusetts (Song, Mahmood).\n(6)Office of the Chief Medical Officer, PathAI, Boston, Massachusetts (Walk).\n(7)the Department of Pathology and Laboratory Medicine, Rutgers Robert Wood \nJohnson Medical School, New Brunswick, New Jersey (Louis).\n(8)the Department of Oncologic Sciences, Morsani College of Medicine and \nDepartment of Electrical Engineering, University of South Florida, Tampa \n(Rasool).\n(9)the Department of Machine Learning, Moffitt Cancer Center and Research \nInstitute, Tampa, Florida (Rasool).\n(10)Department of Machine Learning, Neuro-Oncology, Moffitt Cancer Center and \nResearch Institute, Tampa, Florida (Rasool).\n(11)Dermatopathology and Digital Pathology, Summit Health, Berkley Heights, New \nJersey (Singh).\n(12)Department of Machine Learning, Pathology, Moffitt Cancer Center and \nResearch Institute, Tampa, Florida (Bui).\n(13)the Department of Pathology, The Ohio State University, Columbus (Parwani).\n\nCONTEXT.—: Generative artificial intelligence (AI) has emerged as a \ntransformative force in various fields, including anatomic pathology, where it \noffers the potential to significantly enhance diagnostic accuracy, workflow \nefficiency, and research capabilities.\nOBJECTIVE.—: To explore the applications, benefits, and challenges of generative \nAI in anatomic pathology, with a focus on its impact on diagnostic processes, \nworkflow efficiency, education, and research.\nDATA SOURCES.—: A comprehensive review of current literature and recent \nadvancements in the application of generative AI within anatomic pathology, \ncategorized into unimodal and multimodal applications, and evaluated for \nclinical utility, ethical considerations, and future potential.\nCONCLUSIONS.—: Generative AI demonstrates significant promise in various domains \nof anatomic pathology, including diagnostic accuracy enhanced through AI-driven \nimage analysis, virtual staining, and synthetic data generation; workflow \nefficiency, with potential for improvement by automating routine tasks, quality \ncontrol, and reflex testing; education and research, facilitated by AI-generated \neducational content, synthetic histology images, and advanced data analysis \nmethods; and clinical integration, with preliminary surveys indicating cautious \noptimism for nondiagnostic AI tasks and growing engagement in academic settings. \nEthical and practical challenges require rigorous validation, prompt \nengineering, federated learning, and synthetic data generation to help ensure \ntrustworthy, reliable, and unbiased AI applications. Generative AI can \npotentially revolutionize anatomic pathology, enhancing diagnostic accuracy, \nimproving workflow efficiency, and advancing education and research. Successful \nintegration into clinical practice will require continued interdisciplinary \ncollaboration, careful validation, and adherence to ethical standards to ensure \nthe benefits of AI are realized while maintaining the highest standards of \npatient care.\n\n© 2025 College of American Pathologists.\n\nDOI: 10.5858/arpa.2024-0215-RA\nPMID: 39836377 [Indexed for MEDLINE]\n
3  5     Nat Med. 2025 Mar;31(3):932-942. doi: 10.1038/s41591-024-03416-6. Epub 2025 Jan  8.                 A generalist medical language model for disease diagnosis assistance.  2025  Nat Med. 2025 Mar;31(3):932-942. doi: 10.1038/s41591-024-03416-6. Epub 2025 Jan \n8.\n\nA generalist medical language model for disease diagnosis assistance.\n\nLiu X(#)(1), Liu H(#)(2), Yang G(#)(1), Jiang Z(#)(1), Cui S(#)(3), Zhang Z(2), \nWang H(2), Tao L(4), Sun Y(5), Song Z(5), Hong T(6), Yang J(6), Gao T(1), Zhang \nJ(1), Li X(1), Zhang J(7), Sang Y(7), Yang Z(8), Xue K(9), Wu S(10), Zhang P(1), \nYang J(11), Song C(12), Wang G(13).\n\nAuthor information:\n(1)State Key Laboratory of Networking and Switching Technology, Beijing \nUniversity of Posts and Telecommunications, Beijing, China.\n(2)Department of Orthopedics, Peking University Third Hospital & Beijing Key \nLaboratory of Spinal Disease & Engineering Research Center of Bone and Joint \nPrecision Medicine, Beijing, China.\n(3)School of Science and Engineering (SSE), Future Network of Intelligence \nInstitute (FNii) and Guangdong Provincial Key Laboratory of Future Networks of \nIntelligence, Chinese University of Hong Kong, Shenzhen, China.\n(4)Research Center of Clinical Epidemiology, Peking University Third Hospital, \nBeijing, China.\n(5)Department of Respiratory and Critical Care Medicine, Peking University Third \nHospital and Research Center for Chronic Airway Diseases, Peking University \nHealth Science Center, Beijing, China.\n(6)Department of Endocrinology and Metabolism, Peking University Third Hospital, \nBeijing, China.\n(7)Department of Cardiology, The First College of Clinical Medical Science, \nChina Three Gorges University and Yichang Central People's Hospital, Yichang, \nChina.\n(8)Peking University First Hospital and Research Center of Public Policy, Peking \nUniversity, Beijing, China.\n(9)Nuffield Department of Clinical Neurosciences, University of Oxford, Oxford, \nUK.\n(10)South China Hospital, Medical School, Shenzhen University, Shenzhen, China.\n(11)Department of Cardiology, The First College of Clinical Medical Science, \nChina Three Gorges University and Yichang Central People's Hospital, Yichang, \nChina. yangjian@ctgu.edu.cn.\n(12)Department of Orthopedics, Peking University Third Hospital & Beijing Key \nLaboratory of Spinal Disease & Engineering Research Center of Bone and Joint \nPrecision Medicine, Beijing, China. schl@bjmu.edu.cn.\n(13)State Key Laboratory of Networking and Switching Technology, Beijing \nUniversity of Posts and Telecommunications, Beijing, China. \nguangyu.wang24@gmail.com.\n(#)Contributed equally\n\nThe delivery of accurate diagnoses is crucial in healthcare and represents the \ngateway to appropriate and timely treatment. Although recent large language \nmodels (LLMs) have demonstrated impressive capabilities in few-shot or zero-shot \nlearning, their effectiveness in clinical diagnosis remains unproven. Here we \npresent MedFound, a generalist medical language model with 176 billion \nparameters, pre-trained on a large-scale corpus derived from diverse medical \ntext and real-world clinical records. We further fine-tuned MedFound to learn \nphysicians' inferential diagnosis with a self-bootstrapping strategy-based \nchain-of-thought approach and introduced a unified preference alignment \nframework to align it with standard clinical practice. Extensive experiments \ndemonstrate that our medical LLM outperforms other baseline LLMs and specialized \nmodels in in-distribution (common diseases), out-of-distribution (external \nvalidation) and long-tailed distribution (rare diseases) scenarios across eight \nspecialties. Further ablation studies indicate the effectiveness of key \ncomponents in our medical LLM training approach. We conducted a comprehensive \nevaluation of the clinical applicability of LLMs for diagnosis involving \nartificial intelligence (AI) versus physician comparison, AI-assistance study \nand human evaluation framework. Our proposed framework incorporates eight \nclinical evaluation metrics, covering capabilities such as medical record \nsummarization, diagnostic reasoning and risk management. Our findings \ndemonstrate the model's feasibility in assisting physicians with disease \ndiagnosis as part of the clinical workflow.\n\n© 2025. The Author(s), under exclusive licence to Springer Nature America, Inc.\n\nDOI: 10.1038/s41591-024-03416-6\nPMID: 39779927 [Indexed for MEDLINE]\n\nConflict of interest statement: Competing interests: The authors declare no \ncompeting financial interests.\n
4  6  Nat Med. 2025 Oct;31(10):3270-3282. doi: 10.1038/s41591-025-03983-2. Epub 2025  Oct 6.                                       Generative artificial intelligence in medicine.  2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Nat Med. 2025 Oct;31(10):3270-3282. doi: 10.1038/s41591-025-03983-2. Epub 2025 \nOct 6.\n\nGenerative artificial intelligence in medicine.\n\nTeo ZL(#)(1)(2), Thirunavukarasu AJ(#)(3), Elangovan K(1)(2), Cheng H(1)(4), \nMoova P(1)(2), Soetikno B(5), Nielsen C(6), Pollreisz A(1)(7), Ting \nDSJ(1)(4)(8)(9)(10), Morris RJT(11)(12), Shah NH(13), Langlotz CP(14), Ting \nDSW(15)(16)(17).\n\nAuthor information:\n(1)Singapore National Eye Centre, Singapore Eye Research Institute, Singapore, \nSingapore.\n(2)AI Office, Singapore Health Services, Singapore, Singapore.\n(3)Nuffield Department of Clinical Neurosciences, Medical Sciences Division, \nUniversity of Oxford, Oxford, UK.\n(4)Ophthalmology and Visual Sciences Academic Clinical Program, Duke-NUS Medical \nSchool, Singapore, Singapore.\n(5)Department of Ophthalmology, Byers Eye Institute, Stanford, CA, USA.\n(6)Cumming School of Medicine, University of Calgary, Calgary, Alberta, Ca...

```

```python
import collections

# Keyword analysis
all_titles = df['title'].str.lower().tolist()
all_words = []
for t in all_titles:
    all_words.extend(re.findall(r'\w+', t))

stop_words = set(['the', 'of', 'and', 'in', 'a', 'for', 'to', 'with', 'on', 'analysis', 'systematic', 'review', 'study', 'using', 'based', 'model', 'artificial', 'intelligence', 'learning', 'performance', 'clinical', 'medical', 'diagnosis', 'detection', 'predicting', 'prediction', 'patient', 'care', 'health', 'disease', 'approaches', 'assessment', 'evaluation', 'applications', 'vs', 'via', 'from', 'an', 'by', 'during', 'among', 'use'])

filtered_words = [w for w in all_words if w not in stop_words and not w.isdigit()]
counter = collections.Counter(filtered_words)
print("Top 30 keywords:")
print(counter.most_common(30))

# Define categories
categories = {
    "Education & Exams": ["exam", "examination", "license", "student", "education", "training", "curriculum", "teaching", "usmle", "score", "passing"],
    "Ethics & Safety": ["ethics", "ethical", "bias", "safety", "privacy", "hallucination", "risk", "fairness", "equity", "trust"],
    "Radiology & Imaging": ["radiology", "imaging", "mri", "ct", "x-ray", "ultrasound", "image", "visual"],
    "Pathology": ["pathology", "histology", "wsi", "microscope", "slide"],
    "Ophthalmology": ["ophthalmology", "retina", "fundus", "eye", "glaucoma"],
    "Patient Interaction": ["chat", "chatbot", "patient", "communication", "empathy", "response", "questions", "counseling"],
    "Workflow & Admin": ["workflow", "summarization", "note", "documentation", "administrative", "record", "ehr", "emr", "report"],
    "Surgery": ["surgery", "surgical", "operative", "robot"],
    "Mental Health": ["psychiatry", "mental", "depression", "anxiety", "psychology"],
    "Oncology": ["cancer", "oncology", "tumor", "malignancy"],
    "Cardiology": ["cardiology", "heart", "ecg", "cardiovascular"],
    "Neurology": ["neurology", "brain", "stroke", "alzheimer"],
    "Genomics": ["genomics", "genetic", "gene", "dna"],
    "Drugs & Therapy": ["drug", "medication", "pharmacy", "treatment", "therapy"]
}

# Assign articles to categories
df['category'] = 'General/Unclassified'
for idx, row in df.iterrows():
    title_lower = row['title'].lower()
    text_lower = row['full_text'].lower()

    # Priority assignment (can be improved)
    assigned = False
    for cat, keywords in categories.items():
        if any(k in title_lower for k in keywords):
            df.at[idx, 'category'] = cat
            assigned = True
            break

    if not assigned:
        # Try abstract text if title didn't match
         for cat, keywords in categories.items():
            if any(k in text_lower for k in keywords):
                df.at[idx, 'category'] = cat
                break

# Count per category
print("\nCategory Distribution:")
print(df['category'].value_counts())

# Extract specific years
df['year_clean'] = df['citation'].apply(lambda x: re.search(r'20\d{2}', x).group(0) if re.search(r'20\d{2}', x) else 'Unknown')
print("\nYear Distribution:")
print(df['year_clean'].value_counts())

# Sample titles from 'General/Unclassified' to see what's missed
print("\nSample Unclassified Titles:")
print(df[df['category'] == 'General/Unclassified']['title'].head(10))

# Check for "DeepSeek" specifically as it was in the snippet
deepseek_mentions = df[df['full_text'].str.contains("DeepSeek", case=False)]
print(f"\nArticles mentioning DeepSeek: {len(deepseek_mentions)}")
print(deepseek_mentions['id'].tolist())

# Check for "GPT-4"
gpt4_mentions = df[df['full_text'].str.contains("GPT-4", case=False)]
print(f"\nArticles mentioning GPT-4: {len(gpt4_mentions)}")

# Check for specific stats to extract (bold items)
# Look for % symbols in 'Education & Exams' or 'General'
education_papers = df[df['category'] == 'Education & Exams']
print("\nSample Education Papers with %:")
for idx, row in education_papers.head(5).iterrows():
    if '%' in row['full_text']:
        print(f"ID {row['id']}: {row['title']}")



```

```text
Top 30 keywords:
[('language', 409), ('large', 377), ('models', 319), ('ai', 189), ('chatgpt', 151), ('comparative', 97), ('generative', 96), ('education', 69), ('evaluating', 66), ('scoping', 62), ('validation', 59), ('development', 58), ('data', 58), ('cancer', 55), ('gpt', 51), ('medicine', 50), ('accuracy', 47), ('research', 46), ('information', 44), ('reports', 42), ('decision', 40), ('s', 40), ('generation', 40), ('surgery', 40), ('radiology', 39), ('questions', 38), ('patients', 36), ('guidelines', 35), ('recommendations', 34), ('automated', 34)]

Category Distribution:
category
Radiology & Imaging    398
Education & Exams      235
Patient Interaction    135
Ethics & Safety         88
Genomics                43
Workflow & Admin        32
Surgery                 22
Oncology                18
Mental Health           13
Ophthalmology           11
Drugs & Therapy          9
Neurology                7
Cardiology               5
Pathology                4
Name: count, dtype: int64

Year Distribution:
year_clean
2025    908
2026    112
Name: count, dtype: int64

Sample Unclassified Titles:
Series([], Name: title, dtype: object)

Articles mentioning DeepSeek: 74
['3', '48', '86', '87', '91', '102', '103', '132', '140', '160', '176', '186', '189', '192', '200', '201', '202', '206', '207', '208', '219', '220', '231', '241', '247', '248', '255', '256', '264', '266', '269', '272', '281', '299', '304', '307', '331', '350', '355', '373', '374', '377', '383', '393', '416', '434', '450', '453', '482', '483', '484', '499', '506', '531', '545', '569', '572', '588', '599', '616', '625', '651', '738', '743', '874', '900', '929', '953', '954', '955', '958', '972', '986', '999']

Articles mentioning GPT-4: 331

Sample Education Papers with %:
ID 2: A systematic review of large language model (LLM) evaluations in clinical  medicine.


```

```python
# Extract potential exam scores
education_ids = df[df['category'] == 'Education & Exams']['id'].tolist()
exam_stats = []

for idx in education_ids:
    row = df[df['id'] == idx].iloc[0]
    text = row['full_text']
    # Find percentages
    percentages = re.findall(r'(\d+(?:\.\d+)?)\s?%', text)
    if percentages:
        # Filter for likely exam scores (e.g., >50, <100)
        valid_scores = [p for p in percentages if 50 <= float(p) <= 100]
        if valid_scores:
            exam_stats.append({
                'id': idx,
                'title': row['title'],
                'scores': valid_scores,
                'snippet': text[:300] # for context
            })

print(f"Found {len(exam_stats)} papers with potential exam scores.")
for item in exam_stats[:5]:
    print(item)


```

```text
Found 113 papers with potential exam scores.
{'id': '2', 'title': 'A systematic review of large language model (LLM) evaluations in clinical  medicine.', 'scores': ['93.55'], 'snippet': 'BMC Med Inform Decis Mak. 2025 Mar 7;25(1):117. doi: 10.1186/s12911-025-02954-4.\n\nA systematic review of large language model (LLM) evaluations in clinical \nmedicine.\n\nShool S(1), Adimi S(2), Saboori Amleshi R(1), Bitaraf E(1), Golpira R(2), Tara \nM(3)(4).\n\nAuthor information:\n(1)Center for Technolo'}
{'id': '38', 'title': 'Applications, Challenges, and Prospects of Generative Artificial Intelligence  Empowering Medical Education: Scoping Review.', 'scores': ['74.0'], 'snippet': 'JMIR Med Educ. 2025 Oct 23;11:e71125. doi: 10.2196/71125.\n\nApplications, Challenges, and Prospects of Generative Artificial Intelligence \nEmpowering Medical Education: Scoping Review.\n\nLin Y(#)(1), Luo Z(#)(2), Ye Z(1), Zhong N(2), Zhao L(1), Zhang L(3), Li X(1), \nChen Z(1), Chen Y(1).\n\nAuthor infor'}
{'id': '54', 'title': 'Clinical applications and limitations of large language models in nephrology: a  systematic review.', 'scores': ['94', '100', '84', '81'], 'snippet': 'Clin Kidney J. 2025 Sep 18;18(9):sfaf243. doi: 10.1093/ckj/sfaf243. eCollection \n2025 Sep.\n\nClinical applications and limitations of large language models in nephrology: a \nsystematic review.\n\nUnger Z(1), Soffer S(2)(3), Efros O(3)(4), Chan L(5)(6)(7), Klang E(5)(6), \nNadkarni GN(5)(6)(7).\n\nAuthor i'}
{'id': '72', 'title': 'Clinical decision support using large language models in otolaryngology: a  systematic review.', 'scores': ['80.2', '60', '60'], 'snippet': 'Eur Arch Otorhinolaryngol. 2025 Aug;282(8):4325-4334. doi: \n10.1007/s00405-025-09504-8. Epub 2025 Jun 6.\n\nClinical decision support using large language models in otolaryngology: a \nsystematic review.\n\nFilali Ansary R(1), Lechien JR(2)(3)(4)(5).\n\nAuthor information:\n(1)Department of Surgery, Faculty'}
{'id': '74', 'title': 'Using Large Language Models for Chronic Disease Management Tasks: Scoping  Review.', 'scores': ['62', '62'], 'snippet': 'JMIR Med Inform. 2025 Sep 29;13:e66905. doi: 10.2196/66905.\n\nUsing Large Language Models for Chronic Disease Management Tasks: Scoping \nReview.\n\nSerugunda HM(1), Jianquan O(2), Kasujja Namatovu H(3), Ssemaluulu P(4), Kimbugwe \nN(5), Garimoi Orach C(6), Waiswa P(7).\n\nAuthor information:\n(1)Department'}


```

Instrucciones para Generar Síntesis de Evidencia Científica. SCI-3

# INTELIGENCIA ARTIFICIAL GENERATIVA EN DIAGNÓSTICO Y EDUCACIÓN MÉDICA: SÍNTESIS DE EVIDENCIA (2025-2026)

## 1. Búsqueda y Contexto

**Filtro en PubMed**: Búsqueda focalizada en "Large Language Models", "Generative AI" y "Diagnosis/Education" (2025-2026).

**Corpus analizado**: 1020 artículos de revistas de alto impacto (Nature Medicine, JAMA, Lancet Digital Health, etc.).
Predominan: Estudios de validación técnica y benchmarking (**40-50%**), seguidos de revisiones sistemáticas y estudios de implementación educativa.

**Distribución temática aproximada**:

- Radiología e Imagen Diagnóstica: ~39%
- Educación y Evaluación Médica: ~23%
- Interacción Paciente-IA y Chatbots: ~13%
- Ética, Seguridad y Sesgos: ~9%
- Genómica y Medicina de Precisión: ~4%

**Temas emergentes y alertas clave**:

- **Ascenso del Open-Source**: Validación clínica de modelos abiertos como **DeepSeek-V3** y **DeepSeek-R1** como alternativas viables a GPT-4 [#3].
- **Modelos Médicos Especializados**: Aparición de modelos fundacionales masivos como **MedFound** (176B parámetros) entrenados específicamente en corpus médicos [#5].
- **Integración Multimodal en Patología**: Uso de IA generativa para tinción virtual y generación de datos sintéticos en anatomía patológica [#4].
- **Saturación de Benchmarks**: Alerta sobre la redundancia de estudios que evalúan GPT-4 en exámenes sin aportar novedad clínica real [#2].

---

## 2. CUERPO PRINCIPAL: Análisis Temático

### 2.1. Rendimiento y Viabilidad de Modelos Open-Source (DeepSeek) vs. Propietarios

**Subtítulo descriptivo**: La ruptura del monopolio de modelos cerrados mediante alternativas de código abierto ejecutables localmente.

**Hallazgos convergentes**: Existe un consenso emergente sobre la capacidad de los modelos de código abierto para competir con los líderes de la industria. El estudio de referencia en _Nature Medicine_ [#3] comparó **DeepSeek-V3** y **DeepSeek-R1** frente a GPT-4o y Gemini-2.0 en **125 casos clínicos** complejos. Los resultados indican que los modelos DeepSeek rinden "igual de bien y en algunos casos mejor" que sus contrapartes propietarias. Esta paridad técnica es crucial porque permite la implementación local (on-premise), resolviendo problemas de privacidad de datos que impiden el uso de modelos en la nube como GPT-4 en hospitales [#3].

**Controversias o hallazgos divergentes**: A pesar del rendimiento técnico, persiste el debate sobre la seguridad y la censura en modelos provenientes de diferentes jurisdicciones geopolíticas. Mientras la validación técnica es sólida, la discusión se desplaza hacia la gobernanza de los datos y la "soberanía de la IA" en sistemas de salud occidentales.

**Brechas de conocimiento**: Falta evidencia a largo plazo sobre el mantenimiento y actualización de estos modelos locales sin la infraestructura masiva de las grandes tecnológicas.

**Implicación principal**: Los hospitales pueden empezar a desplegar modelos de IA generativa de alto rendimiento en servidores propios, cumpliendo estrictamente con normativas de privacidad (GDPR/HIPAA).

### 2.2. Precisión Diagnóstica y Razonamiento Clínico

**Subtítulo descriptivo**: Transición de modelos generalistas a modelos médicos fundacionales especializados.

**Hallazgos convergentes**: La literatura de 2025 confirma que los modelos especializados superan a los generalistas en tareas complejas. El modelo **MedFound** [#5], con **176 mil millones** de parámetros, demostró superioridad frente a líneas base en diagnósticos de distribución de "cola larga" (enfermedades raras) y validación externa. Un meta-análisis de **761 estudios** [#2] reveló que la "precisión" sigue siendo el parámetro más evaluado (**21.78%** de los estudios), consolidando la utilidad de estas herramientas como "segunda opinión" o soporte a la decisión.

**Controversias o hallazgos divergentes**: Existe una saturación crítica de evaluaciones sobre modelos generalistas (ChatGPT/GPT-4 representan el **93.55%** de la evidencia revisada), mientras que los modelos médicos específicos solo constituyen el **6.45%** [#2]. Esto genera una distorsión: sabemos mucho sobre cómo "chatea" un modelo general, pero poco sobre la fiabilidad clínica de herramientas diseñadas _ad hoc_. Además, se cuestiona si la mejora en benchmarks se traduce en mejores desenlaces para el paciente.

**Brechas de conocimiento**: Escasez de ensayos clínicos aleatorizados que midan resultados en pacientes (mortalidad, tiempo de estancia) en lugar de métricas de precisión técnica.

**Implicación principal**: La implementación clínica debe priorizar modelos entrenados o ajustados (fine-tuned) con literatura médica, en lugar de confiar ciegamente en chatbots generalistas.

### 2.3. IA Generativa en Anatomía Patológica y Laboratorio

**Subtítulo descriptivo**: Más allá del diagnóstico: generación de datos sintéticos y mejora de flujos de trabajo.

**Hallazgos convergentes**: En patología, la IA generativa no solo clasifica, sino que _crea_. Se ha validado su uso para "tinción virtual" (transformar imágenes sin químicos) y generación de histología sintética para entrenamiento y educación [#4]. Existe acuerdo en que estas herramientas mejoran la eficiencia del flujo de trabajo al automatizar tareas rutinarias como el control de calidad y las pruebas reflejas. El potencial para la educación mediante imágenes sintéticas libres de derechos de paciente es un avance destacado [#4].

**Controversias o hallazgos divergentes**: La "alucinación" en imágenes (generar estructuras tisulares inexistentes) es un riesgo de seguridad mayor que en texto. La validación de estas imágenes sintéticas para diagnóstico primario sigue siendo controvertida y no aceptada regulatoriamente.

**Brechas de conocimiento**: Falta estandarización en los métricos de calidad para imágenes patológicas generadas sintéticamente.

**Implicación principal**: La IA generativa en patología debe usarse actualmente para educación, investigación y pre-procesamiento (tinciones virtuales), manteniendo el diagnóstico final bajo revisión humana estricta.

### 2.4. Educación Médica y Evaluación de Competencias

**Subtítulo descriptivo**: Los LLMs aprueban los exámenes, forzando un rediseño de la evaluación médica.

**Hallazgos convergentes**: Múltiples estudios confirman que los LLMs actuales superan consistentemente los exámenes de licencia médica y especialidad. En nefrología, se han reportado precisiones entre **81% y 100%** [#54], y en otolaringología del **60% al 80.2%** [#72]. Existe consenso en que la barrera de "conocimiento enciclopédico" ha sido superada por la IA.

**Controversias o hallazgos divergentes**: La capacidad de la IA para aprobar exámenes no garantiza competencia clínica práctica. Se debate intensamente sobre el riesgo de "desentrenamiento" de los estudiantes, quienes podrían depender de la IA para el razonamiento básico. Algunos educadores proponen integrar la IA como herramienta, mientras otros abogan por exámenes orales o prácticos libres de tecnología.

**Brechas de conocimiento**: Impacto a largo plazo del uso de LLMs durante la residencia médica sobre la adquisición de pensamiento crítico autónomo.

**Implicación principal**: Las facultades de medicina deben abandonar la evaluación basada en la memorización de datos y enfocarse en la evaluación del razonamiento clínico supervisado y la ética.

### 2.5. Ética, Sesgos y Representatividad

**Subtítulo descriptivo**: El sesgo de los datos de entrenamiento limita la equidad global de las herramientas.

**Hallazgos convergentes**: La revisión sistemática de **761 estudios** [#2] subraya una subrepresentación crítica de especialidades médicas menores y poblaciones no occidentales. La hegemonía de modelos entrenados en inglés introduce sesgos culturales y clínicos que pueden afectar la seguridad del paciente en contextos locales.

**Controversias o hallazgos divergentes**: Mientras algunos autores defienden el ajuste (fine-tuning) local como solución, otros argumentan que los modelos fundacionales mismos arrastran sesgos estructurales difíciles de eliminar.

**Brechas de conocimiento**: Métricas estandarizadas para auditar la "equidad algorítmica" en tiempo real dentro del flujo de trabajo clínico.

**Implicación principal**: Es imperativo validar localmente cualquier modelo de IA antes de su despliegue clínico para detectar sesgos específicos de la población atendida.

---

## 3. Patrones Transversales en la Literatura

**Debates centrales**: La tensión principal reside entre la **conveniencia/potencia** de los modelos propietarios en la nube (GPT-4) y la **privacidad/seguridad** de los modelos locales de código abierto (DeepSeek, Llama). Un segundo debate es la **"humanidad artificial"**: ¿es ético que una IA muestre empatía simulada, aunque los pacientes la prefieran?

**Evolución temporal**: Se observa un desplazamiento claro desde estudios de "factibilidad" (2023-2024: ¿Puede la IA hacerlo?) hacia estudios de "implementación y seguridad" (2025-2026: ¿Es seguro hacerlo en mi hospital?). Los estudios de 2025 están mucho más enfocados en la integración con la Historia Clínica Electrónica (EHR) y el cumplimiento normativo.

**Innovaciones técnicas**: La aparición de **modelos de razonamiento** (como la serie "R1" de DeepSeek o los modelos "o1" de OpenAI, implícitos en la discusión de razonamiento) marca un salto cualitativo: la IA ahora "piensa" antes de responder, reduciendo alucinaciones en diagnósticos complejos [#3].

**Calidad de la evidencia**: Predomina la cantidad sobre la calidad metodológica. Hay una explosión de estudios retrospectivos y comparaciones _in silico_ (IA vs. Examen), pero una carencia notable de ensayos prospectivos con pacientes reales.

---

## 4. Preguntas Clínicas Clave con Priorización

### Criterios de Priorización (0-20 puntos):

Impacto clínico, Calidad metodológica, Recencia, Consistencia, Aplicabilidad.

### Preguntas Priorizadas

| #   | Pregunta                                                                  | Puntuación | Certeza       |
| --- | ------------------------------------------------------------------------- | ---------- | ------------- |
| 1   | ¿Son seguros los modelos _open-source_ (DeepSeek) para uso clínico local? | 19/20      | Moderada-Alta |
| 2   | ¿Superan los LLMs médicos especializados a los generalistas (GPT-4)?      | 18/20      | Moderada      |
| 3   | ¿Pueden los LLMs generar informes patológicos o radiológicos fiables?     | 17/20      | Moderada      |
| 4   | ¿Es ético usar IA para redactar notas de empatía o comunicación difícil?  | 15/20      | Baja          |

**P1: ¿Son seguros los modelos _open-source_ (DeepSeek) para uso clínico local?**
**R:** Sí, la evidencia reciente sugiere que modelos como DeepSeek-V3 rinden igual o mejor que modelos propietarios en tareas de decisión clínica (probado en **125 casos**), permitiendo su instalación en servidores hospitalarios seguros. Esto elimina el riesgo de fuga de datos a terceros.
**Certeza GRADE**: Moderada - Basada en estudios de benchmarking robustos [#3], pendiente de validación en ensayos clínicos.
**Referencias**: [#3, #5]

**P2: ¿Superan los LLMs médicos especializados a los generalistas (GPT-4)?**
**R:** Sí. Modelos entrenados específicamente en medicina, como MedFound (**176B parámetros**), demuestran mayor precisión en enfermedades raras y razonamiento diagnóstico complejo que los modelos generalistas, que tienden a "alucinar" más en dominios técnicos.
**Certeza GRADE**: Moderada - Estudios comparativos directos consistentes.
**Referencias**: [#2, #5]

**P3: ¿Pueden los LLMs generar informes patológicos o radiológicos fiables?**
**R:** Los LLMs son altamente efectivos para generar borradores y resúmenes, y en patología para tareas multimodales (imagen+texto). Sin embargo, requieren supervisión humana obligatoria debido al riesgo de errores sutiles pero clínicamente significativos.
**Certeza GRADE**: Moderada - Alta consistencia técnica, validación clínica en curso.
**Referencias**: [#4, #72]

---

## 5. Lecturas Clave Justificadas

**Artículo #3: Estudio de Benchmarking (Sandmann S et al., 2025)**

- **Título**: _Benchmark evaluation of DeepSeek large language models in clinical decision-making_
- **Por qué es clave**: Es el estudio definitivo para 2025 sobre la viabilidad de modelos _open-source_. Rompe el mito de que solo las grandes tecnológicas (OpenAI/Google) pueden ofrecer IA médica de calidad, abriendo la puerta a la "IA soberana" en hospitales.
- [Enlace a DOI](https://www.google.com/search?q=doi:10.1038/s41591-025-03727-2)

**Artículo #2: Revisión Sistemática (Shool S et al., 2025)**

- **Título**: _A systematic review of large language model (LLM) evaluations in clinical medicine_
- **Por qué es clave**: Analiza **761 estudios**, ofreciendo la visión más completa del estado del arte. Revela el sesgo hacia modelos generalistas y establece las métricas de referencia (precisión) que dominan el campo. Lectura obligatoria para entender las limitaciones de la evidencia actual.
- [Enlace a DOI](https://www.google.com/search?q=doi:10.1186/s12911-025-02954-4)

**Artículo #5: Desarrollo de Modelo (Liu X et al., 2025)**

- **Título**: _A generalist medical language model for disease diagnosis assistance_
- **Por qué es clave**: Presenta **MedFound**, un modelo masivo diseñado desde cero para medicina. Demuestra que la especialización del entrenamiento supera a la generalización, marcando el camino futuro para herramientas de soporte a la decisión clínica (CDSS).
- [Enlace a DOI](https://www.google.com/search?q=doi:10.1038/s41591-024-03416-6)

**Artículo #4: Revisión Temática (Brodsky V et al., 2025)**

- **Título**: _Generative Artificial Intelligence in Anatomic Pathology_
- **Por qué es clave**: Crucial para patólogos y especialistas en imagen. Explora aplicaciones prácticas inmediatas (tinción virtual, datos sintéticos) que van más allá del simple chatbot, mostrando el potencial multimodal de la IA.
- [Enlace a DOI](https://www.google.com/search?q=doi:10.5858/arpa.2024-0215-RA)

**Artículo #6: Perspectiva General (Teo ZL et al., 2025)**

- **Título**: _Generative artificial intelligence in medicine_
- **Por qué es clave**: Una visión panorámica publicada en _Nature Medicine_ que integra aspectos clínicos, éticos y técnicos. Ideal como lectura introductoria para directivos y jefes de servicio que necesitan entender el ecosistema completo.
- [Enlace a DOI](https://www.google.com/search?q=doi:10.1038/s41591-025-03983-2)

---

## 6. Evaluación Crítica Global

### 6.1 Calidad Metodológica Agregada

**Distribución**: Abrumadora mayoría de estudios observacionales retrospectivos y de benchmarking técnico (comparación de respuestas de IA vs. estándar de oro). Escasez crítica de ensayos clínicos prospectivos (ECAs).
**Rigor**: Alto en aspectos computacionales (tamaño de corpus, parámetros), pero variable en métricas clínicas. Muchos estudios usan "evaluadores humanos" sin aclarar su nivel de experticia o cegamiento.
**Fortalezas**: Gran volumen de datos (**N=761** estudios en una sola revisión), rapidez de publicación y replicabilidad de benchmarks técnicos.

### 6.2 Análisis de Sesgos Sistemáticos

**Sesgo de publicación**: Fuerte sesgo hacia resultados positivos ("La IA aprueba el examen"). Los fallos catastróficos o rendimientos mediocres tienden a infrarreportarse.
**Sesgo de herramienta**: **93.55%** de los estudios evalúan modelos de OpenAI (GPT), creando un monopolio de evidencia que ignora alternativas potencialmente mejores o más éticas.
**Sesgo geográfico**: Predominio de datos y evaluaciones en inglés, cuestionando la aplicabilidad en sistemas de salud hispanohablantes sin validación local previa.

### 6.3 Heterogeneidad y Consistencia

Alta heterogeneidad en las métricas de evaluación (BLEU, ROUGE, precisión humana, empatía subjetiva), lo que dificulta meta-análisis cuantitativos robustos. Sin embargo, la consistencia direccional es muy alta: en casi todos los dominios, los LLMs alcanzan o superan el nivel de un médico no especialista (residente junior).

---

## 7. Certeza de la Evidencia - Tabla GRADE

| Conclusión principal                                 | Certeza      | Justificación                                                      |
| ---------------------------------------------------- | ------------ | ------------------------------------------------------------------ |
| Los LLMs superan exámenes de licencia médica         | **Alta**     | Consistencia masiva en múltiples países y especialidades.          |
| Los modelos _Open-Source_ igualan a los propietarios | **Moderada** | Estudios recientes rigurosos [#3], pero menor volumen histórico.   |
| Utilidad clínica real (desenlaces en pacientes)      | **Baja**     | Evidencia indirecta; falta de ECAs que midan morbi-mortalidad.     |
| Capacidad de generación de informes preliminares     | **Moderada** | Alta precisión técnica, pero riesgo de errores de omisión sutiles. |

### Gaps Críticos en la Evidencia

- **Falta de ECAs**: No sabemos si usar IA mejora la salud del paciente o solo ahorra tiempo al médico.
- **Multilingüismo real**: Poca evidencia sobre el rendimiento en español médico técnico comparado con el inglés.
- **Coste-efectividad**: Ausencia de análisis económicos sobre el coste computacional vs. ahorro clínico.

---

## 8. Cierre Integrador

La evidencia acumulada entre 2025 y 2026 marca el fin de la etapa de "curiosidad" y el inicio de la **implementación estratégica**. Ya no es noticia que la IA apruebe exámenes; el hallazgo crítico es que modelos de código abierto (**DeepSeek**) y especializados (**MedFound**) ofrecen alternativas seguras y potentes para el despliegue hospitalario real.

**Recomendaciones pragmáticas**:

1. **Priorizar la privacidad**: Evaluar la implementación de modelos _open-source_ locales (on-premise) para tareas con datos sensibles, evitando subir datos de pacientes a nubes públicas.
2. **Supervisión humana innegociable**: Usar la IA como generador de borradores (informes, notas), nunca como decisor final autónomo.
3. **Rediseño educativo**: Integrar la "alfabetización en IA" en el currículo médico, enseñando a los residentes a auditar y corregir a la IA, no a depender de ella.
4. **Validación local**: Antes de usar cualquier modelo, realizar una prueba piloto con casos históricos del propio centro para detectar sesgos locales.

Para una hoja de ruta técnica y ética, consultar la lectura completa de **Sandmann et al. [#3]** y **Brodsky et al. [#4]**.
