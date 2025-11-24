import geopandas as gpd
import matplotlib.pyplot as plt
import pickle as pk
import country_matching as CM
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch


# ===========================
# 설정값
# ===========================
year = 2022
TOP_PERCENT = 0.003   # 상위 10% 링크만 시각화


# ===========================
# 데이터 로드
# ===========================
with open("save/ITN_pos.txt", "rb") as f:
    pos_dic = pk.load(f)
pos_dic = CM.map_keys(pos_dic, CM.country_mapping)

with open("save/BACI_2022.pk", "rb") as f:
    od_data = pk.load(f)
od_data = CM.map_keys(od_data, CM.country_mapping)


# ===========================
# 그래프 생성
# ===========================
G = nx.DiGraph()

for i in od_data:
    for j in od_data[i]:
        w = od_data[i][j]
        if w > 0:
            G.add_edge(i, j, weight=w)

# 위치 없는 노드 제거
for n in list(G.nodes()):
    if n not in pos_dic:
        G.remove_node(n)


# ===========================
# 상위 p% 링크만 선택
# ===========================
all_weights = np.array([d["weight"] for _, _, d in G.edges(data=True)])
cutoff = np.quantile(all_weights, 1 - TOP_PERCENT)

# edge 중에서 cutoff 이상만 선택
edges_selected = [(u, v, d) for u, v, d in G.edges(data=True) if d["weight"] >= cutoff]

# 새로운 하위 그래프
G2 = nx.DiGraph()
for u, v, d in edges_selected:
    G2.add_edge(u, v, weight=d["weight"])

# 노드 좌표 유지
node_positions = {n: pos_dic[n] for n in G2.nodes()}


# ===========================
# 선 굵기 스케일링
# ===========================
weights = np.array([d["weight"] for _, _, d in G2.edges(data=True)])
if len(weights) > 0 and weights.max() != weights.min():
    w_scaled = 0.5 + 5.0 * ((weights - weights.min()) / (weights.max() - weights.min())) **(2)
else:
    w_scaled = np.ones(len(weights)) * 2.0


# ===========================
# 커브드 화살표 함수
# ===========================
def curved_arrow(ax, pos_src, pos_dst, weight, color="#3b4cc0", alpha=0.6):
    """두 점 사이에 커브드 화살표 그리기"""
    if pos_src == pos_dst:
        return
    rad = 0.25
    arrow = FancyArrowPatch(
        pos_src, pos_dst,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>",
        mutation_scale=10 + weight * 1.5,
        color=color,
        #alpha=(weight - 0.5)/3,
        alpha = 0.55,
        linewidth=weight
    )
    ax.add_patch(arrow)


# ===========================
# 플롯 시작
# ===========================
fig, ax = plt.subplots(figsize=(16, 9))

# 배경 지도
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
world.plot(ax=ax, color='#f8f7f2', edgecolor='gray', linewidth=0.7)


# ===========================
# 네트워크 노드 + 커브드 엣지
# ===========================
nx.draw_networkx_nodes(G2, node_positions, node_size=30, node_color="#2b2b2b", ax=ax)

# 커브드 엣지
for (u, v, d), w_scaled_val in zip(G2.edges(data=True), w_scaled):
    curved_arrow(ax, node_positions[u], node_positions[v], w_scaled_val)

plt.axis("off")
plt.tight_layout()
plt.show()
