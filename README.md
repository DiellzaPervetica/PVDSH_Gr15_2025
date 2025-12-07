# PVDSH_Gr15_2025
US Accidents (2016 - 2023)


### University Logo
Expand
message.txt
24 KB
Fjolla — 7:41 PM
Image
Perfect — po e përgatis **README-n final në shqip**, të plotë, të strukturuar sipas formatit profesional të UP-së dhe bazuar në të gjitha informacionet e projektit tënd.

---

# **README.md (Versioni Final në Shqip)**
Expand
message.txt
9 KB
# README -- Projekti i Përgatitjes dhe Vizualizimit të të Dhënave

```{=html}
<table>
```
```{=html}
Expand
message.txt
6 KB
# README -- Projekti i Përgatitjes, Detektimit të Anomalive dhe Vizualizimit të të Dhënave të Aksidenteve Rrugore

(Në vijim do të vendosen të gjitha seksionet e plota --- për shkak të
gjatësisë së dokumentit, kjo është vetëm struktura e skedarit. Më njofto
dhe unë do ta mbush automatikisht me versionin final të plotë.)
README (2).md
1 KB
Fjolla — 7:51 PM
fjolla.gjikolli1@student.uni-pr.edu
Diellza — 8:07 PM
Po e rikonstruktoj gjithë dokumentimin në stil më akademik, duke ruajtur strukturën dhe duke e thelluar shpjegimin metodologjik. Ti pastaj mund ta kopjosh si `README.md` dhe ta plotësosh me foto / figura.

---

### University Logo
Expand
message.txt
29 KB
Fjolla — 8:12 PM
Më poshtë është një version më **profesional**, më **i strukturuar** dhe edhe më **i detajizuar** i README-së tënde, i harmonizuar me kodin që ke dërguar (pipeline-i real i implementuar në Python). Nëse do, ti mund ta kopjosh drejtpërdrejt si `README.md` në GitHub.

---

### University Logo

**Universiteti i Prishtinës**
**Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike (FIEK)**

**Programi:** Inxhinieri Kompjuterike dhe Softuerike – Studime Master
**Lënda:** Përgatitja dhe vizualizimi i të dhënave
**Profesor:** PhD Mërgim Hoti

---

# Projekti

## “Data Preparation, Anomaly Detection and Visualization on Road Accident Data”

**Studentët (Gr. XX):**

* Emri 1
* Emri 2
* Emri 3
* Emri 4

*(Të plotësohet sipas përbërjes së grupit.)*

---

## Përmbajtja

1. [Përmbledhje e Projektit](#përmbledhje-e-projektit)
2. [Struktura e Repository-t](#struktura-e-repository-t)
3. [Përshkrimi i Dataset-it](#përshkrimi-i-dataset-it)
4. [Pipeline-i End-to-End](#pipeline-i-end-to-end)
5. [Teknikat e Zbatuara dhe Lidhja me Lëndën](#teknikat-e-zbatuara-dhe-lidhja-me-lëndën)
6. [Përshkrimi i Detajuar i Hapeve](#përshkrimi-i-detajuar-i-hapeve)
7. [Detektimi dhe Trajtimi i Anomalive / Outlier-ave](#detektimi-dhe-trajtimi-i-anomalive--outlier-ave)
8. [Trajtimi i Pabalancimit të Klasave me SMOTE](#trajtimi-i-pabalancimit-të-klasave-me-smote)
9. [Vizualizimet dhe Interpretimi i Rezultateve](#vizualizimet-dhe-interpretimi-i-rezultateve)
10. [Teknologjitë e Përdorura](#teknologjitë-e-përdorura)
11. [Instalimi dhe Ekzekutimi i Projektit](#instalimi-dhe-ekzekutimi-i-projektit)
12. [Rezultatet Kryesore dhe Vlerësimi](#rezultatet-kryesore-dhe-vlerësimi)
13. [Kufizimet dhe Supozimet](#kufizimet-dhe-supozimet)
14. [Punë e Ardhshme](#punë-e-ardhshme)

---

## Përmbledhje e Projektit

Ky projekt implementon një **pipeline të plotë, modular dhe të ripërdorshëm** për përgatitjen e të dhënave mbi aksidentet rrugore, duke filluar nga të dhënat bruto (raw) deri te një dataset i strukturuar, i balancuar dhe i gatshëm për aplikimin e algoritmeve të mësimit makinerik.

Theksi vendoset në:

* **Pastrimin dhe integrimin e të dhënave** (mungesa, duplikate, vlera të parregullta, standardizim teksti);
* **Inxhinierimin e karakteristikave (feature engineering)** me fokus në dimensionin kohor, gjeografik, meteorologjik dhe historik (risk i bazuar në frekuencë aksidentesh);
* **Detektimin dhe trajtimin e anomalive / outlier-ave**, si në hapësirën origjinale, ashtu edhe në hapësirën e reduktuar të PCA-së;
* **Scaling, normalizim dhe reduktim dimensionaliteti (PCA)** për të përmirësuar cilësinë e vizualizimeve dhe performancën e modeleve të mëvonshme;
* **Trajtimin e pabalancimit të klasave** të target-it (`Severity_binary`) me **SMOTE**;
* **Vizualizimin krahasues PARA/PAS** transformimeve të ndryshme për të vlerësuar ndikimin konkret të çdo faze.

Rezultati final është një dataset i përgatitur profesionalisht, i përshtatshëm për **klasifikimin e ashpërsisë së aksidenteve** dhe për studime të mëtejshme mbi riskun dhe faktorët ndikues të aksidenteve.

### Objektivat kryesore

* Projektimi i një **pipeline-i të riprodhueshëm** që mund të aplikohet edhe në dataset-e të ngjashme;
* Zbatimi i teknikave **statistike dhe bazuar në distancë** për detektimin dhe trajtimin e outlier-ave;
* Ndërtimi i **karakteristikave të orientuara drejt riskut**, si frekuenca e aksidenteve në periudha të shkurtra dhe mesatare ditore;
* Vlerësimi i ndikimit të **scaling, PCA dhe SMOTE** në hapësirën e të dhënave;
* Dokumentimi i të gjithë procesit, me referencë të qartë ndaj koncepteve të lëndës “Përgatitja dhe vizualizimi i të dhënave”.

---

## Struktura e Repository-t

```text
PVDH_GR_XX/
│
├── Datasets/
│   ├── sampled_dataset.csv                 # Dataset-i fillestar (sample)
│   ├── Week2_Dataset.csv                   # Pas shpërbërjes së datës në komponentë kohorë
│   ├── Week3_Dataset.csv                   # Pas pastrimit fillestar & imputimit bazik
│   ├── Week4_Dataset.csv                   # Pas feature engineering & diskretizimit fillestar
│   ├── df_binarized.csv                    # Pas binarizimit dhe heqjes së kolonave tekstuale
│   ├── df_transformed.csv                  # Versioni i ndërmjetëm pas disa transformimeve
│   ├── Week4_transformed_final.csv         # Pas scaling & normalizimit
│   ├── Week4_transformed_final2.csv        # Pas encoding shtesë (one-hot / label encoding)
│   ├── Week4_PCA.csv                       # Komponentët kryesorë nga PCA
│   └── ...                                 # Dataset-e intermediate shtesë
│
├── notebooks_or_scripts/
│   └── accident_preparation_pipeline.ipynb # Notebook kryesor me pipeline-in e implementuar
│
├── plots/
│   ├── missing_values_barplot.png          # Barplot i vlerave mungesë
│   ├── boxplots_iqr_before_after.png       # Boxplot PARA/PAS IQR
│   ├── scatter_iqr_before_after.png        # Scatterplots PARA/PAS IQR (me flag outlier)
│   ├── heatmap_corr_severity_binary.png    # Heatmap i korrelacioneve me Severity_binary
│   ├── heatmap_corr_before_after_iqr.png   # Heatmap PARA/PAS IQR
... (490 lines left)
Collapse
message.txt
26 KB
﻿
Fjolla
fjolla3355
 
Më poshtë është një version më **profesional**, më **i strukturuar** dhe edhe më **i detajizuar** i README-së tënde, i harmonizuar me kodin që ke dërguar (pipeline-i real i implementuar në Python). Nëse do, ti mund ta kopjosh drejtpërdrejt si `README.md` në GitHub.

---

### University Logo

**Universiteti i Prishtinës**
**Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike (FIEK)**

**Programi:** Inxhinieri Kompjuterike dhe Softuerike – Studime Master
**Lënda:** Përgatitja dhe vizualizimi i të dhënave
**Profesor:** PhD Mërgim Hoti

---

# Projekti

## “Data Preparation, Anomaly Detection and Visualization on Road Accident Data”

**Studentët (Gr. XX):**

* Emri 1
* Emri 2
* Emri 3
* Emri 4

*(Të plotësohet sipas përbërjes së grupit.)*

---

## Përmbajtja

1. [Përmbledhje e Projektit](#përmbledhje-e-projektit)
2. [Struktura e Repository-t](#struktura-e-repository-t)
3. [Përshkrimi i Dataset-it](#përshkrimi-i-dataset-it)
4. [Pipeline-i End-to-End](#pipeline-i-end-to-end)
5. [Teknikat e Zbatuara dhe Lidhja me Lëndën](#teknikat-e-zbatuara-dhe-lidhja-me-lëndën)
6. [Përshkrimi i Detajuar i Hapeve](#përshkrimi-i-detajuar-i-hapeve)
7. [Detektimi dhe Trajtimi i Anomalive / Outlier-ave](#detektimi-dhe-trajtimi-i-anomalive--outlier-ave)
8. [Trajtimi i Pabalancimit të Klasave me SMOTE](#trajtimi-i-pabalancimit-të-klasave-me-smote)
9. [Vizualizimet dhe Interpretimi i Rezultateve](#vizualizimet-dhe-interpretimi-i-rezultateve)
10. [Teknologjitë e Përdorura](#teknologjitë-e-përdorura)
11. [Instalimi dhe Ekzekutimi i Projektit](#instalimi-dhe-ekzekutimi-i-projektit)
12. [Rezultatet Kryesore dhe Vlerësimi](#rezultatet-kryesore-dhe-vlerësimi)
13. [Kufizimet dhe Supozimet](#kufizimet-dhe-supozimet)
14. [Punë e Ardhshme](#punë-e-ardhshme)

---

## Përmbledhje e Projektit

Ky projekt implementon një **pipeline të plotë, modular dhe të ripërdorshëm** për përgatitjen e të dhënave mbi aksidentet rrugore, duke filluar nga të dhënat bruto (raw) deri te një dataset i strukturuar, i balancuar dhe i gatshëm për aplikimin e algoritmeve të mësimit makinerik.

Theksi vendoset në:

* **Pastrimin dhe integrimin e të dhënave** (mungesa, duplikate, vlera të parregullta, standardizim teksti);
* **Inxhinierimin e karakteristikave (feature engineering)** me fokus në dimensionin kohor, gjeografik, meteorologjik dhe historik (risk i bazuar në frekuencë aksidentesh);
* **Detektimin dhe trajtimin e anomalive / outlier-ave**, si në hapësirën origjinale, ashtu edhe në hapësirën e reduktuar të PCA-së;
* **Scaling, normalizim dhe reduktim dimensionaliteti (PCA)** për të përmirësuar cilësinë e vizualizimeve dhe performancën e modeleve të mëvonshme;
* **Trajtimin e pabalancimit të klasave** të target-it (`Severity_binary`) me **SMOTE**;
* **Vizualizimin krahasues PARA/PAS** transformimeve të ndryshme për të vlerësuar ndikimin konkret të çdo faze.

Rezultati final është një dataset i përgatitur profesionalisht, i përshtatshëm për **klasifikimin e ashpërsisë së aksidenteve** dhe për studime të mëtejshme mbi riskun dhe faktorët ndikues të aksidenteve.

### Objektivat kryesore

* Projektimi i një **pipeline-i të riprodhueshëm** që mund të aplikohet edhe në dataset-e të ngjashme;
* Zbatimi i teknikave **statistike dhe bazuar në distancë** për detektimin dhe trajtimin e outlier-ave;
* Ndërtimi i **karakteristikave të orientuara drejt riskut**, si frekuenca e aksidenteve në periudha të shkurtra dhe mesatare ditore;
* Vlerësimi i ndikimit të **scaling, PCA dhe SMOTE** në hapësirën e të dhënave;
* Dokumentimi i të gjithë procesit, me referencë të qartë ndaj koncepteve të lëndës “Përgatitja dhe vizualizimi i të dhënave”.

---

## Struktura e Repository-t

```text
PVDH_GR_XX/
│
├── Datasets/
│   ├── sampled_dataset.csv                 # Dataset-i fillestar (sample)
│   ├── Week2_Dataset.csv                   # Pas shpërbërjes së datës në komponentë kohorë
│   ├── Week3_Dataset.csv                   # Pas pastrimit fillestar & imputimit bazik
│   ├── Week4_Dataset.csv                   # Pas feature engineering & diskretizimit fillestar
│   ├── df_binarized.csv                    # Pas binarizimit dhe heqjes së kolonave tekstuale
│   ├── df_transformed.csv                  # Versioni i ndërmjetëm pas disa transformimeve
│   ├── Week4_transformed_final.csv         # Pas scaling & normalizimit
│   ├── Week4_transformed_final2.csv        # Pas encoding shtesë (one-hot / label encoding)
│   ├── Week4_PCA.csv                       # Komponentët kryesorë nga PCA
│   └── ...                                 # Dataset-e intermediate shtesë
│
├── notebooks_or_scripts/
│   └── accident_preparation_pipeline.ipynb # Notebook kryesor me pipeline-in e implementuar
│
├── plots/
│   ├── missing_values_barplot.png          # Barplot i vlerave mungesë
│   ├── boxplots_iqr_before_after.png       # Boxplot PARA/PAS IQR
│   ├── scatter_iqr_before_after.png        # Scatterplots PARA/PAS IQR (me flag outlier)
│   ├── heatmap_corr_severity_binary.png    # Heatmap i korrelacioneve me Severity_binary
│   ├── heatmap_corr_before_after_iqr.png   # Heatmap PARA/PAS IQR
│   └── pca_explained_variance.png          # Varianca e shpjeguar nga PCA
│
├── README.md                               # Dokumentimi i projektit
└── requirements.txt                        # Lista e librarive të nevojshme
```

Struktura është e organizuar sipas parimeve të **riprodhueshmërisë**, **trasparencës** dhe **modularitetit**, duke ndarë qartë të dhënat, kodin, vizualizimet dhe dokumentimin. 

---

## Përshkrimi i Dataset-it

Dataset-i përfaqëson një koleksion të madh aksidentesh rrugore (p.sh. US Accidents), me shumë atribute numerike dhe kategoriale. Ai kombinon informacione **kohore**, **gjeografike**, **meteorologjike** dhe **infrastrukturore**, si dhe një variabël target (`Severity`), e cila pasohet me ndërtimin e një versioni binar (`Severity_binary`).

### Grupet kryesore të atributeve

#### 1. Identifikues & kohë

* `ID` – identifikues unik për secilin aksident;
* `Start_Time`, `End_Time` – koha e fillimit dhe mbarimit të aksidentit;
* `Weather_Timestamp` – koha e matjes së kushteve meteorologjike.

#### 2. Veti kohore të derivuara

Nga `Start_Time` dhe `End_Time` ndërtohen:

* `Start_Day`, `End_Day` – emri i ditës (Monday, Tuesday, ...);
* `Start_Month`, `End_Month` – emri i muajit;
* `Start_Year`, `End_Year` – viti;
* `Start_Hour`, `End_Hour` – ora (0–23);
* `Hour`, `Day`, `Month`, `Weekday` – veti kohore shtesë të derivuara nga `Start_Time`;
* `Is_Weekend` – indikator binar për fundjavë (1 = e shtunë/e diel; 0 = ditët tjera);
* `Season` – sezon (Winter, Spring, Summer, Fall) i deduktuar nga muaji.

Këto veti mundësojnë studimin e **modeleve kohore** të aksidenteve (p.sh. kulme në orët e pikut, ndryshime sezonale).

#### 3. Vendndodhja & infrastruktura

* `Start_Lat`, `Start_Lng`, `End_Lat`, `End_Lng` – koordinata gjeografike;
* `Distance(mi)` – gjatësia e segmentit të rrugës së prekur;
* `Street`, `City`, `County`, `State`, `Zipcode`, `Country`, `Timezone`, `Airport_Code` – informacione gjeo-administrative.

Këto kolona shërbejnë si bazë për:

* llogaritjen e **densitetit të aksidenteve** në zona të caktuara;
* krijimin e **indikatorëve historikë** si `Accident_Count_Last_Week`.

#### 4. Kushtet meteorologjike

* `Temperature(F)`, `Wind_Chill(F)`, `Humidity(%)`, `Pressure(in)`;
* `Visibility(mi)`, `Wind_Speed(mph)`, `Precipitation(in)`;
* `Weather_Condition`, `Wind_Direction`.

Prej tyre ndërtohen:

* `Temperature` – version i unifikuar numerik (nëse mungon si kolonë më vete);
* `Precipitation_raw` – reshjet në formë numerike;
* `Rain` – flag binar për praninë e reshjeve (`Precipitation_raw > 0` → 1, përndryshe 0);
* `Visibility` – kolonë e unifikuar për dukshmërinë.

#### 5. Koha e ditës / drita

* `Sunrise_Sunset`, `Civil_Twilight`, `Nautical_Twilight`, `Astronomical_Twilight` – variabla kategorialë rreth dritës natyrore artificiale/natyrore, të cilët binarizohen përmes one-hot encoding (p.sh. `Sunrise_Sunset_Night`).

#### 6. Karakteristika binare infrastrukturore

* `Amenity`, `Bump`, `Crossing`, `Give_Way`, `Junction`, `No_Exit`,
  `Railway`, `Roundabout`, `Station`, `Stop`, `Traffic_Calming`,
  `Traffic_Signal`, `Turning_Loop`.

Këto karakteristika ndihmojnë në identifikimin e **pikeve kritike** (p.sh. kryqëzime, ndalesa, semaforë) ku rreziku i aksidenteve është më i lartë.

#### 7. Target dhe veti të riskut

* `Severity` – ashpërsia (shofër, dëme materiale, lëndime, fatalitet, etj.);
* `Severity_binary` – variabël binar:

[
Severity_binary =
\begin{cases}
1, & \text{nëse } Severity \geq 3 \
0, & \text{përndryshe}
\end{cases}
]

* `Accident_Count_Last_Week` – numri i aksidenteve në 7 ditët e fundit për zonë;
* `Accidents_Per_Day_Avg` – mesatarja ditore e aksidenteve për zonë ose në nivel global.

---

## Pipeline-i End-to-End

Në terma të lartë, pipeline-i përbëhet nga:

1. Ngarkimi i dataset-it fillestar dhe eksplorimi i cilësisë;
2. Parsimi i datave dhe shpërbërja kohore (derivimi i vetive kohore);
3. Agregime eksploruese sipas orës dhe motit;
4. Heqja e kolonave me shumë mungesa dhe e duplikateve;
5. Pastrimi dhe standardizimi i tekstit;
6. Trajtimi i vlerave që mungojnë (numerike, kategoriale, kohore);
7. Feature engineering (kohore, meteorologjike, historike);
8. Diskretizim dhe binarizim i variablave;
9. Encoding i kolonave kategoriale dhe scaling/normalizim i atyre numerike;
10. Reduktimi i dimensionalitetit me PCA;
11. Detektimi dhe trajtimi i anomalive/univariate & multivariate;
12. Trajtimi i pabalancimit të klasave me SMOTE;
13. Vizualizime para/pas për interpretimin e transformimeve.

---

## Teknikat e Zbatuara dhe Lidhja me Lëndën

### Anomaly Detection

* **IQR-based outlier handling (univariate)**:
  Përdoret **Interquartile Range (IQR)** për të identifikuar outlier-at në çdo kolonë numerike kontinuele. Vlerat jashtë intervalit ([Q1 - 1.5 \cdot IQR, Q3 + 1.5 \cdot IQR]) konsiderohen ekstreme dhe **clamp-ohen** (jo fshihen) në kufijtë përkatës.

* **Z-score në hapësirën PCA (multivariate)**:
  Aplikohet `stats.zscore` mbi komponentët kryesorë (`PC1`, `PC2`, ...). Për secilin rresht:

  * llogaritet maksimumi absolut i Z-score-ve;
  * pikat me (|Z| < 3.5) mbahen si normale;
  * të tjerat konsiderohen kandidat-outlier.

Kjo mbështetet direkt në konceptet e **outlier detection** të trajtuara në lëndë (statistical dhe distance-based).

### Similarity & Distance

* **StandardScaler** dhe **Normalizer** përgatitin të dhënat në mënyrë që metrikat e distancës (si Euclidean) të jenë domethënëse;
* **SMOTE** përdor **k-nearest neighbors**, ku distancat në hapësirën vektoriale janë kyçe për gjenerimin e mostrave sintetike të klasës minoritare.

### Skewness & Spread

* IQR përdoret si masë **robuste** e shpërndarjes, më pak e ndjeshme ndaj outlier-ave;
* Diskretizimi me `KBinsDiscretizer(strategy="quantile")` ndihmon në trajtimin e shpërndarjeve të shtrembëra (skewed).

### Class Imbalance & SMOTE

* Pabalancimi i target-it `Severity_binary` trajtohet përmes **SMOTE**, duke krijuar një dataset ku klasat janë të balancuara dhe ku algoritmet klasike të klasifikimit mund të trajnohen më mirë (sidomos kur klasat e rralla janë më të rëndësishme).

---

## Përshkrimi i Detajuar i Hapeve

### 1. Ngarkimi i të dhënave dhe kontrolli fillestar

* Lezimi i `sampled_dataset.csv` me `pandas.read_csv`;
* `df.info()`, `df.shape`, `df.head()` për të inspektuar strukturën;
* `df.isnull().sum()` dhe llogaritja e numrit total të vlerave mungesë;
* Numërimi i placeholder-ve problematikë: `"?"`, `"-"`, `" "`, `"NA"`, `""`;
* Llogaritja e përqindjes së mungesave për kolonë dhe vizualizimi i tyre përmes një barplot-i.

**Qëllimi:** të identifikohen atributet me cilësi të dobët dhe kolonat që ndoshta duhen hequr ose trajtuar me kujdes shtesë.

---

### 2. Parsimi i datës dhe shpërbërja kohore

* Konvertimi i `Start_Time` dhe `End_Time` në `datetime`;
* Ndërtimi i `date_details` me `Start_Day`, `Start_Month`, `Start_Year`, `Start_Hour`, `End_Day`, `End_Month`, `End_Year`, `End_Hour`;
* Ruajtja e `dates_exploded.csv` dhe pastaj merge me dataset-in kryesor (`df_merged`);
* Riorganizimi i kolonave për një rend më logjik (kohor → metadata → të tjera).

---

### 3. Agregime eksploruese (EDA Aggregations)

Dy agregime kryesore:

1. **Sipas `Start_Hour`**:

   * `Accident_Count` – numri total i aksidenteve për çdo orë;
   * `Avg_Severity` – ashpërsia mesatare për orë.

2. **Sipas `Weather_Condition`**:

   * `Accident_Count` – numri i aksidenteve për çdo gjendje moti;
   * `Avg_Severity` – ashpërsia mesatare për secilën kategori meteorologjike.

Këto rezultate mund të vizualizohen dhe interpretohen për të identifikuar:

* intervale kohore me risk të lartë (p.sh. orët e pikut);
* kushte atmosferike që lidhen me rritje të ashpërsisë.

---

### 4. Heqja e kolonave me shumë mungesa dhe duplikateve

* Përcaktohet një prag prej 50% mungesa për kolonë;
* Kolonat që nuk e kalojnë këtë prag mbahen (`dropna(axis=1, thresh=threshold)`);
* Identifikohen dhe hiqen rreshtat e duplikuar (`df_merged.drop_duplicates()`).

Kjo rrit integritetin e të dhënave dhe zvogëlon rrezikun e mbifitimit (overfitting) për modele të mëvonshme.

---

### 5. Pastrimi i tekstit dhe standardizimi i string-ëve

* `str.strip()` për të hequr hapësirat e panevojshme;
* `str.title()` për emra (qytete, rrugë, twilight, etj.);
* `str.upper()` për kode (`State`, `Country`, `Timezone`, `Airport_Code`);
* Konvertim i `Weather_Timestamp` në `datetime`;
* Zëvendësimi i vlerave si `Unknown`, `None`, `N/A`, `UNK` me `NaN`.

Rezultati është një dataset më konsistent, ku vlerat semantikisht të barabarta nuk trajtohen si kategori të ndryshme për shkak të formatimit.

---

### 6. Trajtimi i vlerave që mungojnë

#### 6.1. Vlerat numerike dhe kategoriale

* Kolonat numerike: imputim me **medianë**, për të qenë robust ndaj outlier-ave;
* Kolonat kategoriale: imputim me **modën** (vlera më e shpeshtë);
* Raportimi i kolonave ku është kryer imputimi dhe numri i mungesave pas këtij procesi.

#### 6.2. Vlerat kohore

* Llogaritja e **kohezgjatjes mesatare** së ngjarjeve (`End_Time - Start_Time`);
* Plotësimi i `End_Time` nga `Start_Time` (dhe anasjelltas) kur njëra mungon;
* Plotësimi i `Weather_Timestamp` me `Start_Time`, duke supozuar matje meteorologjike afër kohës së aksidentit;
* Për çdo mbetje mungesash kohore, përdoret përsëri **mediana** e datave.

Kjo siguron **koherencë temporale** dhe redukton humbjen e rreshtave për shkak të mungesave kohore.

---

### 7. Feature Engineering

#### 7.1. Detektimi dinamik i kolonave

Përdoret një hartë (`col_map_lower`) për të gjetur kolonat e rëndësishme edhe kur emrat e tyre ndryshojnë pak (p.sh. `start_time`, `StartTime`, `occurred_on_date`). Kjo e bën pipeline-in:

* më **gjenerik**,
* më **i transferueshëm** mes dataset-esh të ndryshme.

#### 7.2. Veti meteorologjike

* `Temperature` (numerike);
* `Precipitation_raw` dhe `Rain`;
* `Visibility` – unifikimi i `Visibility(mi)` në një kolonë numerike standarde.

#### 7.3. Veti kohore

Nga `Start_Time`:

* `Hour`, `Day`, `Month`, `Weekday`, `Is_Weekend`;
* `Season` (Winter, Spring, Summer, Fall).

#### 7.4. Veti historike të aksidenteve

Në varësi të një **location key** (`City`, `State`, `Zipcode`, etj.):

* `daily_count` – numri i aksidenteve në ditë për zonë;
* `Accident_Count_Last_Week` – shuma lëvizëse 7-ditore e aksidenteve për zonë;
* `Accidents_Per_Day_Avg` – mesatarja ditore e aksidenteve për zonë.

Në mungesë të një location key, llogaritjet bëhen në **nivel global**.

---

### 8. Diskretizim dhe binarizim

* Përdoret `KBinsDiscretizer` me `n_bins=4`, `strategy='quantile'`;
* Vetit numerike me më shumë se 4 vlera unike diskretizohen → `*_Binned`;
* `Severity_binary` ndërtohet nga `Severity` (prag = 3);
* Variablat si `Sunrise_Sunset`, `Season` etj. kthehen në variabla dummy përmes `get_dummies`.

---

### 9. Encoding & Scaling

* Heqje e kolonave si `Street`, `City`, `Zipcode`, `Airport_Code`, `Description` (reduktim i dimensionit tekstual të panevojshëm);
* Përdorimi i kombinimit:

  * **StandardScaler** për kolona numerike me shumë vlera të ndryshme (kontinuele);
  * **Normalizer (L2)** për pjesën tjetër të kolonave numerike të zgjedhura;
  * **One-Hot Encoding** për `Source`, `Start_Day`, `End_Day`, `Weekday`, `Timezone`, `Weather_Condition`;
  * **LabelEncoder** për `County`, `State`, `Country`;
  * Mapim i muajve në vlera numerike (`January` → 1, etj.).

Dataset-i ruhet si `Week4_transformed_final2.csv`, ku të gjitha kolonat janë numerike dhe të gatshme për aplikimin e PCA-së dhe metodave të tjera.

---

### 10. Reduktimi i dimensionalitetit (PCA)

* Nxirren vetëm kolonat numerike;
* Aplikohet **StandardScaler** përpara PCA;
* Përdoret `PCA(n_components=0.95)` për të ruajtur **≥95% të variancës**;
* Ruhet matrica e komponentëve në `Week4_PCA.csv`;
* Vizualizohet `explained_variance_ratio_` për të parë kontributin e secilit komponent.

---

## Detektimi dhe Trajtimi i Anomalive / Outlier-ave

### 1. Z-Score në hapësirën PCA

* Llogaritet Z-score për çdo komponent;
* Për secilën observim merret maksimumi i Z-score-ve;
* Përdoret prag `|Z| < 3.5` për të përcaktuar rreshtat “normalë”;
* Krijohet `df_pca_clean` si variant i pastër i dataset-it në hapësirën PCA.

### 2. IQR Clamping në hapësirën origjinale

* Identifikohen kolonat numerike jo-binare me më shumë se 2 vlera unike;
* Për secilën kolonë llogariten Q1, Q3, IQR dhe kufijtë e pranuar;
* Vlerat jashtë intervalit zëvendësohen me kufijtë përkatës (clamping);
* Raportohet numri i outlier-ave të trajtuar për kolonë dhe në total.

Kjo qasje mbron strukturen e dataset-it (asnjë rresht nuk fshihet), duke reduktuar njëkohësisht **ndikimin e vlerave ekstreme**.

---

## Trajtimi i Pabalancimit të Klasave me SMOTE

* Ndahet dataset-i në:

  * `X` – të gjitha kolonat përveç `Severity_binary`;
  * `y` – kolona target `Severity_binary`.

* Llogaritet shpërndarja e klasave PARA SMOTE;

* Aplikohet `SMOTE(random_state=42, k_neighbors=5)`;

* Rikrijohet `df_smote` nga `X_res` dhe `y_res`;

* Raportohet shpërndarja e klasave PAS SMOTE.

Rezultati: klasat “serioze” (`Severity_binary = 1`) përfaqësohen më mirë, duke balancuar dataset-in për trajnime të mëtejshme.

---

## Vizualizimet dhe Interpretimi i Rezultateve

Pipeline-i gjeneron vizualizime që ndihmojnë në:

1. **Missing Values Barplot**

   * Paraqitja grafike e përqindjes së mungesave për kolonat kryesore.

2. **Scatterplots PARA/PAS IQR**

   * Pair-e si (`Start_Hour`, `Accident_Count_Last_Week`), (`Distance(mi)`, `Temperature(F)`), (`Start_Lat`, `Start_Lng`);
   * Pikat e clamp-uara shënohen me `IQR_status` për të dalluar outlier-at.

3. **Boxplots PARA/PAS IQR**

   * Për variabla si `Distance(mi)`, `Temperature(F)`, `Visibility(mi)`, `Precipitation(in)`, etj.;
   * Demonstrohet vizualisht reduktimi i vlerave ekstreme.

4. **Barplot për variablat binare PARA/PAS IQR**

   * Proporcioni i vlerave 1 për `Amenity`, `Bump`, `Crossing`, `Rain`, `Is_Weekend`, `Severity_binary`, etj.;
   * Tregohet se IQR clamping nuk ndryshon shpërndarjen e variablave binarë.

5. **Heatmap Atributeve më të lidhura me `Severity_binary`**

   * Seleksionim i top 12 variablave me korrelacion absolut më të madh;
   * Interpretim i lidhjes së tyre me ashpërsinë e aksidenteve.

6. **Heatmap PARA/PAS IQR**

   * Krahasim i matricës së korrelacionit para dhe pas clamping-ut;
   * Analizë nëse trajtimi i outlier-ave ka ndryshuar marrëdhëniet lineare midis variablave kryesorë.

7. **PCA Explained Variance Plot**

   * Tregon sa komponentë PCA janë të nevojshëm për të shpjeguar pjesën më të madhe të variancës.

---

## Teknologjitë e Përdorura

* **Python 3.x**
* **pandas** – manipulim dhe pastrim i të dhënave;
* **numpy** – operacione numerike;
* **matplotlib**, **seaborn** – vizualizime (barplot, boxplot, scatterplot, heatmap, etj.);
* **scikit-learn**:

  * `StandardScaler`, `Normalizer` – scaling & normalizim;
  * `KBinsDiscretizer` – diskretizim;
  * `PCA` – reduktim dimensionaliteti;
  * `LabelEncoder`, `get_dummies` – encoding i kolonave kategoriale;
  * (`SelectKBest`, `f_classif`) – të parapara për seleksionim karakteristikash;
* **imbalanced-learn** – `SMOTE` për oversampling të klasës minoritare;
* **SciPy** – `stats.zscore` për Z-score në hapësirën PCA.

---

## Instalimi dhe Ekzekutimi i Projektit

### 1. Parakushte

* Python 3.8+
* `pip` i instaluar
* Hapësirë disk-u: ~1–2 GB

### 2. Klonimi i repository-t

```bash
git clone <repo-url>
cd PVDH_GR_XX
```

### 3. Virtual environment (rekomandohet)

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Instalimi i librarive

```bash
pip install -r requirements.txt
```

ose:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn imbalanced-learn scipy
```

### 5. Ekzekutimi i pipeline-it

* Hap `notebooks_or_scripts/accident_preparation_pipeline.ipynb`;
* Ekzekuto cell-at në rend;
* Dataset-et intermediate krijohen automatikisht në `Datasets/`;
* Vizualizimet mund të ruhen në `plots/`.

---

## Rezultatet Kryesore dhe Vlerësimi

* Dataset-i fillestar është transformuar në një seri versionesh të ndërmjetme, secili duke rritur **cilësinë** dhe **strukturalitetin** e të dhënave;

* Mungesat janë trajtuar sistematikisht përmes:

  * imputimit statistikor (medianë, modë);
  * logjikës specifike kohore (ruajtje e rendit kronologjik).

* Janë krijuar karakteristika domethënëse të orientuara drejt riskut:

  * `Is_Weekend`, `Season`, `Rain`, `Accident_Count_Last_Week`, `Accidents_Per_Day_Avg`, etj.

* Është aplikuar **PCA** për të ulur dimensionalitetin duke ruajtur rreth 95% të variancës;

* Janë implementuar dy qasje për **outlier detection**:

  * Z-score në hapësirën PCA (multivariate);
  * IQR clamping në hapësirën origjinale (univariate, robust).

* Është përdorur **SMOTE** për të balancuar klasat në `Severity_binary`, duke krijuar një bazë të fortë për ndërtimin e modeleve klasifikuese ku klasat e rralla janë kritike nga këndvështrimi i riskut.

---

## Kufizimet dhe Supozimet

* Supozohet që të dhënat e motit (`Weather_Timestamp`) janë të vlefshme në afërsi të kohës së aksidentit (`Start_Time`);
* Përdorimi i pragut `Severity >= 3` për ndërtimin e `Severity_binary` është një zgjedhje e bazuar në interpretimin e ashpërsisë, por mund të ndryshohet;
* I njëjti pipeline nuk merr parasysh aktualisht **aspektet hapësinore më të avancuara** (p.sh. clustering gjeografik, distanca midis aksidenteve);
* Disa teknika të importuara (p.sh. `IsolationForest`) janë të planifikuara për përdorim, por jo të integruara plotësisht në versionin aktual të notebook-ut.

---
