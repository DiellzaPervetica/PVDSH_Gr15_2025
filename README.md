# PVDSH_Gr15_2025
US Accidents (2016 - 2023)


#  Analiza e te dhenave – US Accidents Dataset

## Hyrje

Ky projekt paraqet nje analize te detajuar te datasetit US Accidents (2016–2023), i cili permban mbi 7 milion raste aksidentesh ne Shtetet e Bashkuara. Te dhenat jane mbledhur nga API-te publike te trafikut, sensoret rrugore dhe burime te tjera te transportit**. Qellimi kryesor eshte te pergatitet dataset-i per perdorim ne analiza statistikore dhe modelim me algoritme te Machine Learning, duke kaluar ne menyre sistematike neper fazat e paraperpunimit, pastrimit, transformimit dhe reduktimit te dimensioneve.
Permes ketij procesi jane trajtuar vlerat e munguar, duplikimet, transformimi i tipeve te te dhenave, si dhe krijimi i vecorive te reja per analize te avancuar te faktoreve qe ndikojne ne ashpersine e aksidenteve.


## Mbledhja dhe pershkrimi i te dhenave

* Dataset-i eshte marre nga [Kaggle – US Accidents (Sobhan Moosavi)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents).
* Te dhenat perfshijne koordinatat gjeografike, kushtet e motit, koha e ndodhjes, vrazhdesia e aksidentit dhe shume karakteristika te tjera kontekstuale.
* Pas importimit u perdor `pandas` per inspektim fillestar te formes (`df.shape`), tipeve te kolonave (`df.info()`) dhe vlerave qe mungojne (`df.isnull().sum()`).


## Definimi i tipeve te te dhenave dhe cilesia e tyre

* Kolonat `Start_Time` dhe `End_Time` u konvertuan ne tipe `datetime`.
* U shtuan kolonat e zberthyera: `Start_Day`, `Start_Month`, `Start_Year`, `Start_Hour`, `End_Day`, etj., per lehtesi ne analize kohore.
* Kontroll i duplikateve me `df.duplicated()` dhe heqja e tyre per te siguruar integritetin e te dhenave.
* Cilesia e te dhenave u vleresua permes identifikimit te simboleve jo te vlefshme (`?`, `-`, `NA`, etj.) dhe uniformizimit te formatimit tekstual.


## Integrimi dhe agregimi i te dhenave

* Dataseti u integrua me tabelen e datave te zberthyera per te formuar nje strukture te vetme (`df_merged`).
* Jane kryer dy forma agregimi:

  * Sipas ores: numri dhe vrazhdesia mesatare e aksidenteve (`groupby('Start_Hour')`).
  * Sipas kushteve te motit: per te analizuar ndikimin e motit ne frekuencen dhe ashpersine e ngjarjeve.
* Rezultatet u eksportuan ne skedaret ndermjetes (`Week2_Dataset.csv`, `Week3_Dataset.csv`) per cdo faze te analizes.


## Pastrimi i te dhenave dhe trajtimi i vlerave te munguar

* Kolonat me me shume se 50% mungesa u eliminuan.
* Vlerat munguar ne kolonat numerike u zevendesuan me medianen**, ndersa ne ato kategorike me moden.
* Per kolonat kohore (`Start_Time`, `End_Time`, `Weather_Timestamp`) u aplikua nje strategji e personalizuar:

  * Zevendesimi i datave te munguar me medianen ose me kohezgjatjen mesatare te ngjarjeve.
  * Uniformizimi i formateve te dates ne te gjitha kolonat kohore.


## Krijimi dhe perzgjedhja e vecorive 

* Jane krijuar vecori te reja per analize kohore:

  * `Hour`, `Day`, `Month`, `Weekday`, `Is_Weekend`, `Season`.
* U ndertuan dy vecori te avancuara per analize te frekuences:

  * `Accident_Count_Last_Week` – numri i aksidenteve gjate 7 diteve te fundit.
  * `Accidents_Per_Day_Avg` – mesatarja ditore e aksidenteve per cdo qytet ose zone.
* Perzgjedhja e kolonave relevante u be permes metodes `SelectKBest` me testin `f_classif` per atributet numerike.


## Diskretizimi dhe binarizimi

* Per kolonat numerike me me shume se 4 vlera unike, u aplikua diskretizimi ne 4 intervale duke perdorur `KBinsDiscretizer` (strategjia quantile).
* Kolona `Severity` u shnderrua ne nje variabel binare (`Severity_binary`), ku vlerat ≥3 u koduan si 1 (aksidente te renda).
* Kolonat kategorike (`Sunrise_Sunset`, `Twilight`, `Season`, etj.) u binarizuan** permes `pd.get_dummies()` me `drop_first=True` per te shmangur multikollinearitetin.


## Transformimi, scaling dhe normalizimi

* Kolonat numerike u ndane ne tre grupe:

  * Scaling columns – me shume vlera numerike → `StandardScaler`.
  * Normalization columns – per vlera me shperndarje te ndryshme → `Normalizer(norm='l2')`.
  * Binary columns – per vlera booleane (`True/False`) te konvertuara ne (0/1).
* Kolonat tekstuale (`State`, `County`, `Weather_Condition`, etj.) u koduan permes `LabelEncoder` dhe `One-Hot Encoding`.
* U eksportua dataseti final i transformuar (`Week4_transformed_final2.csv`).


## Reduktimi i dimensionit me PCA

* U aplikua Principal Component Analysis (PCA) pas standardizimit te te dhenave.
* Varianca e shpjeguar totale ishte mbi 95%, duke reduktuar numrin e kolonave ne nje nensheshje me efikase per modelim.
* Rezultatet u ruajten ne `Week4_PCA.csv` dhe u vizualizuan permes grafikut te variances per cdo komponent.


## Rezultatet kryesore te pergatitjes

* Dataseti fillestar: mbi 7 milion rreshta dhe 47+ kolona.
* Pas pastrimit, diskretizimit dhe transformimeve: dataset kompakt dhe uniform per analiza te avancuara.
* Gjithsej jane pergatitur disa versione te datasetit (`Week2`, `Week3`, `Week4`, `PCA`) per gjurmueshmeri te plote te fazave te procesit.


## Perfundim

Ky projekt demonstron nje cikel te plote te para-procesimit te te dhenave duke perfshire integrimin, pastrimin, trajtimin e mungesave, krijimin e vecorive te reja, diskretizimin, binarizimin, transformimin dhe reduktimin e dimensioneve.
Rezultati perfundimtar eshte nje dataset i gatshem per analiza eksploruese, qe mund te perdoret ne fazat e ardhshme te projektit per analizen e ashpersise se aksidenteve.


