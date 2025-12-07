# PVDSH_Gr15_2025
US Accidents (2016 - 2023)


<table>
  <tr>
    <td width="150" align="center" valign="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/University_of_Prishtina_logo.svg/1200px-University_of_Prishtina_logo.svg.png" width="120" alt="University Logo" />
    </td>
    <td valign="top">
      <p><strong>Universiteti i Prishtinës</strong></p>
      <p>Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike</p>
      <p>Inxhinieri Kompjuterike dhe Softuerike - Programi Master</p>
      <p><strong>Projekti nga lënda:</strong> “Përgatitja dhe vizualizimi i të dhënave”</p>
      <p><strong>Profesor:</strong> PhD Mërgim Hoti</p>
      <p><strong>Studentët (Gr. 15):</strong></p>
      <ul>
        <li>Adonis Xhemajili</li>
        <li>Fjolla Gjikolli</li>
        <li>Diellza Përvetica</li>
      </ul>
    </td>
  </tr>
</table>

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
├── README.md                               # Dokumentimi i projektit
└── main.ipynb                              #Kodi i punimit
```
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

* Leximi i `sampled_dataset.csv` me `pandas.read_csv`;


   <img width="418" height="63" alt="{F595F214-85B3-404D-A972-A37C67EF2CC3}" src="https://github.com/user-attachments/assets/abd9df5b-7f75-4aba-9c72-91c5d562b708" />


* `df.info()`, `df.shape`, `df.head()` për të inspektuar strukturën;
  
  
 <img width="436" height="362" alt="{B37AD6C0-A389-4A21-933E-4CC00DB9CF3A}" src="https://github.com/user-attachments/assets/6359c7d2-4014-4b13-9dc8-3f869a815b35" />

  
* `df.isnull().sum()` dhe llogaritja e numrit total të vlerave mungesë;


 <img width="436" height="357" alt="{9B4FE55B-FC64-4A89-8C99-27ECAE66E67D}" src="https://github.com/user-attachments/assets/3a2f24b3-01d7-416d-bc5b-044d86d3603d" />


* Numërimi i placeholder-ve problematikë: `"?"`, `"-"`, `" "`, `"NA"`, `""`;


 <img width="435" height="100" alt="{D37F58EA-E9C8-4DA3-A647-C9DFA411FCDA}" src="https://github.com/user-attachments/assets/d4d06702-1462-492c-a13e-250701379b3a" />


* Llogaritja e përqindjes së mungesave për kolonë dhe vizualizimi i tyre përmes një barplot-i.


 <img width="438" height="373" alt="{5425DCDF-9CB4-4BB9-9ECE-5BF31828E402}" src="https://github.com/user-attachments/assets/4cd9b3c2-cdcc-4bde-bf24-9541a28b2c24" />


**Qëllimi:** të identifikohen atributet me cilësi të dobët dhe kolonat që ndoshta duhen hequr ose trajtuar me kujdes shtesë.

---

### 2. Parsimi i datës dhe shpërbërja kohore

* Konvertimi i `Start_Time` dhe `End_Time` në `datetime`;


 <img width="434" height="48" alt="{EA534C05-00A1-4040-AE53-D4655D52F6D7}" src="https://github.com/user-attachments/assets/ebb8abda-4d55-43f0-bde2-014d56d97759" />

  
* Ndërtimi i `date_details` me `Start_Day`, `Start_Month`, `Start_Year`, `Start_Hour`, `End_Day`, `End_Month`, `End_Year`, `End_Hour`;


 <img width="433" height="137" alt="{CAFF7002-37F9-4EA1-AB76-70ECDBDBACEF}" src="https://github.com/user-attachments/assets/9a896318-77a7-433e-96ee-0397145823a2" />


* Ruajtja e `dates_exploded.csv` dhe pastaj merge me dataset-in kryesor (`df_merged`);


 <img width="432" height="38" alt="{E70E1A7E-1956-4A6D-9C47-755B0B78496C}" src="https://github.com/user-attachments/assets/2379c3e5-6f33-40cc-9277-062efe4d7438" />


 <img width="432" height="40" alt="{FD9C7A7D-6B92-4DB3-A881-45741F1D43C6}" src="https://github.com/user-attachments/assets/887acda8-eba0-46c6-89c3-f81247963f45" />


* Riorganizimi i kolonave për një rend më logjik (kohor → metadata → të tjera).
  

 <img width="434" height="98" alt="{911401FA-0939-4779-95FC-F383198A3A8F}" src="https://github.com/user-attachments/assets/5b3f1228-20a8-4f1b-bf66-5bc5c622a00a" />


---

### 3. Agregime eksploruese (EDA Aggregations)

Dy agregime kryesore:

1. **Sipas `Start_Hour`**:

   * `Accident_Count` – numri total i aksidenteve për çdo orë;
   * `Avg_Severity` – ashpërsia mesatare për orë.


 <img width="430" height="110" alt="{76425CA8-17A5-492A-B4BF-A0C819ED0694}" src="https://github.com/user-attachments/assets/e1389a17-56c1-4bc1-9135-9dd36e581979" />


2. **Sipas `Weather_Condition`**:

   * `Accident_Count` – numri i aksidenteve për çdo gjendje moti;
   * `Avg_Severity` – ashpërsia mesatare për secilën kategori meteorologjike.


 <img width="436" height="113" alt="{695A1F88-0F57-4B9E-AA9C-5BE52C08890F}" src="https://github.com/user-attachments/assets/7dbab9f7-da2b-45e4-b225-04a4c6c04e74" />


Këto rezultate mund të vizualizohen dhe interpretohen për të identifikuar:

* intervale kohore me risk të lartë (p.sh. orët e pikut);
* kushte atmosferike që lidhen me rritje të ashpërsisë.

---

### 4. Heqja e kolonave me shumë mungesa dhe duplikateve

* Përcaktohet një prag prej 50% mungesa për kolonë;
* * Kolonat që nuk e kalojnë këtë prag mbahen (`dropna(axis=1, thresh=threshold)`);


 <img width="433" height="212" alt="{1DDCD82D-6C0E-4C35-BF62-56BF1BE760F2}" src="https://github.com/user-attachments/assets/416096be-ea4c-46c6-b5e7-ebc3bc7b9bc5" />


* Identifikohen dhe hiqen rreshtat e duplikuar (`df_merged.drop_duplicates()`).


 <img width="421" height="91" alt="{F5F45FD8-5846-4AA9-87B0-6A5E918A76AA}" src="https://github.com/user-attachments/assets/ff929786-9e86-4b74-b2dd-8e519f09f079" />


Kjo rrit integritetin e të dhënave dhe zvogëlon rrezikun e mbifitimit (overfitting) për modele të mëvonshme.

---

### 5. Pastrimi i tekstit dhe standardizimi i string-ëve

* `str.strip()` për të hequr hapësirat e panevojshme;
* `str.title()` për emra (qytete, rrugë, twilight, etj.);
* `str.upper()` për kode (`State`, `Country`, `Timezone`, `Airport_Code`);
* Konvertim i `Weather_Timestamp` në `datetime`;
* Zëvendësimi i vlerave si `Unknown`, `None`, `N/A`, `UNK` me `NaN`.


 <img width="432" height="284" alt="{2BF9477A-2DE5-4763-99E0-6631B4EC0EA7}" src="https://github.com/user-attachments/assets/4edbd491-83a6-4f63-ad84-ea70a1da7692" />


Rezultati është një dataset më konsistent, ku vlerat semantikisht të barabarta nuk trajtohen si kategori të ndryshme për shkak të formatimit.

---

### 6. Trajtimi i vlerave që mungojnë

#### 6.1. Vlerat numerike dhe kategoriale

* Kolonat numerike: imputim me **medianë**, për të qenë robust ndaj outlier-ave;


 <img width="443" height="77" alt="{072E3C52-5D59-47D2-8EAB-F2E9DAA5AEC5}" src="https://github.com/user-attachments/assets/7d203923-9c71-4f9a-b298-db93af7de425" />

 <img width="433" height="133" alt="{6426A599-DAC2-44D6-BD64-4D544C7466FA}" src="https://github.com/user-attachments/assets/32fb827e-1106-4931-bba2-eeea5092e047" />


* Kolonat kategoriale: imputim me **modën** (vlera më e shpeshtë);


 <img width="425" height="71" alt="{FFCB6A71-7A86-4A0A-B6B1-C23ED86EB3EA}" src="https://github.com/user-attachments/assets/56b59943-26ff-4e71-aecb-93ff2463343a" />
 <img width="437" height="160" alt="{D30D56D1-6D42-49B8-965E-0D78F4AD7EA0}" src="https://github.com/user-attachments/assets/d9d2712e-9174-45f0-bd4f-3b022265a7df" />


* Raportimi i kolonave ku është kryer imputimi dhe numri i mungesave pas këtij procesi.


 <img width="420" height="39" alt="{242FD4D6-E76A-4925-AF77-904195B61DD3}" src="https://github.com/user-attachments/assets/d699891b-d082-48a1-8a07-0cabf0915861" />
 <img width="438" height="15" alt="{450A57D0-22B1-4529-B0A9-8C834036D93F}" src="https://github.com/user-attachments/assets/f9046736-996f-4126-ae63-7f3f17fde816" />


#### 6.2. Vlerat kohore

* Llogaritja e **kohezgjatjes mesatare** së ngjarjeve (`End_Time - Start_Time`);


 <img width="421" height="89" alt="{FC9CC96F-85E5-4F7D-83D8-0041CF759B3E}" src="https://github.com/user-attachments/assets/7977d207-0915-4105-bf50-f3074bebfbc3" />


* Plotësimi i `End_Time` nga `Start_Time` (dhe anasjelltas) kur njëra mungon;


 <img width="426" height="64" alt="{DA4ADF31-91C9-4FE2-BDE0-8C3C5BC58EA3}" src="https://github.com/user-attachments/assets/41f4f093-a803-42eb-a09c-8defb726067b" />


* Plotësimi i `Weather_Timestamp` me `Start_Time`, duke supozuar matje meteorologjike afër kohës së aksidentit;


 <img width="420" height="22" alt="{CAB1EE67-11DA-442F-8007-B70090A60DD2}" src="https://github.com/user-attachments/assets/fa87b511-57d8-45de-830d-3a3f25e6eba6" />


* Për çdo mbetje mungesash kohore, përdoret përsëri **mediana** e datave.


 <img width="425" height="85" alt="{F79620CF-9EE8-4528-A509-26B6730EA8B5}" src="https://github.com/user-attachments/assets/310876e8-1e81-4165-bdc3-cac33c2cdc38" />
 <img width="432" height="54" alt="{5BFFBF19-BDF6-4826-9AD1-FDF935BC08EF}" src="https://github.com/user-attachments/assets/2cc360c9-be0e-4499-a03c-7f40c610258d" />


Kjo siguron **koherencë temporale** dhe redukton humbjen e rreshtave për shkak të mungesave kohore.

---

### 7. Feature Engineering

#### 7.1. Detektimi dinamik i kolonave

Përdoret një hartë (`col_map_lower`) për të gjetur kolonat e rëndësishme edhe kur emrat e tyre ndryshojnë pak (p.sh. `start_time`, `StartTime`, `occurred_on_date`). Kjo e bën pipeline-in:


<img width="429" height="291" alt="{67702E16-6022-444C-94E5-63E10EA552B7}" src="https://github.com/user-attachments/assets/7c466408-47cb-44d9-a9b6-13cf86e967fe" />


* më **gjenerik**,
* më **i transferueshëm** mes dataset-esh të ndryshme.

#### 7.2. Veti meteorologjike

* `Temperature` (numerike);


 <img width="426" height="30" alt="{5DE1350E-778F-4FAC-99D8-9F9BB8EB6735}" src="https://github.com/user-attachments/assets/5a0b6213-bc9a-4721-bfa1-211906617c48" />


* `Precipitation_raw` dhe `Rain`;]


 <img width="433" height="70" alt="image" src="https://github.com/user-attachments/assets/5a2797e2-d9fc-4b90-8f36-7f515d5f0932" />


* `Visibility` – unifikimi i `Visibility(mi)` në një kolonë numerike standarde.


 <img width="423" height="28" alt="{78B0C205-3D87-41C9-858F-7316B0FBAE53}" src="https://github.com/user-attachments/assets/0c7cac90-9d47-4187-a870-af03d60a12d4" />


#### 7.3. Veti kohore

Nga `Start_Time`:


 <img width="422" height="64" alt="{94972373-A09B-4F6C-9280-BA136460CD25}" src="https://github.com/user-attachments/assets/784a42d3-bce9-4973-868a-27136331c706" />


* `Hour`, `Day`, `Month`, `Weekday`, `Is_Weekend`;


 <img width="438" height="55" alt="{75043318-0292-4467-9381-5C9E27C97B81}" src="https://github.com/user-attachments/assets/9bc4276f-edff-475e-b3f0-62a90525ff8f" />


* `Season` (Winter, Spring, Summer, Fall).


 <img width="425" height="87" alt="{E7552E9F-1D6F-4784-A37C-16D175459B62}" src="https://github.com/user-attachments/assets/0d8920e7-df05-495f-a3f6-287aa5fa363c" />


#### 7.4. Veti historike të aksidenteve

Në varësi të një **location key** (`City`, `State`, `Zipcode`, etj.):

* `daily_count` – numri i aksidenteve në ditë për zonë;
* `Accident_Count_Last_Week` – shuma lëvizëse 7-ditore e aksidenteve për zonë;
* `Accidents_Per_Day_Avg` – mesatarja ditore e aksidenteve për zonë.


 <img width="905" height="414" alt="{28949133-7FA3-4E91-93E9-431CF2B64168}" src="https://github.com/user-attachments/assets/1850b1cb-c22d-4be8-8f07-8afc31923d78" />
 <img width="898" height="116" alt="image" src="https://github.com/user-attachments/assets/f2b271ab-7310-4418-9c2e-e619bb136771" />


Në mungesë të një location key, llogaritjet bëhen në **nivel global**.

---

### 8. Diskretizim dhe binarizim

* Përdoret `KBinsDiscretizer` me `n_bins=4`, `strategy='quantile'`;


 <img width="424" height="26" alt="{C0027E35-3EF0-4A06-A63F-8691E6BA1FA9}" src="https://github.com/user-attachments/assets/834ad252-0d82-475e-b112-6a9ece51fac0" />


* Vetit numerike me më shumë se 4 vlera unike diskretizohen → `*_Binned`;


 <img width="436" height="72" alt="{3F0F4D24-53FC-42F5-8396-62E09C39EDCF}" src="https://github.com/user-attachments/assets/3788d961-ebbc-46a7-8aed-050190548d39" />

* Pamje


 <img width="430" height="360" alt="{A801F1E7-ADC1-49D7-91CC-C5A2053CBE1A}" src="https://github.com/user-attachments/assets/d1b34942-ce86-43c7-9404-4b481369b078" />

<img width="910" height="64" alt="{25DE1518-6879-4C28-ACC9-11A6BDC77B73}" src="https://github.com/user-attachments/assets/b132d5c9-8dee-4068-a41d-20156ccf1252" />


---

### 9. Encoding & Scaling

* Heqje e kolonave si `Street`, `City`, `Zipcode`, `Airport_Code`, `Description` (reduktim i dimensionit tekstual të panevojshëm);


 <img width="435" height="89" alt="{A2F7140D-DB47-4097-83F4-835FA1F92EAE}" src="https://github.com/user-attachments/assets/55143d4e-3c6f-4471-8514-ca24c0212660" />
 <img width="437" height="88" alt="{E3E77E08-78D9-45A0-B78F-0D9E0D679178}" src="https://github.com/user-attachments/assets/76f5340d-ed3f-44e0-a114-51203c27153a" />


* Përdorimi i kombinimit:

  * **StandardScaler** për kolona numerike me shumë vlera të ndryshme (kontinuele);
 

 <img width="428" height="91" alt="{D3772787-BD7F-4995-A006-7CC6EB345424}" src="https://github.com/user-attachments/assets/24cc6873-99a4-41c4-b9a8-ab62f9f850e3" />


  * **Normalizer (L2)** për pjesën tjetër të kolonave numerike të zgjedhura;


 <img width="442" height="85" alt="{32853F66-D3C6-4F0F-ADF8-7AF94A922D49}" src="https://github.com/user-attachments/assets/030fe229-d16a-42e4-9cfe-32f541ff08a4" />


  * **One-Hot Encoding** për `Source`, `Start_Day`, `End_Day`, `Weekday`, `Timezone`, `Weather_Condition`;
  * **LabelEncoder** për `County`, `State`, `Country`;
  * Mapim i muajve në vlera numerike (`January` → 1, etj.).

 <img width="436" height="340" alt="{4E84F8A6-7EFC-4101-96F0-38AAEE24C5CE}" src="https://github.com/user-attachments/assets/03a6d96c-e4eb-4bf5-a483-3f93efe8a8b0" />


Dataset-i ruhet si `Week4_transformed_final2.csv`, ku të gjitha kolonat janë numerike dhe të gatshme për aplikimin e PCA-së dhe metodave të tjera.

---

### 10. Reduktimi i dimensionalitetit (PCA)

* Nxirren vetëm kolonat numerike;
* Aplikohet **StandardScaler** përpara PCA;


 <img width="584" height="455" alt="image" src="https://github.com/user-attachments/assets/f3ef2264-cd87-432b-8d20-9dfdde84cdc0" />


* Përdoret `PCA(n_components=0.95)` për të ruajtur **≥95% të variancës**;


 <img width="415" height="59" alt="{4C2A751E-BC47-4F6E-B30D-1F92F1C2163C}" src="https://github.com/user-attachments/assets/11279e51-793b-4340-bea8-18927d6e7296" />


* Ruhet matrica e komponentëve në `Week4_PCA.csv`;


 <img width="419" height="103" alt="{3B909D11-27E2-4DA0-83A8-7DB9466C6079}" src="https://github.com/user-attachments/assets/13b10d8b-babc-46a5-8585-0d82f9d9e117" />


* Vizualizohet `explained_variance_ratio_` për të parë kontributin e secilit komponent.


 <img width="318" height="247" alt="{6FEDDE73-4713-4D2D-8CD1-B7F1318A47BC}" src="https://github.com/user-attachments/assets/4057b35c-3d94-40e1-ad40-4c7881cf63bc" />


---

## Detektimi dhe Trajtimi i Anomalive / Outlier-ave

### 1. Z-Score në hapësirën PCA

* Llogaritet Z-score për çdo komponent;


 <img width="300" height="44" alt="{00694391-8144-446E-ABEE-5145489967C4}" src="https://github.com/user-attachments/assets/892340ad-b1b7-4db7-a5c8-c3e7510dc3b0" />


* Për secilën observim merret maksimumi i Z-score-ve;


 <img width="197" height="21" alt="{0B93C00D-B7DE-4286-BE41-2C6E6D0320B8}" src="https://github.com/user-attachments/assets/ccb338ab-d01a-40e8-8dbc-a75ce76518e3" />


* Përdoret prag `|Z| < 3.5` për të përcaktuar rreshtat “normalë”;


 <img width="263" height="71" alt="{DF18029F-890D-46DA-913D-13EA75ACB98B}" src="https://github.com/user-attachments/assets/9c7733b1-e825-4ff3-8d88-218563f46a04" />


* Krijohet `df_pca_clean` si variant i pastër i dataset-it në hapësirën PCA.


 <img width="255" height="79" alt="{6CCCB909-81B9-4F4B-8EBF-8B6D64FCEAC3}" src="https://github.com/user-attachments/assets/04acc500-36b5-4c2c-ba32-760f6feb56ec" />


### 2. IQR Clamping në hapësirën origjinale

* Identifikohen kolonat numerike jo-binare me më shumë se 2 vlera unike;


 <img width="386" height="74" alt="{8F1D26A4-0D9C-47E7-87E2-6EB99421D62B}" src="https://github.com/user-attachments/assets/0ef1a70e-5c84-4f8e-825b-1f3e21ade544" />
 <img width="438" height="31" alt="{50740496-FB6F-467D-9B58-AB5083779838}" src="https://github.com/user-attachments/assets/7267073e-6bad-4a34-aa39-b86e746c901b" />


* Për secilën kolonë llogariten Q1, Q3, IQR dhe kufijtë e pranuar;


 <img width="310" height="127" alt="{F61D8CAB-EDB3-4438-95A6-BCE2602F9386}" src="https://github.com/user-attachments/assets/26c28bad-4cbf-4e75-8504-e62876721625" />


* Vlerat jashtë intervalit zëvendësohen me kufijtë përkatës (clamping);


 <img width="434" height="64" alt="{2E233440-A992-487B-857C-5E1262E2F16C}" src="https://github.com/user-attachments/assets/9ea75244-87ea-4640-b609-6d3314c491a6" />


* Raportohet numri i outlier-ave të trajtuar për kolonë dhe në total.


 <img width="321" height="56" alt="{A04B9AB4-EFE5-4898-BB33-6102BE308A54}" src="https://github.com/user-attachments/assets/410c17d5-fb86-4abe-9bc3-9ab58268acfb" />
 <img width="244" height="27" alt="{5A66932F-DCB9-4CDE-BE37-FF925B7CA3F1}" src="https://github.com/user-attachments/assets/2922bbd7-2ac9-44bd-9f63-8f7fdb8241fd" />


Kjo qasje mbron strukturen e dataset-it (asnjë rresht nuk fshihet), duke reduktuar njëkohësisht **ndikimin e vlerave ekstreme**.

---

## Trajtimi i Pabalancimit të Klasave me SMOTE

* Ndahet dataset-i në:

  * `X` – të gjitha kolonat përveç `Severity_binary`;
  * `y` – kolona target `Severity_binary`.



 <img width="223" height="31" alt="{D454CF70-4943-403C-B182-6A5210730689}" src="https://github.com/user-attachments/assets/bfe60eaf-5495-4984-ae99-3be8e3f7719f" />


* Llogaritet shpërndarja e klasave PARA SMOTE;


 <img width="171" height="31" alt="{B6F0F6DA-7AF1-41BB-B7F8-85EF893CA1AE}" src="https://github.com/user-attachments/assets/8a529c06-3bae-47dc-b1c4-0cfaa0f1b378" />


* Aplikohet `SMOTE(random_state=42, k_neighbors=5)`;


  <img width="228" height="26" alt="{8EFE1977-0D75-42AA-8E2A-B4A7EBE06F13}" src="https://github.com/user-attachments/assets/c4de163b-e444-4a0d-ae77-e6e2cc76a9fe" />


* Rikrijohet `df_smote` nga `X_res` dhe `y_res`;


 <img width="263" height="122" alt="{06AFA53B-70A3-46C3-8BA8-CC39D400D058}" src="https://github.com/user-attachments/assets/1b3eb45d-922c-4d42-91bb-ad322d5c142e" />


* Raportohet shpërndarja e klasave PAS SMOTE.


 <img width="170" height="33" alt="{1420AAAE-2782-45D2-AC9C-FD7E49549D8A}" src="https://github.com/user-attachments/assets/6b6f43e4-8ef2-48d1-b823-fcdb01f21389" />


Rezultati: klasat “serioze” (`Severity_binary = 1`) përfaqësohen më mirë, duke balancuar dataset-in për trajnime të mëtejshme.

---

## Vizualizimet dhe Interpretimi i Rezultateve

Pipeline-i gjeneron vizualizime që ndihmojnë në:

1. **Scatterplots PARA/PAS IQR**

   * Pair-e si (`Start_Hour`, `Accident_Count_Last_Week`), (`Distance(mi)`, `Temperature(F)`), (`Start_Lat`, `Start_Lng`);
   * Pikat e clamp-uara shënohen me `IQR_status` për të dalluar outlier-at.


 <img width="1389" height="1535" alt="image" src="https://github.com/user-attachments/assets/09a1ca5a-7207-4839-9f49-c76518e0bbf9" />


2. **Boxplots PARA/PAS IQR**

   * Për variabla si `Distance(mi)`, `Temperature(F)`, `Visibility(mi)`, `Precipitation(in)`, etj.;
   * Demonstrohet vizualisht reduktimi i vlerave ekstreme.

 
 <img width="1490" height="7512" alt="image" src="https://github.com/user-attachments/assets/a9dd53aa-73f7-4534-8bf9-76bc3cc0efcc" />


3. **Barplot për variablat binare PARA/PAS IQR**

   * Proporcioni i vlerave 1 për `Amenity`, `Bump`, `Crossing`, `Rain`, `Is_Weekend`, `Severity_binary`, etj.;
   * Tregohet se IQR clamping nuk ndryshon shpërndarjen e variablave binarë.


     <img width="1770" height="590" alt="image" src="https://github.com/user-attachments/assets/eba33815-2e95-49ae-9caf-48850d2dc2d2" />


4. **Heatmap Atributeve më të lidhura me `Severity_binary`**

   * Seleksionim i top 12 variablave me korrelacion absolut më të madh;
   * Interpretim i lidhjes së tyre me ashpërsinë e aksidenteve.
  

 <img width="929" height="790" alt="image" src="https://github.com/user-attachments/assets/7f7003d2-c3c5-487d-9e06-a1be46bfbd1f" />


5. **Heatmap PARA/PAS IQR**

   * Krahasim i matricës së korrelacionit para dhe pas clamping-ut;
   * Analizë nëse trajtimi i outlier-ave ka ndryshuar marrëdhëniet lineare midis variablave kryesorë.


 <img width="1697" height="734" alt="image" src="https://github.com/user-attachments/assets/36330ccc-4333-40a8-9b77-d81cf3e4c87d" />


---

## Teknologjitë e Përdorura

* **Python 3.13.3**
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
cd PVDH_Gr15_2025
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
