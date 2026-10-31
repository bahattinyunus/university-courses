# 🌌 Parçacık Fiziği Standart Modeli, Ayar Alanları ve Kuantum Kütleçekimi Ufukları
### *Temel Fizik Araştırma Raporu & Kuramsal Monograf (2026+)*

> *“Fizik, evrenin en derin simetrilerini matematiksel dilde arama macerasıdır. Eğer simetri bozulmasaydı kütle var olamazdı; kütle olmasaydı evrende ışık haricinde hiçbir şey var olamazdı.”*

---

## 📌 1. Standart Modelin Ayar Simetrisi Grubu

Doğadaki bilinen dört temel kuvvetten üçü (Elektromanyetik, Zayıf ve Güçlü nükleer kuvvetler), yerel ayar dönüşümleri altında değişmez kalan Yang-Mills ayar teorisi çerçevesinde birleştirilmiştir:

$$\mathcal{G}_{\text{SM}} = SU(3)_C \times SU(2)_L \times U(1)_Y$$

Lagrangian yoğunluğu:

$$\mathcal{L}_{\text{SM}} = -\frac{1}{4} G_{\mu\nu}^a G^{\mu\nu a} -\frac{1}{4} W_{\mu\nu}^i W^{\mu\nu i} -\frac{1}{4} B_{\mu\nu} B^{\mu\nu} + \bar{\psi} i \gamma^\mu D_\mu \psi + (D_\mu \Phi)^\dagger (D^\mu \Phi) - V(\Phi) + \mathcal{L}_{\text{Yukawa}}$$

Ayar kovaryant türevi:

$$D_\mu = \partial_\mu - i g_s T^a G_\mu^a - i g \frac{\tau^i}{2} W_\mu^i - i g' \frac{Y}{2} B_\mu$$

---

## 💥 2. Brout-Englert-Higgs Mekanizması ve Kendiliğinden Simetri Kırılması

Elektrozayıf simetri kırılması, kompleks skaler Higgs çiftlisinin vakum beklenen değeri (VEV) kazanmasıyla gerçekleşir:

$$V(\Phi) = -\mu^2 \Phi^\dagger \Phi + \lambda (\Phi^\dagger \Phi)^2, \quad \mu^2 > 0, \; \lambda > 0$$

Minimum potansiyel konfigürasyonunda vakum beklenen değeri:

$$\langle \Phi \rangle_0 = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v \end{pmatrix}, \quad v = \sqrt{\frac{\mu^2}{\lambda}} \approx 246 \ \text{GeV}$$

Bu simetri kırılması sonucunda:
- $W^\pm$ bozonları: $M_W = \frac{1}{2} g v \approx 80.4 \ \text{GeV}$
- $Z^0$ bozonu: $M_Z = \frac{1}{2} \sqrt{g^2 + g'^2} v \approx 91.2 \ \text{GeV}$
- Foton ($A_\mu$): Kütlesiz kalır ($M_\gamma = 0$, artık $U(1)_{\text{EM}}$ simetrisi korunur).
- Skaler Higgs Bozonu: $M_H = \sqrt{2\lambda} v \approx 125.1 \ \text{GeV}$

---

## 🪢 3. Kuantum Kütleçekimi ve AdS/CFT Uyuşumu

Genel Görelilik ile Kuantum Alan Teorisini birleştirme arayışında Juan Maldacena tarafından 1997'de keşfedilen **AdS/CFT Karşılığı (Holografik Prensip)**:

```
(d + 1) Boyutlu Anti-de Sitter Uzayında Kuantum Kütleçekimi (Sicim Teorisi)
                                   ▲
                                   │ Holografik İkili (Duality)
                                   ▼
d Boyutlu Düz Sınırda (Boundary) Güçlü Bağlaşımlı Konform Alan Teorisi (CFT)
```

Bu ikilik, kara delik enformasyon paradoksunun ve kuantum dolanıklığının uzay-zaman geometrisini nasıl dokuduğunun ($ER = EPR$) anlaşılmasında modern teorik fiziğin en güçlü matematiksel köprüsüdür.

---

## 📚 4. Kanonik Kaynakça

1. **Peskin, M. E., & Schroeder, D. V. (1995):** *“An Introduction to Quantum Field Theory”*, Westview Press.
2. **Weinberg, S. (1995-2000):** *“The Quantum Theory of Fields”* (Vol. 1-3), Cambridge University Press.
3. **Zwiebach, B. (2009):** *“A First Course in String Theory”*, Cambridge University Press.
4. **Maldacena, J. (1999):** *“The Large-N Limit of Superconformal Field Theories and Supergravity”*, Int. J. Theor. Phys.
