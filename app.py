import os
import numpy as np
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


st.set_page_config(
    page_title="US Accidents – Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚦 US Accidents – Dashboard")
st.caption("Analizë e datasetit US Accidents")


RAW_PATH = "Datasets/Week3_Dataset.csv" 
AFTER_PATH = "Datasets/finalizedds.csv"    



@st.cache_data(show_spinner=False)
def read_csv_path(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def numeric_cols(df: pd.DataFrame) -> list[str]:
    return df.select_dtypes(include=[np.number]).columns.tolist()


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    ms = df.isna().sum().to_frame("missing_count")
    ms["missing_pct"] = (ms["missing_count"] / len(df) * 100).round(2)
    return ms.sort_values(["missing_count", "missing_pct"], ascending=False)


def iqr_outlier_count(series: pd.Series) -> int:
    s = pd.to_numeric(series, errors="coerce").dropna()
    if s.empty:
        return 0
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    if iqr == 0:
        return 0
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return int(((s < lower) | (s > upper)).sum())


def download_button(df: pd.DataFrame, filename: str, label: str):
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    st.download_button(label=label, data=csv_bytes, file_name=filename, mime="text/csv")


def safe_to_datetime(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce", utc=False)


def ensure_time_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Hour
    if "Hour" not in out.columns:
        if "Start_Hour" in out.columns:
            out["Hour"] = pd.to_numeric(out["Start_Hour"], errors="coerce")
        elif "Start_Time" in out.columns:
            dt = safe_to_datetime(out["Start_Time"])
            if dt.notna().any():
                out["Hour"] = dt.dt.hour

    # Weekday
    if "Weekday" not in out.columns and "Start_Time" in out.columns:
        dt = safe_to_datetime(out["Start_Time"])
        if dt.notna().any():
            out["Weekday"] = dt.dt.day_name()

    # Month
    if "Month" not in out.columns:
        if "Start_Month" in out.columns:
            m = pd.to_numeric(out["Start_Month"], errors="coerce")
            out["Month"] = m.map(
                {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
            )
        elif "Start_Time" in out.columns:
            dt = safe_to_datetime(out["Start_Time"])
            if dt.notna().any():
                out["Month"] = dt.dt.month_name()

    return out


def add_day_night_bucket(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "Day_Night" not in out.columns and "Hour" in out.columns:
        h = pd.to_numeric(out["Hour"], errors="coerce")
        out["Day_Night"] = np.where((h >= 20) | (h <= 5), "Night", "Day")
    return out


def preprocess_minimal(df: pd.DataFrame, severe_threshold: int = 3) -> pd.DataFrame:

    out = df.copy()

    out = ensure_time_features(out)
    out = add_day_night_bucket(out)

    if "Severity_binary" not in out.columns and "Severity" in out.columns:
        sev = pd.to_numeric(out["Severity"], errors="coerce")
        out["Severity_binary"] = np.where(sev >= severe_threshold, 1, 0)

    if "Weather_Condition" in out.columns:
        out["Weather_Condition"] = out["Weather_Condition"].fillna("Unknown").astype(str)
    elif "Weather" in out.columns:
        out["Weather"] = out["Weather"].fillna("Unknown").astype(str)

    if "State" in out.columns:
        out["State"] = out["State"].astype(str).str.upper().str.strip()

    return out


def build_cat_candidates(df: pd.DataFrame) -> list[str]:
    cats = df.select_dtypes(include=["object", "category"]).columns.tolist()
    for c in df.select_dtypes(include=[np.number]).columns:
        nunique = int(df[c].nunique(dropna=True))
        if 2 <= nunique <= 60 and c not in cats:
            cats.append(c)

    preferred_order = ["Hour", "Weather_Condition", "Weather", "Day_Night", "Weekday", "Month", "State"]
    preferred = [c for c in preferred_order if c in cats]
    rest = [c for c in cats if c not in preferred]
    return preferred + rest


def common_numeric_columns(df1: pd.DataFrame, df2: pd.DataFrame) -> list[str]:
    n1 = set(numeric_cols(df1))
    n2 = set(numeric_cols(df2))
    return sorted(list(n1.intersection(n2)))


def safe_rate(num: float, den: float) -> float:
    return float(num) / float(den) if den else float("nan")


if not os.path.exists(RAW_PATH):
    st.error(f"file not found `{RAW_PATH}`. Vendose në folderin e projektit.")
    st.stop()

if not os.path.exists(AFTER_PATH):
    st.error(f"file not found `{AFTER_PATH}`. Vendose në folderin e projektit.")
    st.stop()

st.sidebar.header("Settings")
severe_threshold = st.sidebar.selectbox("Severity threshold → Severity_binary", options=[2, 3, 4], index=1)

df_raw = read_csv_path(RAW_PATH)
df_after = read_csv_path(AFTER_PATH)

df_main = preprocess_minimal(df_raw, severe_threshold=severe_threshold)           
df_before_proc = preprocess_minimal(df_raw, severe_threshold=severe_threshold)    
df_after_proc = preprocess_minimal(df_after, severe_threshold=severe_threshold)   


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
st.sidebar.header("📊 Navigimi")
section = st.sidebar.radio(
    "Zgjidh faqen:",
    [
        "Overview",
        "KPI Dashboard",
        "Risk Profile",
        "US States Map",
        "Severity & Correlations",
        "PCA Impact",
        "Comparison: Dataset Overview",
        "Comparison: Missing Values",
        "Comparison: Distributions",
        "Comparison: Outliers"
    ]
)


# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------
if section == "Overview":
    st.subheader("📌 Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", df_after_proc.shape[0])
    c2.metric("Columns", df_after_proc.shape[1])
    c3.metric("Missing (total)", int(df_after_proc.isna().sum().sum()))
    c4.metric("Severity_binary", "Yes" if "Severity_binary" in df_after_proc.columns else "No")

    with st.expander("Shiko sample (head)"):
        st.dataframe(df_after_proc.head(25), use_container_width=True)



elif section == "KPI Dashboard":
    st.subheader("📈 KPI Dashboard")
    st.caption("Pikat kryesore (numra) të nxjerra prej datasetit.")

    total = int(len(df_after_proc))
    missing_total = int(df_after_proc.isna().sum().sum())
    missing_rate = safe_rate(missing_total, total * max(1, df_after_proc.shape[1]))

    has_sev_bin = "Severity_binary" in df_after_proc.columns
    if has_sev_bin:
        sev_bin = pd.to_numeric(df_after_proc["Severity_binary"], errors="coerce")
        severe_n = int((sev_bin == 1).sum())
        severe_rate = safe_rate(severe_n, int(sev_bin.notna().sum()))
    else:
        severe_n, severe_rate = None, None

    has_state = "State" in df_main.columns
    if has_state:
        st_series = df_main["State"].dropna().astype(str).str.upper().str.strip()
        unique_states = int(st_series.nunique())
        top_state = st_series.value_counts().idxmax() if not st_series.empty else None
        top_state_n = int(st_series.value_counts().iloc[0]) if not st_series.empty else 0
    else:
        unique_states, top_state, top_state_n = None, None, None

    weather_col = "Weather_Condition" if "Weather_Condition" in df_main.columns else ("Weather" if "Weather" in df_main.columns else None)
    if weather_col:
        w = df_main[weather_col].dropna().astype(str)
        top_weather = w.value_counts().idxmax() if not w.empty else None
        top_weather_n = int(w.value_counts().iloc[0]) if not w.empty else 0
    else:
        top_weather, top_weather_n = None, None

    if "Day_Night" in df_main.columns:
        dn = df_main["Day_Night"].dropna().astype(str)
        night_share = safe_rate(int((dn == "Night").sum()), int(dn.notna().sum()))
    else:
        night_share = None

    date_range = None
    if "Start_Time" in df_main.columns:
        dt = safe_to_datetime(df_main["Start_Time"])
        if dt.notna().any():
            date_range = (dt.min(), dt.max())

    risky_hour = None
    risky_hour_rate = None
    if has_sev_bin and "Hour" in df_main.columns:
        tmp = df_main[["Hour", "Severity_binary"]].copy()
        tmp["Hour"] = pd.to_numeric(tmp["Hour"], errors="coerce")
        tmp["Severity_binary"] = pd.to_numeric(tmp["Severity_binary"], errors="coerce")
        tmp = tmp.dropna(subset=["Hour", "Severity_binary"])
        if not tmp.empty:
            by_hour = tmp.groupby("Hour")["Severity_binary"].mean().sort_values(ascending=False)
            risky_hour = int(by_hour.index[0])
            risky_hour_rate = float(by_hour.iloc[0])

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    r1c1.metric("Total accidents", f"{total:,}")
    r1c2.metric("Missing cells", f"{missing_total:,}")
    r1c3.metric("Missing rate", "—" if np.isnan(missing_rate) else f"{missing_rate:.2%}")
    r1c4.metric("Unique states", "—" if unique_states is None else f"{unique_states}")

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    r2c1.metric("Severe accidents", "—" if severe_n is None else f"{severe_n:,}")
    r2c2.metric("Severe rate", "—" if severe_rate is None or np.isnan(severe_rate) else f"{severe_rate:.2%}")
    r2c3.metric("Top state", "—" if top_state is None else f"{top_state} ({top_state_n:,})")
    r2c4.metric("Top weather", "—" if top_weather is None else f"{top_weather} ({top_weather_n:,})")

    r3c1, r3c2, r3c3, r3c4 = st.columns(4)
    r3c1.metric("Night share", "—" if night_share is None or np.isnan(night_share) else f"{night_share:.2%}")
    if date_range:
        r3c2.metric("Start date", str(pd.to_datetime(date_range[0]).date()))
        r3c3.metric("End date", str(pd.to_datetime(date_range[1]).date()))
    else:
        r3c2.metric("Start date", "—")
        r3c3.metric("End date", "—")

    if risky_hour is not None and risky_hour_rate is not None:
        r3c4.metric("Most risky hour", f"{risky_hour}:00 (~{risky_hour_rate:.2%})")
    else:
        r3c4.metric("Most risky hour", "—")

    with st.expander("Charts"):
        if "Hour" in df_main.columns:
            hh = pd.to_numeric(df_main["Hour"], errors="coerce").dropna()
            if not hh.empty:
                cnt = hh.value_counts().sort_index().reset_index()
                cnt.columns = ["Hour", "Accidents"]
                st.plotly_chart(px.bar(cnt, x="Hour", y="Accidents", title="Accidents by Hour"), use_container_width=True)

        if has_state:
            st_series = df_main["State"].dropna().astype(str).str.upper().str.strip()
            if not st_series.empty:
                top = st_series.value_counts().head(15).reset_index()
                top.columns = ["State", "Accidents"]
                st.plotly_chart(px.bar(top, x="Accidents", y="State", orientation="h", title="Top 15 States (Accidents)"),
                                use_container_width=True)


elif section == "Risk Profile":
    st.subheader("🧭 Risk Profile")
    st.caption("Zgjedh dimensione (dropdown) dhe shiko risk-un + top kombinimet.")

    num_cols = numeric_cols(df_main)
    if not num_cols:
        st.warning("Nuk ka kolona numerike për risk.")
        st.stop()

    default_target = "Severity_binary" if "Severity_binary" in num_cols else num_cols[0]
    target = st.selectbox("Target për risk", options=num_cols, index=num_cols.index(default_target))

    cat_candidates = build_cat_candidates(df_main)
    if not cat_candidates:
        st.warning("S’po gjej kolona kategorike/low-cardinality për dropdown.")
        st.stop()

    st.markdown("### 1) Zgjedh dimensionet")
    default_dims = [c for c in ["Hour", "Weather_Condition", "Day_Night"] if c in cat_candidates][:2]
    if not default_dims:
        default_dims = [cat_candidates[0]]

    dims = st.multiselect("Dimensionet (rekomando 1–3):", options=cat_candidates, default=default_dims)
    if not dims:
        st.stop()

    st.markdown("### 2) Filtro vlerat (opsionale)")
    filters = {}
    cols = st.columns(min(3, len(dims)))
    for i, d in enumerate(dims):
        with cols[i % len(cols)]:
            vals = df_main[d].dropna().unique().tolist()
            if d == "Hour":
                try:
                    vals = sorted([int(v) for v in vals])
                except Exception:
                    vals = sorted(vals)
            else:
                try:
                    vals = sorted(vals)
                except Exception:
                    pass
                vals = vals[:200]
            filters[d] = st.selectbox(d, options=["(Any)"] + vals)

    mask = pd.Series(True, index=df_main.index)
    for d, v in filters.items():
        if v != "(Any)":
            mask &= (df_main[d] == v)

    sub = df_main.loc[mask, dims + [target]].copy()
    sub[target] = pd.to_numeric(sub[target], errors="coerce")

    overall = pd.to_numeric(df_main[target], errors="coerce")
    overall_mean = float(overall.mean(skipna=True))
    sub_mean = float(sub[target].mean(skipna=True)) if len(sub) else float("nan")
    sub_n = int(sub[target].notna().sum())

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Overall risk (mean)", f"{overall_mean:.4f}")
    c2.metric("Selected risk (mean)", "—" if np.isnan(sub_mean) else f"{sub_mean:.4f}")
    c3.metric("Δ vs overall", "—" if np.isnan(sub_mean) else f"{(sub_mean - overall_mean):+.4f}")
    c4.metric("N (selected)", sub_n)

    if sub_n == 0:
        st.warning("Nuk ka data për këtë kombinim/filtrim.")
        st.stop()
    if sub_n < 50:
        st.warning("Kujdes: N i vogël → risk-u mund të jetë i paqëndrueshëm.")

    if target == "Severity_binary":
        st.info(f"Risk(mean) ≈ probabiliteti i severity=1 në subset (~{sub_mean:.2%}).")

    st.markdown("### 3) Distribution në subset")
    st.plotly_chart(px.histogram(sub.dropna(subset=[target]), x=target, nbins=30, title="Target distribution (subset)"),
                    use_container_width=True)

    st.markdown("###Top kombinimet më të rrezikshme")
    min_support = st.slider("Minimum support (N) për kombinim", 20, 500, 80, 10)

    grp = df_main[dims + [target]].copy()
    grp[target] = pd.to_numeric(grp[target], errors="coerce")
    grp = grp.dropna(subset=[target])

    stats = (
        grp.groupby(dims, dropna=True)
        .agg(n=(target, "count"), risk_mean=(target, "mean"))
        .reset_index()
    )
    stats = stats[stats["n"] >= min_support].sort_values("risk_mean", ascending=False).head(50)

    if stats.empty:
        st.warning("Nuk ka kombinime që plotësojnë minimumin e support. Ule slider-in.")
        st.stop()

    st.dataframe(stats, use_container_width=True)

    top15 = stats.head(15).copy()
    top15["combo"] = top15[dims].astype(str).agg(" | ".join, axis=1)
    st.plotly_chart(px.bar(top15, x="risk_mean", y="combo", orientation="h", title="Top 15 kombinime (risk_mean)"),
                    use_container_width=True)



elif section == "US States Map":
    st.subheader("🗺️ US States – Harta e aksidenteve")
    st.caption("Choropleth (numri i aksidenteve për shtet). Opsionale: pika në hartë nëse ka koordinata.")

    if "State" not in df_main.columns:
        st.warning("Kolona mungon ne datataset")
        st.stop()

    states = df_main["State"].dropna().astype(str).str.upper().str.strip()
    counts = states.value_counts().reset_index()
    counts.columns = ["State", "Accidents"]

    c1, c2 = st.columns(2)
    c1.metric("Shtete unike", counts.shape[0])

    fig = px.choropleth(
        counts,
        locations="State",
        locationmode="USA-states",
        color="Accidents",
        scope="usa",
        title="Accidents by US State (count)"
    )
    st.plotly_chart(fig, use_container_width=True)

    if {"Start_Lat", "Start_Lng"}.issubset(df_main.columns):
        st.markdown("### Pikat në hartë (sample)")
        sample_n = st.slider("Sa pika me shfaq (sample)", 1000, 30000, 5000, 1000)
        d = df_main[["Start_Lat", "Start_Lng", "State"]].copy()
        d["Start_Lat"] = pd.to_numeric(d["Start_Lat"], errors="coerce")
        d["Start_Lng"] = pd.to_numeric(d["Start_Lng"], errors="coerce")
        d = d.dropna(subset=["Start_Lat", "Start_Lng"])
        if d.empty:
            st.info("Nuk ka koordinata valide për pika.")
        else:
            d = d.sample(n=min(sample_n, len(d)), random_state=42)
            fig2 = px.scatter_geo(
                d,
                lat="Start_Lat",
                lon="Start_Lng",
                scope="usa",
                opacity=0.35,
                title="Accident points (sample)"
            )
            st.plotly_chart(fig2, use_container_width=True)



elif section == "Severity & Correlations":
    st.subheader("🔥 Correlations (numeric only)")

    num_cols = numeric_cols(df_main)
    if len(num_cols) < 2:
        st.warning("Duhet të paktën 2 kolona numerike.")
        st.stop()

    target = "Severity_binary" if "Severity_binary" in num_cols else num_cols[0]
    corr = df_main[num_cols].corr(numeric_only=True)

    top_k = st.slider("Top K features", 5, 30, 12, 1)
    top = corr[target].abs().sort_values(ascending=False).head(top_k).index.tolist()

    heat = corr.loc[top, top]
    st.plotly_chart(px.imshow(heat, title=f"Top {top_k} features lidhur me {target}", aspect="auto"),
                    use_container_width=True)

    tbl = corr[target].sort_values(key=lambda s: s.abs(), ascending=False).head(top_k).to_frame(f"corr_with_{target}")
    st.dataframe(tbl, use_container_width=True)



elif section == "PCA Impact":
    st.subheader("📉 PCA")

    num_df = df_main.select_dtypes(include=[np.number]).dropna()
    if num_df.shape[1] < 2:
        st.warning("Duhet të paktën 2 kolona numerike për PCA.")
        st.stop()

    variance_target = st.slider("Explained variance target", 0.80, 0.99, 0.95, 0.01)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(num_df)

    pca = PCA(n_components=variance_target)
    X_pca = pca.fit_transform(X_scaled)

    c1, c2 = st.columns(2)
    c1.metric("Original features", X_scaled.shape[1])
    c2.metric("PCA components", X_pca.shape[1])

    cum = np.cumsum(pca.explained_variance_ratio_)
    fig = px.line(x=list(range(1, len(cum) + 1)), y=cum, markers=True, title="Cumulative Explained Variance")
    fig.update_xaxes(title="Components")
    fig.update_yaxes(title="Explained variance (cumulative)")
    st.plotly_chart(fig, use_container_width=True)

    if X_pca.shape[1] >= 2:
        pca_df = pd.DataFrame(X_pca[:, :2], columns=["PC1", "PC2"])
        st.plotly_chart(px.scatter(pca_df, x="PC1", y="PC2", title="PCA Scatter (PC1 vs PC2)", opacity=0.6),
                        use_container_width=True)



elif section == "Comparison: Dataset Overview":
    st.subheader("📂 Comparison – Dataset Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔴 RAW (Week3_Dataset)")
        st.write(f"Shape: {df_before_proc.shape[0]} × {df_before_proc.shape[1]}")
        st.write(f"Missing: {int(df_before_proc.isna().sum().sum())}")
        st.dataframe(df_before_proc.head(15), use_container_width=True)
    with col2:
        st.markdown("### 🟢 Finalized (finalizedds)")
        st.write(f"Shape: {df_after_proc.shape[0]} × {df_after_proc.shape[1]}")
        st.write(f"Missing: {int(df_after_proc.isna().sum().sum())}")
        st.dataframe(df_after_proc.head(15), use_container_width=True)


elif section == "Comparison: Missing Values":
    st.subheader("Comparison – Missing Values")

    ms_before = missing_summary(df_before_proc)
    ms_after = missing_summary(df_after_proc)

    left, right = st.columns(2)
    with left:
        st.markdown("### RAW")
        top = ms_before[ms_before["missing_count"] > 0].head(20).reset_index().rename(columns={"index": "column"})
        if top.empty:
            st.success("Nuk ka missing values.")
        else:
            st.dataframe(top, use_container_width=True)
            st.plotly_chart(px.bar(top, x="missing_pct", y="column", orientation="h", title="Missing % (Top 20)"),
                            use_container_width=True)
    with right:
        st.markdown("### Finalized")
        top = ms_after[ms_after["missing_count"] > 0].head(20).reset_index().rename(columns={"index": "column"})
        if top.empty:
            st.success("Nuk ka missing values.")
        else:
            st.dataframe(top, use_container_width=True)
            st.plotly_chart(px.bar(top, x="missing_pct", y="column", orientation="h", title="Missing % (Top 20)"),
                            use_container_width=True)


elif section == "Comparison: Distributions":
    st.subheader(" Comparison – Distributions")

    common_num = common_numeric_columns(df_before_proc, df_after_proc)
    if not common_num:
        st.warning("Nuk ka kolona numerike të përbashkëta.")
        st.stop()

    feature = st.selectbox("Zgjidh atribut numerik:", common_num)
    log_scale = st.checkbox("Log scale (log10, vetëm për >0)", value=False)

    b = pd.to_numeric(df_before_proc[feature], errors="coerce")
    a = pd.to_numeric(df_after_proc[feature], errors="coerce")

    if log_scale:
        b = np.log10(b[b > 0])
        a = np.log10(a[a > 0])

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(b.dropna(), nbins=50, title="RAW", marginal="box"), use_container_width=True)
    with col2:
        st.plotly_chart(px.histogram(a.dropna(), nbins=50, title="Finalized", marginal="box"), use_container_width=True)


elif section == "Comparison: Outliers":
    st.subheader(" Comparison – Outliers (IQR)")

    common_num = common_numeric_columns(df_before_proc, df_after_proc)
    if not common_num:
        st.warning("Nuk ka kolona numerike të përbashkëta.")
        st.stop()

    feature = st.selectbox("Zgjidh atribut:", common_num)

    out_b = iqr_outlier_count(df_before_proc[feature])
    out_a = iqr_outlier_count(df_after_proc[feature])

    c1, c2 = st.columns(2)
    c1.metric("Outliers (RAW)", out_b)
    c2.metric("Outliers (Finalized)", out_a)

    fig = go.Figure()
    fig.add_trace(go.Box(y=pd.to_numeric(df_before_proc[feature], errors="coerce"), name="RAW"))
    fig.add_trace(go.Box(y=pd.to_numeric(df_after_proc[feature], errors="coerce"), name="Finalized"))
    fig.update_layout(title=f"Boxplot: {feature}")
    st.plotly_chart(fig, use_container_width=True)


