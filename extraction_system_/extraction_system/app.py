"""
Streamlit UI — Extraction + Algebraic Encoding Pipeline.

Run with:  streamlit run app.py
"""

import streamlit as st
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from config import GEMINI_API_KEY, WORLDSPEC_VOCAB
from knowledge_base.kb import list_cached, is_cached, load_or_generate, delete

st.set_page_config(
    page_title="CB Extraction — CASL",
    page_icon="🔬",
    layout="wide",
)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🔬 Extraction Pipeline")
    st.caption("Gemini · MeTTa · CASL")
    st.divider()

    st.subheader("Gemini API Key")
    api_key_input = st.text_input(
        "Key", value=st.session_state.get("api_key", GEMINI_API_KEY or ""),
        type="password", label_visibility="collapsed",
    )
    if api_key_input:
        st.session_state["api_key"] = api_key_input
        os.environ["GEMINI_API_KEY"] = api_key_input

    st.divider()
    st.subheader("Concept Library")
    cached = list_cached()
    if cached:
        st.caption(f"{len(cached)} concepts cached")
        for c in cached:
            col1, col2 = st.columns([5, 1])
            col1.markdown(f"• `{c}`")
            if col2.button("✕", key=f"del_{c}", help=f"Delete '{c}'"):
                delete(c)
                st.rerun()
    else:
        st.caption("Empty — concepts auto-cache on first extraction.")

    st.divider()
    st.subheader("WorldSpec Vocabulary")
    for ws in WORLDSPEC_VOCAB:
        st.markdown(f"<small>• `{ws}`</small>", unsafe_allow_html=True)

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab_run, tab_kb = st.tabs(["🔬  Extract", "📚  Knowledge Base"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Extract
# ══════════════════════════════════════════════════════════════════════════════
with tab_run:
    st.title("Property Extraction + CASL Encoding")
    st.markdown(
        "Enter any two concepts. "
        "If a concept isn't in the library yet, Gemini will profile it automatically "
        "and cache it — no manual KB entry needed."
    )

    cached = list_cached()
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Concept A**")
        ca_text = st.text_input("Concept A", placeholder="e.g. Solar Energy", label_visibility="collapsed")
        if cached:
            ca_pick = st.selectbox("Pick from library", [""] + cached, key="pick_a", label_visibility="collapsed")
            concept_a = ca_text or ca_pick
        else:
            concept_a = ca_text
        if concept_a:
            st.success(f"✓ In library") if is_cached(concept_a) else st.info("Will be auto-profiled")

    with col2:
        st.markdown("**Concept B**")
        cb_text = st.text_input("Concept B", placeholder="e.g. Water Purification", label_visibility="collapsed")
        if cached:
            cb_pick = st.selectbox("Pick from library", [""] + cached, key="pick_b", label_visibility="collapsed")
            concept_b = cb_text or cb_pick
        else:
            concept_b = cb_text
        if concept_b:
            st.success(f"✓ In library") if is_cached(concept_b) else st.info("Will be auto-profiled")

    api_key = st.session_state.get("api_key", "") or GEMINI_API_KEY or ""
    can_run = bool(concept_a and concept_b and api_key)
    run_btn = st.button("🔬  Extract & Encode", type="primary", disabled=not can_run)
    if not api_key:
        st.warning("Add your Gemini API key in the sidebar.")

    if run_btn:
        from pipeline import run
        with st.spinner(f"Extracting '{concept_a}' and '{concept_b}' in parallel…"):
            try:
                result = run(concept_a, concept_b)
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()

        st.success("✓ Extraction complete")
        st.rerun()

        for key, label in [("concept_a", concept_a), ("concept_b", concept_b)]:
            r = result[key]
            st.divider()
            st.subheader(f"📄 {label}")

            # ── CASL ──
            st.markdown("**CASL Algebraic Representation**")
            st.code(r["casl"], language="lisp")

            # ── Properties table ──
            st.markdown("**Extracted Properties**")
            props = r["json"]["V_predicate"]["Property"]
            for p in props:
                ws_str = " · ".join(f"`{w}`" for w in p["WorldSpecSet"]) if p["WorldSpecSet"] else "*empty set*"
                with st.expander(f"`{p['name']}` — {p['degree']}  ({p['centrality']:.2f})"):
                    st.markdown(f"**WorldSpecSet:** {ws_str}")
                    st.markdown(f"**Description:** {p['description']}")

            # ── MeTTa ──
            with st.expander("MeTTa Atoms"):
                st.code(r["metta"], language="text")

            # ── Downloads ──
            dc1, dc2, dc3 = st.columns(3)
            safe = label.replace(" ", "_")
            dc1.download_button(f"CASL",  r["casl"],  file_name=f"{safe}.casl",  mime="text/plain",        key=f"dl_casl_{key}")
            dc2.download_button(f"MeTTa", r["metta"], file_name=f"{safe}.metta", mime="text/plain",        key=f"dl_metta_{key}")
            dc3.download_button(f"JSON",  json.dumps(r["json"], indent=2), file_name=f"{safe}.json", mime="application/json", key=f"dl_json_{key}")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — Knowledge Base
# ══════════════════════════════════════════════════════════════════════════════
with tab_kb:
    st.title("Knowledge Base")
    st.markdown(
        "Concepts are **auto-cached** after first extraction. "
        "You can also pre-generate an entry for any concept here."
    )

    api_key = st.session_state.get("api_key", "") or GEMINI_API_KEY or ""

    # ── Add concept ──────────────────────────────────────────────────────────
    st.subheader("Add a concept")
    col_i, col_b = st.columns([4, 1])
    new_c = col_i.text_input("Concept name", placeholder="e.g. Quantum Computing", label_visibility="collapsed")
    add_btn = col_b.button("Generate & save", disabled=not (new_c and api_key))

    if add_btn and new_c:
        if is_cached(new_c):
            st.info(f"'{new_c}' is already cached.")
        else:
            with st.spinner(f"Profiling '{new_c}'…"):
                try:
                    data = load_or_generate(new_c)
                    st.success(f"✓ '{new_c}' saved to library")
                    st.json(data)
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed: {e}")

    st.divider()

    # ── Browse ───────────────────────────────────────────────────────────────
    st.subheader("Browse library")
    cached = list_cached()
    if not cached:
        st.caption("Empty. Run an extraction or add a concept above.")
    else:
        search = st.text_input("Search", placeholder="Filter…", label_visibility="collapsed")
        filtered = [c for c in cached if search.lower() in c.lower()] if search else cached
        st.caption(f"{len(filtered)} of {len(cached)}")

        for c in filtered:
            with st.expander(f"**{c}**"):
                from knowledge_base.kb import _path
                import json as _json
                try:
                    with open(_path(c)) as f:
                        raw = _json.load(f)
                except Exception:
                    raw = {}

                if raw:
                    st.markdown(f"**Description:** {raw.get('description','—')}")
                    ws = raw.get("world_specs", [])
                    st.markdown("**WorldSpecs:** " + " ".join(f"`{w}`" for w in ws))
                    rels = raw.get("relations", {})
                    for rel, items in rels.items():
                        if items:
                            st.markdown(f"*{rel}*: {', '.join(str(i) for i in items)}")

                col_d, col_r = st.columns(2)
                if col_d.button("Delete", key=f"del2_{c}"):
                    delete(c)
                    st.rerun()
                if col_r.button("Regenerate", key=f"regen_{c}", disabled=not api_key):
                    delete(c)
                    with st.spinner(f"Regenerating '{c}'…"):
                        try:
                            load_or_generate(c)
                            st.success("Done!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Failed: {e}")
