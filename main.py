import streamlit as st
from docxtpl import DocxTemplate
import os
from datetime import date
import tempfile

# Path
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "generated_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.set_page_config(layout="centered")
st.title("📄 Aplikasi Pembuat Dokumen Otomatis")

# =========================
# PILIH TEMPLATE DOKUMEN
# =========================
jenis_dokumen = st.selectbox("Pilih jenis dokumen:", ["Surat Peringatan", "Surat Penawaran Harga"])

# =========================
# FORM SURAT PERINGATAN
# =========================
if jenis_dokumen == "Surat Peringatan":
    st.header("📌 Formulir Surat Peringatan")
    with st.form("form_sp"):
        no_sp = st.text_input("Nomor Surat", value="01")
        peringatan_sp = st.selectbox("Peringatan ke-", ["1", "2", "3"])
        nama_karyawan = st.text_input("Nama Karyawan")
        jabatan = st.text_input("Jabatan")
        isi_penilaian_kinerja_yang_dilanggar = st.text_area("Isi pelanggaran")
        isi_akibat_dari_tindakan_pelanggaran = st.text_area("Akibat pelanggaran")
        perintah_sp = st.text_input("Jenis SP", value="SP-2")
        surat_peringatan_berikutnya = st.text_input("Surat Peringatan Berikutnya", value="SP-3")
        tanggal_surat = st.date_input("Tanggal", value=date.today())
        nama_saksi = st.text_input("Nama Saksi")
        jabatan_saksi = st.text_input("Jabatan Saksi")
        generate = st.form_submit_button("Buat Surat")

    if generate:
        doc = DocxTemplate(os.path.join(TEMPLATE_DIR, "FORM_SP_template.docx"))
        context = {
            "no_sp": no_sp,
            "peringatan_sp": peringatan_sp,
            "nama_karyawan": nama_karyawan,
            "jabatan": jabatan,
            "isi_penilaian_kinerja_yang_dilanggar": isi_penilaian_kinerja_yang_dilanggar,
            "isi_akibat_dari_tindakan_pelanggaran": isi_akibat_dari_tindakan_pelanggaran ,
            "perintah_sp": perintah_sp,
            "surat_peringatan_berikutnya": surat_peringatan_berikutnya,
            "tanggal_surat": tanggal_surat.strftime("%d %B %Y"),
            "nama_saksi": nama_saksi,
            "jabatan_saksi": jabatan_saksi,
        }
        filename = f"SP_{nama_karyawan.replace(' ', '_')}_ke{peringatan_sp}.docx"
        filepath = os.path.join(OUTPUT_DIR, filename)
        doc.render(context)
        doc.save(filepath)
        st.success("✅ Surat berhasil dibuat dan siap diunduh.")

        with open(filepath, "rb") as f:
            st.download_button("📥 Download Word", f, file_name=filename)


# =========================
# FORM SURAT PENAWARAN HARGA
# =========================
elif jenis_dokumen == "Surat Penawaran Harga":
    st.header("📌 Formulir Surat Penawaran Harga")
    with st.form("form_penawaran"):
        no_surat = st.text_input("No. Surat", value="[Surat ke-]/01/003/[Bulan(Romawi)]/2025/ADM/SPH	")
        nama_perusahaan = st.text_input("Nama Perusahaan Tujuan")
        lokasi_perusahaan = st.text_input("Lokasi Perusahaan")
        nama_up = st.text_input("Nama UP / Contact Person")
        tanggal_surat = st.date_input("Tanggal Surat", value=date.today())
        generate = st.form_submit_button("Buat Surat")

    if generate:
        doc = DocxTemplate(os.path.join(TEMPLATE_DIR, "template_surat_penawaran_harga.docx"))
        context = {
            "no_surat": no_surat,
            "nama_perusahaan": nama_perusahaan,
            "lokasi_perusahaan": lokasi_perusahaan,
            "nama_up": nama_up,
            "tanggal_surat": tanggal_surat.strftime("%d %B %Y")
        }
        filename = f"Penawaran_{nama_perusahaan.replace(' ', '_')}.docx"
        filepath = os.path.join(OUTPUT_DIR, filename)
        doc.render(context)
        doc.save(filepath)
        st.success("✅ Surat penawaran berhasil dibuat!")

        with open(filepath, "rb") as f:
            st.download_button("📥 Download Word", f, file_name=filename)

