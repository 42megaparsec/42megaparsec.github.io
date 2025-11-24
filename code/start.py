import matplotlib.pyplot as plt
import umap
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. abstracts.txt 로드 (두 줄 개행으로 split)
# ==========================================
text = open("abstracts.txt", "r", encoding="utf-8").read()
blocks = [b.strip() for b in text.split("\n\n") if b.strip()]
print("Loaded abstracts:", len(blocks))

# ==========================================
# 2. 논문 제목 리스트 (blocks와 순서 완전 동일)
# ==========================================
titles = [
    "Spam Filtering",
    "Community Consistency",
    "Trade Multiresolution",
    "Agricultural Flow–Price",
    "Genetic Algorithm Environment",
    "Photosystem II Dynamics",
    "Growing Network Synchrony",
    "Community Reorganization",
    "SST Heat Network",
    "Self-consistent Gravity Model",
    "Pseudo-phase Synchrony"
]


assert len(titles) == len(blocks), "제목 개수와 초록 개수가 일치해야 합니다!"

# ==========================================
# 3. Sentence-BERT embedding
# ==========================================
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(blocks)

# ==========================================
# 4. UMAP 변환
# ==========================================
reducer = umap.UMAP(
    n_neighbors=5,      # 데이터가 11개라면 3~6 사이가 적절
    min_dist=0.3,       # 점들이 너무 붙지 않도록
    metric="cosine",    # 문서 임베딩에는 cosine이 정석
    random_state=42
)

xy = reducer.fit_transform(embeddings)

# ==========================================
# 5. 시각화 + 제목 라벨 표시
# ==========================================
plt.figure(figsize=(14, 10))

# 점 찍기
plt.scatter(xy[:, 0], xy[:, 1], s=60, color="black")

# 제목 텍스트 라벨 붙이기
for (x, y), title in zip(xy, titles):
    plt.text(x + 0.02, y + 0.02, title, fontsize=9, color="blue")

plt.axis("off")
plt.tight_layout()
plt.savefig("umap_with_titles.png", dpi=300)
plt.show()
