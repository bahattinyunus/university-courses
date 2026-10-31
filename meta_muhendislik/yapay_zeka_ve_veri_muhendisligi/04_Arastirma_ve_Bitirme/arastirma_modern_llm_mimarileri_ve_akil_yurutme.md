# 🧠 Modern Büyük Dil Modelleri (LLM), Akıl Yürütme Mimarileri ve Otonom Ajan Sistemleri
### *İleri Yapay Zeka Araştırma Raporu & Mühendislik Monografı (2026+)*

> *“Yapay zeka sadece hesaplamanın hızlanması değil; sembolik akıl yürütme ile bağlantıcı (connectionist) sezginin tarihteki ilk büyük sentezidir.”*

---

## 📌 1. Giriş ve Kuramsal Temeller

Modern yapay zeka araştırmaları, klasik derin öğrenme paradigmalarından çok modlu (multimodal), otonom planlama yeteneğine sahip ve çıkarım zamanında (inference-time) dinamik hesaplama bütçesi tahsis edebilen **Akıl Yürüten Ajanlara (Reasoning Agents)** doğru evrilmiştir. Bu araştırma monografı, Transformer temelli modellerin içsel mekaniklerini, dikkat mekanizmalarının matematiksel optimizasyonunu ve otonom ajan mimarilerini analitik bir derinlikle incelemektedir.

---

## 📐 2. Dikkat Mekanizmaları ve Ölçekleme Matematiği

### 2.1. Standart Çok Başlı Dikkat (Multi-Head Self-Attention - MHA)
Girdi matrisi $X \in \mathbb{R}^{N \times d}$ verildiğinde, Projeksiyon matrisleri $W_Q, W_K, W_V \in \mathbb{R}^{d \times d_k}$ ile Sorgu ($Q$), Anahtar ($K$) ve Değer ($V$) tensörleri hesaplanır:

$$Q = X W_Q, \quad K = X W_K, \quad V = X W_V$$

Ölçeklenmiş Nokta Çarpım Dikkati (Scaled Dot-Product Attention) formülasyonu:

$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} + M \right) V$$

Burada $M \in \mathbb{R}^{N \times N}$ matrisi, otoregresif kod çözücüler için gelecekteki token'ları maskeleyen nedensel maskeleme matrisidir ($M_{ij} = -\infty, \forall j > i$).

### 2.2. Rotary Position Embedding (RoPE)
Modern mimariler (Llama-3, Mistral, Qwen, DeepSeek) mutlak pozisyon kodlamaları yerine göreli pozisyonel ilişkileri rotasyonel matrislerle kodlayan **RoPE** kullanır:

$$R_{\Theta, m}^d = \text{diag}\left( R_{\theta_1, m}, R_{\theta_2, m}, \dots, R_{\theta_{d/2}, m} \right)$$

Her 2 boyutlu alt uzay için dönüşüm:

$$R_{\theta_i, m} = \begin{pmatrix} \cos(m\theta_i) & -\sin(m\theta_i) \\ \sin(m\theta_i) & \cos(m\theta_i) \end{pmatrix}$$

Bu sayede iki token ($m$ ve $n$) arasındaki içsel çarpım yalnızca onların göreli mesafesine $(m - n)$ bağlı kalır.

---

## 🏗️ 3. Verimli Çıkarım ve Donanım Optimizasyonları

### 3.1. FlashAttention-2 ve FlashAttention-3 Algoritması
Bellek bant genişliği darboğazını (HBM Memory Bandwidth Bottleneck) aşmak için matris bloklama (tiling) ve çevrim içi softmax (online softmax normalization) uygulanır:

```mermaid
graph TD
    HBM["High Bandwidth Memory (HBM)<br/>Yüksek Kapasite / Düşük Hız (~3 TB/s)"]
    SRAM["GPU On-Chip SRAM Cache<br/>Düşük Kapasite / Ultra Yüksek Hız (~20 TB/s)"]
    Compute["Tensor Cores (FP16/FP8/BF16)<br/>Matris Çarpım Motoru"]
    
    HBM -->|Blok Transferi (Tiling)| SRAM
    SRAM -->|SRAM İçi Çevrim İçi Softmax & MM| Compute
    Compute -->|Sadece Nihai O Matrisi| HBM
```

---

## 🧩 4. Akıl Yürütme Paradigması: Düşünce Zincirinden Düşünce Ağacına

Klasik otoregresif çıkarım tek seferlik (greedy/sampling) sonraki token tahminine dayanırken; karmaşık matematiksel ve algoritmik problemlerde **Inference-Time Compute Scaling** uygulanır:

| Yöntem | Matematiksel Formülasyon | Karmaşıklık | Karar Alanı |
| :--- | :--- | :---: | :--- |
| **Direct Generation** | $P(Y \mid X) = \prod_{t=1}^T P(y_t \mid X, y_{<t})$ | $\mathcal{O}(T)$ | Düşük karmaşıklık |
| **Chain-of-Thought (CoT)** | $P(Y \mid X) = \sum_Z P(Y \mid X, Z) P(Z \mid X)$ | $\mathcal{O}(T_{\text{reasoning}} + T)$ | Doğrusal akıl yürütme |
| **Tree-of-Thoughts (ToT)** | $G = (V, E), \quad v^* = \arg\max_{v \in V} \mathcal{V}(v)$ | $\mathcal{O}(b^d)$ | Arama ve geri izleme (Backtracking) |
| **Graph-of-Thoughts (GoT)** | Dinamik yönlü döngüsüz çizge üzerinde sentez | Çizge tabanlı | Çapraz argüman birleştirme |

---

## 🛠️ 5. Otonom Çoklu Ajan (Multi-Agent) Koordinasyon Protokolü

```python
"""
Basitleştirilmiş Çift Döngülü Otonom Ajan Karar Motoru (ReAct + Reflection)
"""
from typing import List, Dict, Any

class AutonomousCognitiveAgent:
    def __init__(self, memory_stream, tools_registry):
        self.memory = memory_stream
        self.tools = tools_registry
        
    def reason_and_act(self, goal: str, context: Dict[str, Any]) -> str:
        plan = self._generate_hierarchical_plan(goal, context)
        step_results = []
        
        for step in plan:
            # 1. Düşünce (Thought)
            thought = self._deliberate(step, step_results)
            # 2. Eylem (Action)
            action, args = self._select_tool(thought)
            # 3. Gözlem (Observation)
            observation = self.tools.execute(action, **args)
            # 4. Öz-Denetim ve Düzeltme (Self-Correction)
            verification = self._verify_outcome(step, observation)
            if not verification.is_valid:
                observation = self._recover_failure(step, verification.critique)
            
            step_results.append({"step": step, "obs": observation})
            
        return self._synthesize_final_solution(step_results)
```

---

## 📚 6. Kanonik Bibliyografya ve Temel Makaleler

1. **Vaswani et al. (2017):** *“Attention Is All You Need”*, NeurIPS 2017.
2. **Su et al. (2021):** *“RoFormer: Enhanced Transformer with Rotary Position Embedding”*, arXiv:2104.09864.
3. **Dao et al. (2022, 2023):** *“FlashAttention & FlashAttention-2: Fast and Memory-Efficient Exact Attention with IO-Awareness”*, NeurIPS.
4. **Yao et al. (2023):** *“Tree of Thoughts: Deliberate Problem Solving with Large Language Models”*, NeurIPS.
5. **Shinn et al. (2023):** *“Reflexion: Language Agents with Verbal Reinforcement Learning”*, NeurIPS.
6. **OpenAI (2024):** *“Learning to Reason with LLMs (o1 System Paper)”*.

---

## 🔬 7. Açık Araştırma Problemleri (2026+)

- **Test-Time Search vs. Pre-Training Compute Trade-off:** Hangi problem sınıflarında modeli büyütmek yerine çıkarım zamanındaki arama bütçesini artırmak Pareto-optimaldir?
- **Sonsuz Bağlamda Halüsinasyon ve Kayıp İğne Problemi (Needle-In-A-Haystack):** $1M+$ token pencerelerinde ara katman dikkat seyrelmesinin önlenmesi.
- **Biçimsel Doğrulama ile Nöral Kodlama Sentezi:** LLM çıktılarının Lean 4 veya Coq gibi matematiksel ispat denetleyicileriyle uçtan uca kapalı döngüde eğitilmesi.
