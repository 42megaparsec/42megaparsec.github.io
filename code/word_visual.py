import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
from keybert import KeyBERT

# =======================================================
# 1. abstracts.txt 로드
# =======================================================
text = open("abstracts.txt", "r", encoding="utf-8").read()

# =======================================================
# 2. KeyBERT로 의미 있는 단어 추출
# =======================================================
kw_model = KeyBERT(model='all-MiniLM-L6-v2')

# top keywords 40개 정도 추출
keywords = kw_model.extract_keywords(
    text,
    keyphrase_ngram_range=(1, 2),  # 1~2 단어 표현
    stop_words='english',
    top_n=40
)

# 결과는 (단어, 점수) 형태 → 단어만 리스트로
words = [w for w, s in keywords]
print("Extracted words:\n", words)

# =======================================================
# 3. 각 단어 embedding
# =======================================================
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(words)

# =======================================================
# 4. TSNE로 2D 투영
# =======================================================
tsne = TSNE(
    n_components=2,
    perplexity=5,
    learning_rate=150,
    max_iter=2000,
    random_state=42
)
xy = tsne.fit_transform(embeddings)

# =======================================================
# 5. 시각화 (단어 라벨 표시)
# =======================================================
plt.figure(figsize=(14, 10))
plt.scatter(xy[:,0], xy[:,1], s=40, color="black")

for (x, y), word in zip(xy, words):
    plt.text(x + 0.5, y + 0.5, word, fontsize=10, color="blue")

plt.axis("off")
plt.tight_layout()
plt.savefig("keyword_tsne.png", dpi=300)
plt.show()
