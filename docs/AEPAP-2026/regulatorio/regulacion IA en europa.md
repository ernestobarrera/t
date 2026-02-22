# AI in pediatric practice: regulatory framework, privacy, and data protection

**Using large language models in pediatric clinical practice is legally permissible in Spain but requires navigating a multi-layered regulatory framework spanning the EU AI Act, GDPR, and Spanish national law — with particularly stringent protections for children's health data.** As of February 2026, the core obligations are already in force: AI literacy requirements (since February 2025), GPAI provider obligations (since August 2025), and the full GDPR apparatus including mandatory Data Protection Impact Assessments for any AI processing of pediatric health data. The high-risk AI system obligations for medical devices will apply from August 2027 at the earliest (possibly delayed to August 2028 under the Digital Omnibus proposal). This creates a transitional period during which the regulatory grey zone for informal use of tools like ChatGPT or Claude in clinical settings is significant — making data protection law, rather than the AI Act, the primary binding constraint on pediatricians today. This report provides the complete regulatory analysis, risk assessment, and practical guidance framework needed for the AEPap 2026 presentation.

> **Disclaimer**: This analysis reflects the regulatory landscape as of February 2026. EU AI Act implementation is ongoing, the EU-US Data Privacy Framework faces legal challenges, and Spanish legislation on minors in digital environments is under parliamentary review. All recommendations may require updating.

---

## 1. The EU AI Act classifies medical AI as high risk through two distinct pathways

The EU AI Act (Regulation 2024/1689), which entered into force on 1 August 2024, establishes a risk-based classification system with profound implications for healthcare AI.

**Pathway 1 — Medical device route (Article 6(1) + Annex I).** Any AI system that is itself a product or a safety component of a product covered by EU harmonisation legislation — including the Medical Device Regulation (MDR 2017/745) and the In Vitro Diagnostic Regulation (IVDR 2017/746) — and that requires third-party conformity assessment, is automatically classified as a high-risk AI system. Under the MDR, only Class I non-sterile, non-measuring devices are self-certified. Therefore, **all AI medical devices classified as MDR Class IIa, IIb, or III are automatically high-risk AI systems**. This covers AI-assisted radiological diagnosis, software providing diagnostic or therapeutic decision support, and software monitoring vital physiological parameters.

**Pathway 2 — Use-case route (Article 6(2) + Annex III).** Annex III, Section 5(d) specifically lists "AI systems intended to evaluate and classify emergency calls... or to be used to dispatch, or to establish priority in the dispatching of, emergency first response services, including... medical aid, as well as of emergency healthcare patient triage systems." AI for health insurance risk assessment (Section 5(c)) and emotion recognition in healthcare are also captured.

Article 6(3) provides exemptions for AI performing narrow procedural tasks, improving previously completed human activities, or performing preparatory tasks — meaning administrative tools like ICD-10 coding or structured reporting likely fall outside high-risk classification unless they qualify as medical devices.

### Obligations that high-risk systems must meet

The requirements imposed by Articles 8–15 are substantial. **Article 9 establishes a mandatory, continuous risk management system** throughout the AI's lifecycle. Article 10 requires training, validation, and testing data to be "relevant, sufficiently representative, error-free, and tailored to the AI system's intended purpose and target group." Article 11 mandates comprehensive technical documentation before market placement. **Article 13 requires sufficient transparency** for deployers to interpret outputs appropriately. Article 14 — the human oversight provision — requires that high-risk systems be designed for effective human oversight, specifically addressing the "possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system" (automation bias). Article 15 sets requirements for accuracy, robustness, and cybersecurity. Article 43 establishes conformity assessment procedures, creating dual compliance for medical AI: once for MDR, once for the AI Act.

The MDCG 2025-6 guidance document, published in June 2025 by the Medical Device Coordination Group and AI Board, confirmed that the AI Act technical documentation is "substantially more than the documentation needed for US FDA authorization of AI/ML-enabled medical devices."

### Implementation timeline as of February 2026

The Act is being phased in according to the following schedule. **Already in force**: prohibited practices and AI literacy obligations (since 2 February 2025); GPAI model obligations for providers like OpenAI and Anthropic (since 2 August 2025). **Upcoming**: most remaining provisions including Annex III high-risk obligations apply from **2 August 2026**; Article 6(1) obligations for medical device AI apply from **2 August 2027**. However, the European Commission's Digital Omnibus proposal of 19 November 2025, if adopted, would postpone Annex III high-risk obligations to a backstop of 2 December 2027 and medical device AI obligations to August 2028. MedTech Europe has advocated pushing to August 2029. Trilogue negotiations are expected mid-2026.

### The critical distinction: medical device AI versus ChatGPT at the bedside

This is perhaps the most consequential issue for the AEPap presentation. **A CE-marked AI diagnostic tool is fully regulated** under both MDR and the AI Act. But when a pediatrician pastes patient information into ChatGPT to support differential diagnosis, the regulatory picture is fundamentally different. ChatGPT is not designed or marketed as a medical device, so it does not fall under MDR and is not classified as a high-risk AI system under Article 6(1).

General-purpose AI models are regulated under Chapter V of the AI Act (Articles 51–56), which imposes obligations on the *provider* (OpenAI, Anthropic) for transparency, technical documentation, and copyright compliance. The European Parliament explicitly stated that "generative AI, like ChatGPT, will not be classified as high-risk." However, as Busch et al. noted in *npj Digital Medicine* (2024), "if [GPAI models] are used for medical purposes, such as LLM-enabled clinical reasoning and decision-making, they must also fulfil the MDR/IVDR and/or high-risk requirements" — a position whose practical enforceability remains uncertain. A hospital or healthcare organization using ChatGPT clinically becomes a "deployer" under Article 3(4), triggering AI literacy obligations (already binding) and transparency obligations (from August 2026). **The result is a significant regulatory grey zone** in which GDPR and professional liability law, rather than the AI Act itself, serve as the primary constraints on informal clinical AI use.

### Children receive explicit protection

**Article 9(9) is the most operationally significant pediatric provision**: "providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups." This creates a legally binding obligation to specifically assess impact on children in the risk management system of any high-risk AI system. Recital 28 explicitly acknowledges children as a distinct vulnerable group, referencing Article 24 of the EU Charter of Fundamental Rights, the UN Convention on the Rights of the Child, and General Comment No. 25 (2021) on children's rights in the digital environment. Article 5(1)(b) prohibits AI systems that exploit vulnerabilities related to age to distort behavior. Article 60 requires that children be "adequately protected" during real-world testing in regulatory sandboxes.

---

## 2. GDPR and Spanish law impose layered protections on minors' health data

### Health data as special category data under Article 9

GDPR Article 9(1) categorically prohibits the processing of health data, with exceptions listed in Article 9(2). For pediatric clinical practice, the primary legal basis is **Article 9(2)(h) — the medical purposes exception** — which permits processing "necessary for the purposes of preventive or occupational medicine, for the assessment of the working capacity of the employee, medical diagnosis, the provision of health or social care or treatment or the management of health or social care systems." This requires a dual legal basis: one from Article 6 (typically 6(1)(e) — public task, or 6(1)(c) — legal obligation) combined with the Article 9(2)(h) exception.

Critically, **Article 9(3) requires that health data under this basis be processed by or under the responsibility of a professional subject to the obligation of professional secrecy** under national law. This condition is satisfied when the processing physician is bound by *secreto profesional* under Spanish law.

### Article 8 and children's consent: a common misunderstanding

GDPR Article 8 sets special rules for children's consent in the context of "information society services" (ISS). It establishes a default age of 16 (Member States may lower to 13). However, **Article 8 applies exclusively to consent-based processing for ISS offered directly to children** — it does not apply to healthcare processing based on Article 9(2)(h). When a pediatrician uses an AI clinical tool, the legal basis is medical purposes, not consent under Article 6(1)(a). Article 8 becomes relevant only when a hospital offers a patient-facing app or digital health portal directly to minors.

### Spanish LOPDGDD: the 14-year threshold and pending changes

Spain's Ley Orgánica 3/2018 (LOPDGDD) sets the digital consent age at **14 years** in Article 7. For children under 14, data processing based on consent requires authorization from the holder of parental responsibility. For those 14-17, the minor may consent independently to ISS-related data processing. A Draft Organic Law for the Protection of Minors in Digital Environments, approved for parliamentary processing in September 2025, proposes **raising this age to 16 years**. As of February 2026, this law has not been enacted and the threshold remains 14.

For clinical practice, consent follows healthcare law rather than ISS consent rules. Under **Ley 41/2002**, minors aged 16+ can consent to medical treatment independently; minors aged 12–15 must be heard but parents consent; and for those under 12, parents or guardians consent. When a pediatrician uses AI for clinical decision support under Article 9(2)(h), no separate data-protection consent from the parent is needed for the clinical processing itself. However, if the pediatrician shares data with a commercial AI platform outside direct care, **explicit consent under Article 9(2)(a) would be required from the parent/guardian** for children under 14.

### A Data Protection Impact Assessment is always mandatory

GDPR Article 35 requires a DPIA when processing is "likely to result in a high risk to the rights and freedoms of natural persons," particularly when using new technologies. The AEPD's mandatory DPIA list specifies that a DPIA is required when two or more criteria are met. For AI tools processing pediatric health data, **at minimum three criteria are triggered simultaneously**: special category data (criterion 4), vulnerable subjects including minors under 14 (criterion 9), and use of new technologies including AI (criterion 10). If the AI contributes to clinical decisions, criterion 2 (automated decision-making) also applies. **A DPIA is therefore always legally required before deploying any AI tool for processing pediatric health data in Spain.**

### AEPD guidance and investigations

The AEPD published in 2020 its guide "Adecuación al RGPD de tratamientos que incorporan Inteligencia Artificial," a 52-page document establishing that AI solutions unable to answer basic questions about precision, accuracy, and data quality "cannot be considered based on mature technology" and fail accountability requirements. The guide identifies specific healthcare AI applications including image-based diagnosis, patient readmission prediction, and NLP of clinical records. The AEPD initiated ex officio investigation proceedings against OpenAI on 13 April 2023, contributing to the creation of an EDPB task force on ChatGPT. In February 2025, following the DeepSeek controversy, the Spanish consumer organization OCU filed a formal complaint with the AEPD alleging multiple GDPR violations by DeepSeek; the investigation remains ongoing. The AEPD announced in 2025 that it is reviewing and updating its AI-related guides in light of the EU AI Act.

---

## 3. Anonymization is necessary but dramatically insufficient for rare pediatric conditions

### The legal dividing line

GDPR Recital 26 establishes the critical distinction: **truly anonymized data falls outside GDPR scope entirely**, while pseudonymized data remains personal data subject to full GDPR obligations. Article 4(5) defines pseudonymization as processing personal data so it "can no longer be attributed to a specific data subject without the use of additional information," provided that additional information is kept separately. The identifiability test considers "all the means reasonably likely to be used" by the controller or any third party — a standard that LLMs dramatically expand, as discussed below.

The Article 29 Working Party's Opinion 05/2014 (WP216) evaluates anonymization techniques against three risk criteria: **singling out** (isolating an individual's records), **linkability** (linking records across datasets), and **inference** (deducing information about an individual). It concluded that only differential privacy may mitigate all three risks. The EDPB's January 2025 Guidelines 01/2025 on Pseudonymisation introduced the concept of a "pseudonymisation domain" and clarified that unauthorized reversal constitutes a personal data breach.

### Technical approaches and their limitations

**K-anonymity** ensures each record cannot be distinguished from at least k-1 others based on quasi-identifiers. For rare diseases, achieving meaningful k is extremely difficult — if only 3 people in a region have a specific condition, k can be at most 3. It is vulnerable to homogeneity attacks when all records in a group share the same sensitive value.

**L-diversity** extends k-anonymity by requiring diverse sensitive values within each group, but fails for rare diseases where certain diagnoses are inherently low-frequency. **T-closeness** requires the distribution of sensitive attributes in each equivalence class to approximate the global distribution, but causes excessive information loss for high-dimensional clinical data.

**Differential privacy** adds calibrated mathematical noise to outputs, controlled by epsilon (ε). A 2025 comparative study (Siminiuc et al., ICNBME) found that differential privacy at ε=1.0 achieved **re-identification risk below 0.1%** with negligible utility loss for rare disease registries, while k-anonymity at k=5 reduced risk to 2%. However, for small pediatric populations with rare conditions, noise addition can destroy clinical utility entirely.

**Synthetic data generation** using GANs or diffusion models creates artificial datasets mimicking real patient data. Sarkar et al. demonstrated in *Scientific Reports* (2024) that standard de-identification of clinical notes does not protect against membership inference attacks, while synthetic data generation provides substantially better protection. However, synthetic data is not automatically anonymous under GDPR and requires careful validation.

### Pediatric re-identification: when the diagnosis is the identifier

This is the most critical privacy concern for the AEPap presentation. A foundational study published in the *Orphanet Journal of Rare Diseases* (2020) found that **nearly 75% of rare disease patients were at high risk for re-identification** in healthcare datasets, due to unique combinations of indirect identifiers combined with their rare condition. For ultra-rare diseases with prevalence below 1 in 50,000, "identifying the name of the disease and the country of residence might be sufficient to identify an individual patient." The biological information characterizing a rare disease is precisely the information that identifies the patient.

**Geographic re-identification** is particularly acute in rural Spain, where many municipalities have very small populations. A pediatric patient with a specific rare condition in a small town may be the only such patient in the entire autonomous community. **Temporal re-identification** through unique combinations of age, diagnosis, and date of encounter creates "temporal fingerprints." **Aggregation attacks** combining multiple anonymized datasets compound the risk.

A transformative insight from Datavant (2024): LLMs are **"warping the notion of what information should be considered reasonably available"** under GDPR Recital 26. Because LLMs may be trained on an internet's worth of data, they could theoretically connect anonymized clinical details to other information in their training corpus, dramatically expanding re-identification risk. A 2025 scoping review in *JMIR* found that over 50% of healthcare LLM deployments use cloud infrastructure, and generative LLMs can "accidentally expose private data learned during training, including PII." Research on EHR foundation models demonstrated that memorization risk is amplified for patients in "long-tailed" (rare) groups — precisely the pediatric rare disease population.

### What practical de-identification looks like

For commercial LLM use, the most practical approach combines data masking with clinical abstraction. **Tier 1 (minimum)**: remove all direct identifiers (names, dates, locations, ID numbers); generalize ages to ranges; use temporary/ephemeral chat modes; disable training contributions. **Tier 2 (for rare or identifying conditions)**: abstract the clinical question to a mechanistic/pathophysiological level rather than naming the specific disease; remove all geographic references including implicit ones; assess whether the clinical combination itself is identifying. **Tier 3 (institutional/research)**: deploy local on-premise LLMs; use validated de-identification pipelines such as the LLM-Anonymizer (published in *NEJM AI*, 2025, achieving **99.24% success rate** using locally-deployed Llama-3 70B); implement differential privacy for aggregate analyses.

The core message for the presentation: **"In pediatrics, especially with rare diseases, removing the patient's name is necessary but nowhere near sufficient. The diagnosis itself, combined with even basic demographics, can be as identifying as a name. When a condition affects fewer than 1 in 50,000 children, the clinical question IS the identifier."**

---

## 4. Data transfers to Chinese AI providers are essentially incompatible with GDPR for health data

### The three-tier transfer framework

GDPR Chapter V establishes a hierarchy for international data transfers. Adequacy decisions (Article 45) allow free transfers to countries the Commission deems "essentially equivalent" in data protection — currently including the US (under the Data Privacy Framework, for certified organizations only), but **not China**. In the absence of adequacy, Standard Contractual Clauses (Article 46) require a Transfer Impact Assessment evaluating whether the destination country's legal framework allows effective compliance. Derogations under Article 49 (explicit consent, vital interests) are intended only for occasional, non-systematic transfers.

### The EU-US Data Privacy Framework: valid but fragile

The DPF was adopted on **10 July 2023** as an adequacy decision replacing the invalidated Privacy Shield. On 3 September 2025, the EU General Court dismissed French MP Philippe Latombe's annulment challenge, upholding the DPF's validity. However, **Latombe filed an appeal to the CJEU on 31 October 2025**, and NOYB criticized the General Court's ruling as "massively departing from CJEU case law." The DPF rests on Executive Order 14086 (Biden, October 2022), which can be revoked at any time by the US President. Key risks include the firing of PCLOB members (undermining independent oversight), Project 2025's explicit targeting of EO 14086 for repeal, and FISA Section 702 reauthorization without significant reform. The Norwegian DPA warned that if the DPF is revoked, "restrictions could be imposed immediately without a transition period."

Major AI companies' DPF and compliance status: **OpenAI** established OpenAI Ireland Limited as data controller for EEA users (February 2024), offers EU data residency, provides comprehensive DPAs, and does not train on API/Enterprise data by default — but was fined **€15 million by the Italian Garante**. **Anthropic** provides DPAs with SCCs incorporated into Commercial Terms, retains API logs for 7 days (reduced from 30 in September 2025), and offers Zero-Data-Retention for Enterprise — but lacks explicit EU data residency. **Microsoft Azure OpenAI** is DPF-certified, offers EU hosting in Frankfurt and Amsterdam with a data boundary program, and provides the strongest institutional compliance framework among US providers. **Google Vertex AI** is DPF-certified and allows EU data center selection.

Even with DPF certification, the US CLOUD Act allows US authorities to request data from US-headquartered companies regardless of where data is stored — a systemic risk that cannot be fully eliminated by contractual or technical measures.

### Chinese providers present extreme and essentially prohibitive risk

**Italy's Garante imposed an emergency ban on DeepSeek on 30 January 2025** — the first emergency ban on an AI chatbot under GDPR. The Garante found that DeepSeek's privacy policy states data is stored on servers in China, no GDPR-compliant safeguards exist (no SCCs, no BCRs), and no EU representative was appointed. In Spain, the OCU filed a formal complaint with the AEPD on 3 February 2025. Investigations were opened by DPAs in Belgium, Ireland, France, Greece, and Germany.

The fundamental legal problem is China's **National Intelligence Law (2017)**. Article 7 states: "All organizations and citizens shall support, assist, and cooperate with national intelligence efforts in accordance with law." Article 14 allows intelligence institutions to "request that relevant organs, organizations, and citizens provide necessary support, assistance, and cooperation." Chinese companies **cannot legally refuse** intelligence service requests for data access. The Cybersecurity Law (2017) additionally requires data localization and cooperation with public security organs. A Transfer Impact Assessment would almost certainly conclude that Chinese law makes Standard Contractual Clauses ineffective in practice.

### Provider risk hierarchy for clinical data

The risk spectrum runs from lowest to highest:

- **Local/on-premise deployment** (Mistral 7B, Llama 3 via Ollama): zero data transfer, complete sovereignty, lowest risk
- **European cloud providers** (Aleph Alpha/PhariaAI with BSI C5 certification, Mistral Le Chat Enterprise, OVHcloud with HDS healthcare hosting certification): EU jurisdiction only, no third-country transfer, GDPR-native
- **US providers with DPF + EU hosting** (Microsoft Azure OpenAI EU region, OpenAI Enterprise EU data residency): DPF valid but fragile, CLOUD Act risk persists
- **US providers without EU hosting** (Anthropic Claude API, OpenAI API standard): data may reside in US, DPF could be invalidated
- **Chinese providers** (DeepSeek, Qwen, Baichuan): no adequacy decision, intelligence law mandates cooperation, multiple EU bans and investigations — **essentially incompatible with GDPR for health data**

For pediatric clinical data involving special category health data of minors, **European-hosted or local deployment options should be the default**. Mistral AI (Paris) offers open-weight models under Apache 2.0 license that can be self-hosted, and a 2024 peer-reviewed study demonstrated competitive performance of locally-deployed small language models for clinical assistant tasks.

---

## 5. The physician always retains final liability — and lex artis is evolving

### Spanish medical liability and AI

Under Spain's established liability framework (Código Civil Articles 1902–1903 for extracontractual liability, Articles 1101–1107 for contractual), **the physician retains ultimate responsibility for clinical decisions**. As health law expert Ofelia De Lorenzo, President of the Asociación Española de Derecho Sanitario, wrote in April 2025: "The causes of claims for breach of *lex artis* in the context of AI-supported medicine will be the same as in traditional medical acts." The casuistry includes: physician liable for misusing correct AI output; manufacturer/developer liable for design defects; shared liability for erroneous diagnosis based on AI-generated erroneous data; and potential developer and institutional liability for bias-related harm.

The concept of **lex artis ad hoc** — the standard comparing a physician's conduct with what a competent peer would do given current scientific and technical knowledge — is evolving to incorporate AI competence. This means not only the ability to use AI tools appropriately but also to critically evaluate their outputs, understand their limitations, and override them when clinical judgment dictates. The EU AI Act's obligations on risk management, data governance, human oversight, and transparency function as a new "technological lex artis," where compliance or non-compliance becomes the benchmark for measuring diligence.

Spain's **Anteproyecto de Ley de Salud Digital** (Draft Digital Health Law, published September 2025) will integrate Ley 41/2002, GDPR, the EU AI Act, and the European Health Data Space Regulation (EU 2025/327) into a specific framework for AI in Spanish healthcare. Spain's Agencia Española de Supervisión de la IA (AESIA) oversees AI compliance, including in healthcare settings.

### Informed consent must address AI involvement

Under **Ley 41/2002, Articles 4–5**, patients have the right to "adequate, truthful, and comprehensible information" about their care. If AI participates in diagnosis or treatment recommendations, this constitutes relevant information. GDPR Articles 13–14 require information about how personal data is processed. The EU AI Act's transparency requirements reinforce this obligation. A January 2026 analysis in *Educación Médica* recommended that AI-related informed consent should include: that AI is being used and its purpose and limitations; that the physician retains final decision-making authority; how patient data will be processed; and the patient's right to alternatives including non-AI-assisted diagnosis. For pediatrics, parents or guardians exercise consent rights under Ley 41/2002 Article 9.

### Professional bodies have taken clear positions

The **World Medical Association**, in its Statement on Artificial and Augmented Intelligence in Medical Care adopted at the 76th General Assembly in Porto (October 2025), established the **Physician-in-the-Loop (PITL) principle**: a licensed physician must review and retain final authority over all AI outputs before clinical action. The statement warns that "anonymization of data does not provide enough protection when ML algorithms can identify an individual from as few as three data points."

The **Organización Médica Colegial** has emphasized that AI has "great competence capacity, but without the clinical context only the physician can provide" and that physicians must lead AI development and application in health. The OMC launched iAPAS, an AI tool for clinical guidelines, demonstrating institutional engagement while maintaining the primacy of physician judgment.

### A liability vacuum exists — but is being addressed

The proposed EU AI Liability Directive, which would have created a fault-based liability regime with presumption of causality, was **withdrawn by the European Commission in October 2025** as part of its 2025 work programme, citing lack of foreseeable agreement. However, the **revised Product Liability Directive (EU 2024/2853)** — which must be transposed by Member States by 9 December 2026 — explicitly includes software and AI as "products" subject to strict liability for defects causing death, personal injury, or medically recognized psychological harm. This eases the burden of proof for victims in technically complex cases.

**No European AI-specific medical malpractice case law exists yet.** A 2025 systematic review confirmed: "No harms or legal cases involved malpractice liability or claims in which physicians were suing or being sued for decisions made alongside AI systems." However, the parallel with telemedicine is instructive — before COVID-19, only one known Spanish malpractice case existed for telemedicine; after the pandemic, cases multiplied. The same trajectory is expected for AI. Pediatricians should verify with their insurers that their *seguro de responsabilidad civil* covers AI-assisted clinical decisions, as most existing policies were written before the AI era and may contain exclusions.

---

## 6. Practical decision framework for pediatricians using AI

### Risk stratification by clinical use case

The risk profile varies dramatically across different clinical AI applications. **Low risk**: generating parent information sheets about common conditions (e.g., bronchiolitis, fever management) — no patient data enters the system, any commercial AI tool is acceptable, but output must be reviewed for accuracy. **Medium risk**: differential diagnosis support using anonymized clinical parameters — requires replacing exact ages with ranges, removing all dates, locations, and identifiers, and never mentioning the patient by name or hospital. **High risk**: processing laboratory results or clinical images — only institutionally approved, GDPR-compliant tools integrated into the EHR should be used; consumer AI platforms are unacceptable. **Very high risk**: rare disease analysis where even anonymized data may be identifying — only certified medical AI platforms with institutional governance approval should be used; consumer AI tools must never be used.

### The 30-second anonymization protocol

In a 7-minute consultation, a pediatrician can realistically perform these steps before entering any clinical scenario into a commercial AI tool:

1. Replace all names with "Patient A" or "a child"
2. Generalize age to ranges ("infant 6–12 months" rather than "7-month-old born on 15 March 2025")
3. Replace specific dates with approximate timeframes ("3 days ago" rather than "6 February 2026")
4. Remove all geographic references including hospital name, city, and region
5. For rare conditions, reformulate at the pathophysiological level ("peroxisomal disorder affecting very-long-chain fatty acid metabolism" rather than naming X-linked adrenoleukodystrophy)
6. Omit medical record numbers, national ID, and health card numbers — always

A practical query template: *"Child aged [age range], [sex], presenting with [symptoms] for [approximate duration]. Relevant history: [generalized]. What differential diagnoses should be considered?"*

### When local deployment is required versus when cloud is acceptable

Cloud-based commercial AI is acceptable for: generic clinical questions without patient data, drug interaction queries, guideline summaries, continuing education, and generating informational materials for families. **Local or institutional deployment is required** when: the query involves identifiable patient data that cannot be adequately anonymized; rare diseases are involved where the clinical question itself is identifying; images (facial photographs, distinctive lesions) are being analyzed; or genetic or genomic data is being processed.

Open-source models that can be deployed locally include Mistral 7B and Mixtral 8x7B (Apache 2.0 license), Meta Llama 3/3.1 (various sizes), and Microsoft Phi-4 for edge devices. Tools like Ollama and llama.cpp make local deployment practical even on consumer hardware. A 7B-parameter model requires only 8–16 GB of VRAM.

### Essential elements of an institutional AI policy

Every primary care center using AI should establish a written policy covering:

- **Scope and definitions**: explicitly covering both certified medical AI tools and general-purpose LLMs like ChatGPT
- **Approved versus prohibited tools**: a whitelist of approved tools with explicit prohibition on entering patient data into public AI platforms
- **Risk classification**: matching the four-tier stratification above
- **Data protection rules**: mandatory DPIA before any new AI implementation; no personal data in non-institutional platforms
- **Informed consent protocols**: when and how to inform patients and parents about AI use
- **Clinical documentation**: requirement to record AI tool use in the medical record
- **Training requirements**: mandatory AI literacy training for all staff (already legally required under Article 4 of the AI Act since February 2025)
- **Incident reporting**: process for reporting AI errors or adverse events
- **Human oversight**: explicit statement that the physician retains final decision authority at all times
- **Named responsible persons**: AI lead clinician, information governance lead, and Data Protection Officer
- **Annual review cycle**: given the rapid evolution of AI regulation and technology

### Pre-use checklist for any AI tool

Before entering any patient-related information into an AI system, the pediatrician should confirm: Is the tool CE-marked or otherwise institutionally approved? Does the institution permit its use? Has a DPIA been completed? Are the data retention and training policies acceptable? Is the data transfer destination GDPR-compliant? Have all direct identifiers been removed? Could the clinical details themselves identify the patient? Is the patient or parent aware that AI may be used in their care? Will the AI interaction be documented in the clinical record?

---

## Conclusion: a regulatory framework that demands proactive compliance

The regulatory landscape for AI in pediatric practice is multi-layered but navigable. Three key insights emerge from this analysis that go beyond simple compliance checklists.

First, **the most binding constraints today are not from the AI Act but from GDPR**. While the AI Act's high-risk medical device obligations won't apply until at least August 2027, the GDPR's requirements for health data processing — including mandatory DPIAs, lawful transfer mechanisms, and the special protections for children's data — are fully enforceable now and carry fines of up to €20 million or 4% of annual turnover.

Second, **the re-identification problem in pediatrics is qualitatively different from adult medicine**. The rarity of many pediatric conditions means that the clinical information necessary for meaningful AI assistance is often the same information that identifies the patient. No technical anonymization technique fully resolves this tension for ultra-rare diseases. This demands a fundamental shift in how pediatricians formulate queries — moving from specific diagnoses to mechanistic descriptions, from exact demographics to broad categories.

Third, **the law is creating a new lex artis that includes AI competence**. The physician who blindly follows an AI recommendation without critical evaluation faces liability, but so may the physician who fails to use established AI tools that constitute the standard of care. The WMA's PITL principle, the OMC's emphasis on physician-led AI integration, and Article 14's human oversight requirements all converge on the same conclusion: AI is a powerful clinical instrument, but the pediatrician must remain its master, not its servant.

As Spain's Draft Digital Health Law works through parliament and the EU AI Act's high-risk obligations approach their application dates, the regulatory framework will continue to tighten. Pediatricians and their institutions who establish robust governance now — choosing European or local deployment options, conducting DPIAs, training staff in AI literacy, and documenting AI use in clinical records — will be well positioned for what comes next. Those who continue informal, undocumented use of consumer AI tools with patient data face escalating legal, regulatory, and professional risk.