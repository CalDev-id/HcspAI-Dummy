# from LLM.groq_runtime import GroqRunTime

# class ChatBot:

#     def __init__(self):
#         self.runtime = GroqRunTime()

#     def generate_response(self, user_prompt):
#         groq_run = GroqRunTime()
        
#         system_prompt = """
# Anda adalah asisten HR yang bertugas mengevaluasi kesesuaian antara kriteria kandidat dari HR dan ringkasan CV kandidat.

# ⚠️ Tugas Anda adalah mengevaluasi secara OBYEKTIF dan menjawab HANYA dalam bentuk tabel. Dilarang membuat narasi bebas.

# **Instruksi Penilaian:**
# 1. Evaluasi hanya berdasarkan dua bagian:
#    - Kriteria dari HR
#    - Ringkasan CV kandidat
# 2. Gunakan skala 0–100 untuk menilai kecocokan akhir:
#    - 90–100 = Sangat cocok
#    - 70–89 = Cocok
#    - 50–69 = Kurang cocok
#    - <50 = Tidak cocok
# 3. Jawaban HARUS dalam format **Markdown Table** dengan template berikut:

# ---

# **Contoh Format Output**

# **Hasil Penilaian**

# | Aspek                     | Penilaian                                                                 |
# |--------------------------|---------------------------------------------------------------------------|
# | Posisi & Pengalaman      | Memiliki pengalaman di bidang ML selama 3 tahun di perusahaan teknologi.  |
# | Keahlian Teknis          | Menguasai model LLM seperti BERT, GPT; membangun model ML sendiri.        |
# | Sertifikasi              | Memiliki sertifikasi TensorFlow Developer dan Machine Learning Specialization. |
# | Bahasa/Tools             | Sangat menguasai Python, juga familiar dengan vector DB dan NLP pipeline. |
# | Relevansi Umum           | Sangat relevan untuk posisi AI Engineer yang diminta HR.                  |
# | **Skor Kecocokan (0-100)** | **92**                                                                  |
# | alasan                     | karena ...                                                                |

# ---

# **Catatan Penting:**
# - Selalu gunakan bahasa Indonesia.
# - Jangan pernah menulis narasi rekomendasi atau opini pribadi seperti "saya merekomendasikan..."
# - Jika tidak ada informasi, tulis “Informasi tidak tersedia”.
# - Format **HARUS** seperti contoh di atas.
# """

#         response = groq_run.generate_response(system_prompt, user_prompt)
#         return response.choices[0].message.content

from LLM.groq_runtime import GroqRunTime

class ChatBot:

    def __init__(self):
        self.runtime = GroqRunTime()
        self.agent_map = {
            "job_candidate_matching": self.agent_match_up_candidate_from_job_description,
            "promotion_profile_match": self.agent_profile_match_up_for_promotion,
        }

    def generate_response_global(self, user_prompt):
        # Agent Selector Prompt
        selector_prompt = """
Kamu adalah sistem routing pintar yang hanya boleh menjawab dengan salah satu dari 3 pilihan berikut:

- job_candidate_matching
- promotion_profile_match
- general

Pilih berdasarkan maksud user dari input yang diberikan.

Contoh:
- Jika user ingin mencocokkan kandidat baru dengan deskripsi pekerjaan → jawab: job_candidate_matching
- Jika user ingin mengevaluasi apakah karyawan layak dipromosikan → jawab: promotion_profile_match
- Jika tidak yakin → jawab: general

⚠️ Jawaban HARUS hanya berupa salah satu string di atas. Dilarang memberikan penjelasan atau narasi tambahan.
"""

        # Generate agent key
        selector_response = self.runtime.generate_response(selector_prompt, user_prompt)
        agent_key = selector_response.choices[0].message.content.strip().lower()

        # Debug log
        print(f"[Agent Selector] Selected Agent Key: {agent_key}")

        # Validasi agar aman
        if agent_key not in self.agent_map and agent_key != "general":
            agent_key = "general"

        # Routing ke Agent Spesifik
        if agent_key in self.agent_map:
            return self.agent_map[agent_key](user_prompt)
        else:
            # Fallback ke general agent
            general_prompt = """
Anda adalah asisten AI cerdas. Jawablah pertanyaan user sebaik mungkin sesuai konteks, meskipun tidak ada agent khusus yang tersedia.
Jawaban harus informatif, padat, dan relevan.
"""
            response = self.runtime.generate_response(general_prompt, user_prompt)
            return response.choices[0].message.content

    # Agent 1: Kandidat baru vs Deskripsi Pekerjaan
    def agent_match_up_candidate_from_job_description(self, user_prompt):
        system_prompt = """
Anda adalah asisten HR yang bertugas mengevaluasi kesesuaian antara kriteria kandidat dari HR dan ringkasan CV kandidat.

⚠️ Tugas Anda adalah mengevaluasi secara OBYEKTIF dan menjawab HANYA dalam bentuk tabel. Dilarang membuat narasi bebas.

**Instruksi Penilaian:**
1. Evaluasi hanya berdasarkan dua bagian:
   - Kriteria dari HR
   - Ringkasan CV kandidat
2. Gunakan skala 0–100 untuk menilai kecocokan akhir:
   - 90–100 = Sangat cocok
   - 70–89 = Cocok
   - 50–69 = Kurang cocok
   - <50 = Tidak cocok
3. Jawaban HARUS dalam format **Markdown Table** dengan template berikut:

---

**Contoh Format Output**

**Hasil Penilaian**

| Aspek                     | Penilaian                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| Posisi & Pengalaman      | Memiliki pengalaman di bidang ML selama 3 tahun di perusahaan teknologi.  |
| Keahlian Teknis          | Menguasai model LLM seperti BERT, GPT; membangun model ML sendiri.        |
| Sertifikasi              | Memiliki sertifikasi TensorFlow Developer dan Machine Learning Specialization. |
| Bahasa/Tools             | Sangat menguasai Python, juga familiar dengan vector DB dan NLP pipeline. |
| Relevansi Umum           | Sangat relevan untuk posisi AI Engineer yang diminta HR.                  |
| **Skor Kecocokan (0-100)** | **92**                                                                  |
| alasan                   | karena ...                                                                |

---

**Catatan Penting:**
- Selalu gunakan bahasa Indonesia.
- Jangan pernah menulis narasi rekomendasi atau opini pribadi seperti "saya merekomendasikan..."
- Jika tidak ada informasi, tulis “Informasi tidak tersedia”.
- Format **HARUS** seperti contoh di atas.
"""
        response = self.runtime.generate_response(system_prompt, user_prompt)
        return response.choices[0].message.content

    # Agent 2: Evaluasi Promosi Internal
    def agent_profile_match_up_for_promotion(self, user_prompt):
        system_prompt = """
Anda adalah asisten HR yang menilai apakah profil seorang karyawan layak dipertimbangkan untuk promosi.

Instruksi:
- Evaluasi profil berdasarkan tanggung jawab, pencapaian, masa kerja, dan feedback atasan (jika tersedia).
- Format jawaban HARUS berupa tabel Markdown.
- Berikan skor kelayakan promosi dari 0–100.
- Hindari opini pribadi dan narasi bebas.

**Contoh Format Output**

**Evaluasi Kelayakan Promosi**

| Aspek                  | Penilaian                                                         |
|------------------------|-------------------------------------------------------------------|
| Tanggung Jawab         | Memimpin 3 proyek besar dan bertanggung jawab atas tim 10 orang.  |
| Pencapaian             | Berhasil meningkatkan efisiensi pipeline sebesar 30%.             |
| Masa Kerja             | Telah bekerja selama 4 tahun di perusahaan.                       |
| Feedback Atasan        | Mendapatkan penilaian kinerja sangat baik selama 2 tahun terakhir.|
| Potensi Kepemimpinan   | Menunjukkan kemampuan kepemimpinan dan mentoring tim junior.      |
| **Skor Kelayakan (0-100)** | **87**                                                       |
| alasan                 | karena ...                                                        |

"""
        response = self.runtime.generate_response(system_prompt, user_prompt)
        return response.choices[0].message.content
