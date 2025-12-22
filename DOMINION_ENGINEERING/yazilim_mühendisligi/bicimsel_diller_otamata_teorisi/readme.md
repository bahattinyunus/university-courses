# 🧠 Biçimsel Diller ve Otomata Teorisi

Bu dersin amacı, bilgisayarların **neleri yapabileceğini** ve **hangi sınırlar içinde çalıştığını** anlamaktır.  
Yani sadece nasıl kod yazıldığını değil, bir bilgisayarın **mantıksal sınırlarını** keşfetmeyi öğretir.  

---

## ⚙️ 1. Biçimsel Dil (Formal Language)

Bir **biçimsel dil**, belirli **kurallara göre oluşturulmuş semboller dizisidir**.

**Örnek:**

Alfabemiz:

Olası kelimeler:  
`a`, `b`, `ab`, `aab`, `abba`, ...

Kural: “Her `a`’nın ardından bir `b` gelmeli.”  
Geçerli kelimeler: `ab`, `aabb`  
Geçersiz kelimeler: `aa`, `aba`

Bu kuralları tanımlayan yapıya **gramer (grammar)** denir.

---

## ⚙️ 2. Otomata (Automata)

“Otomata”, belirli kurallara göre sembol dizilerini okuyan ve **kabul / red** kararı veren soyut makineleri ifade eder.  
Bu makineler, programların mantıksal temelini oluşturur.

---

## ⚙️ 3. Otomata Türleri

### 🟢 1. Deterministik Sonlu Otomat (DFA)

- Belirli sayıda durumu vardır.  
- Her sembol için tek geçiş tanımlıdır.  
- Kabul veya red kararı verir.

**Örnek:**  
“Çift sayıda ‘a’ içeren kelimeleri kabul et.”

---

### 🟡 2. Non-Deterministik Sonlu Otomat (NFA)

- Bir sembol için **birden fazla** geçiş olabilir.  
- Bazı durumlarda sembol okumadan (ε) geçiş yapılabilir.  
- Teorik olarak DFA ile **eşdeğer güçtedir.**

---

### 🔵 3. Yığınlı Otomat (PDA)

- Yığıt (stack) yapısı kullanır.  
- Parantez dengesi gibi iç içe yapıları tanır.  
- Örnek: `(()())` geçerli, `(()` geçersiz.

---

### 🔴 4. Turing Makinesi (TM)

- En güçlü modeldir.  
- Sonsuz bir bant üzerinde okuma-yazma kafasıyla çalışır.  
- Günümüz bilgisayarlarının teorik temelidir.

---

## 📚 4. Chomsky Hiyerarşisi

| Seviye | Dil Türü | Otomat Türü | Örnek |
|--------|-----------|--------------|--------|
| Tip 0 | Turing Dili | Turing Makinesi | Herhangi bir algoritma |
| Tip 1 | Bağlama duyarlı | Linearly bounded automaton | Programlama dilleri |
| Tip 2 | Bağlamdan bağımsız | Yığınlı Otomat | Parantez dengesi, ifadeler |
| Tip 3 | Düzenli | Sonlu Otomat | Regex desenleri |

---

## 🎯 5. Gerçek Hayat Bağlantıları

- **Regex (Regular Expression)** → DFA / NFA tabanlıdır.  
- **Derleyiciler** → PDA ve gramer analizine dayanır.  
- **NLP & Yapay Zekâ** → Biçimsel dil mantığı kullanır.  

---

# 🟢 DFA (Deterministic Finite Automaton)

## 1. Tanım
> Belirli sayıda durumu olan ve her sembolde tek geçiş yapan bir otomat türüdür.

Formel gösterim:

| Sembol | Anlam |
|--------|--------|
| Q | Durum kümesi |
| Σ | Alfabe |
| δ | Geçiş fonksiyonu |
| q₀ | Başlangıç durumu |
| F | Kabul durumları |

---

## 2. Örnek: “a sayısı çift olan kelimeler”

### Alfabe

---

## 3. Girdi Örnekleri

| Girdi | a sayısı | Son Durum | Kabul mü? |
|--------|-----------|------------|-----------|
| ε | 0 | q₀ | ✅ |
| a | 1 | q₁ | ❌ |
| aa | 2 | q₀ | ✅ |
| aba | 2 | q₀ | ✅ |
| abb | 1 | q₁ | ❌ |

---

# 🟡 NFA (Non-Deterministic Finite Automaton)

## 1. Tanım
> NFA, bir sembolde birden fazla geçiş yapabilen, hatta sembol okumadan (ε) da hareket edebilen otomat türüdür.

Formel gösterim:

(*) kabul durumu

---

## 3. NFA vs DFA

| Özellik | DFA | NFA |
|----------|-----|-----|
| Geçiş sayısı | Tek | Birden fazla |
| ε-geçiş | Yok | Var |
| Kararlılık | Belirli | Belirsiz |
| Güç | Eşit | Eşit |
| Tasarım kolaylığı | Zor | Kolay |

---

## 4. NFA → DFA Dönüşümü (Subset Construction)
Her NFA, **DFA’ya dönüştürülebilir.**  
Bunun için:
- NFA’daki tüm olası durum kümeleri, DFA’da **tek bir durum** olarak temsil edilir.  
- Bu yönteme **Subset Construction** veya **Powerset yöntemi** denir.

---

## 5. Gerçek Hayattaki Kullanımı

- **Regex motorları** (örneğin `grep`, `Python re`, `VSCode search`)  
- **Derleyici (lexer) tasarımı**  
- **Oyunlardaki durum makineleri**

---

## 🧩 Özet

| Kavram | DFA | NFA |
|--------|-----|-----|
| Belirleyicilik | ✅ | ❌ |
| Epsilon geçişi | ❌ | ✅ |
| Tasarım kolaylığı | Daha zor | Daha kolay |
| Hesap gücü | Aynı | Aynı |
| Kullanım alanı | Donanım, derleyici | Regex, dil tanıma |

---

## 💬 Sonuç
> “Kod yazmak yürümekse, otomata bilmek koşmaktır.” 🏃‍♂️💨  
Biçimsel diller ve otomata teorisi, bilgisayar biliminin **mantıksal iskeletini** oluşturur.  
Regex’lerden derleyicilere, yapay zekâdan doğal dil işlemeye kadar her şeyin temelinde bu teori yatar.
🧩 NFA → DFA Dönüşümü (Subset Construction Yöntemi)

NFA’lar sezgisel olarak kolay ama kararsızdır.
DFA’lar kararlı ama katıdır.
Bu yüzden NFA’yı DFA’ya çevirerek hem kararlılığı hem de aynı dili koruruz.

⚙️ 1. Mantık Temeli

Bir NFA aynı anda birden fazla durumda olabilir.
DFA ise tek bir durumda olmalıdır.

O yüzden NFA’nın her “durum kümesi”ni, DFA’da tek bir durum olarak temsil ederiz.

NFA: {q₀, q₁}
DFA: Q₀₁ (yeni bir birleşik durum)

Buna subset construction (küme oluşturma) yöntemi denir.

🧠 2. Adım Adım Örnek

Verilen NFA:

Durum	a	b
q₀	{q₀, q₁}	{q₀}
q₁	{q₂}	∅
q₂	∅	∅

Kabul durumları: {q₂}
Başlangıç durumu: q₀

🔹 Adım 1 — Başlangıç

DFA’da ilk durum, NFA’nın başlangıç durumunun epsilon-closure’ıdır (yani ε geçişleriyle ulaşılabilen tüm durumlar).
Burada ε yok, o yüzden DFA’nın başlangıç durumu {q₀}.

🔹 Adım 2 — “a” ve “b” için yeni kümeler oluştur
DFA Durumu	a	b
{q₀}	{q₀, q₁}	{q₀}
{q₀, q₁}	{q₀, q₁, q₂}	{q₀}
{q₀, q₁, q₂}	{q₀, q₁, q₂}	{q₀}
🔹 Adım 3 — Kabul durumlarını belirle

Eğer NFA kümesi içinde q₂ (kabul durumu) varsa, DFA’daki o küme de kabul durumudur.
Yani:

Kabul durumları = { {q₀, q₁, q₂} }

✅ Sonuç: Yeni DFA
Durum	a	b	Kabul?
{q₀}	{q₀, q₁}	{q₀}	❌
{q₀, q₁}	{q₀, q₁, q₂}	{q₀}	❌
{q₀, q₁, q₂}	{q₀, q₁, q₂}	{q₀}	✅

Yani DFA, NFA’nın davranışını deterministik şekilde taklit eder.
Bu yöntemle her NFA, %100 DFA’ya dönüştürülebilir. 💪

🔁 Regular Expression ↔ Otomata İlişkisi

Regular Expression (Düzenli İfade) ile DFA/NFA aslında aynı şeyi temsil eder.
Fark sadece ifadede mi gösteriyorsun, yoksa makineyle mi?

⚙️ 1. Regex → NFA

Regex aslında otomata kurallarının “dil versiyonu”dur.
Her regex ifadesi, bir NFA’ya dönüştürülebilir.

Regex	Anlam	NFA Yorum
a	sadece “a”	tek geçiş
a*	sıfır veya daha fazla “a”	geri döngü (loop)
`a	b`	“a” veya “b”
ab	“a” ardından “b”	seri geçiş
⚙️ 2. NFA → DFA → Regex Döngüsü

Yani şu dönüşüm mümkündür:

Regex ⇄ NFA ⇄ DFA


💡 Örnek:

Regex: a*b


Bunu bir DFA olarak çizelim:

(start) --a--> (loop a) --b--> (accept)


veya tabloyla:

Durum	a	b	Kabul?
q₀	q₀	q₁	❌
q₁	-	-	✅

Bu DFA, “0 veya daha fazla ‘a’ ardından tek bir ‘b’” desenini tanır.

⚡ 3. Regular Dillerin Özellikleri

Regular diller DFA/NFA ile tanınabilir.

Kapanma Özellikleri:

Birleşim (Union): Eğer L₁ ve L₂ düzenliyse, L₁ ∪ L₂ de düzenlidir.

Kesişim (Intersection): L₁ ∩ L₂ düzenlidir.

Ters (Complement): L düzenliyse, L̅ de düzenlidir.

Zincirleme (Concatenation): L₁L₂ düzenlidir.

Yıldız (Kleene Star): L* düzenlidir.

Yani regex’ler matematiksel olarak kapalı sistemlerdir — bu yüzden derleyici ve metin işleme sistemleri bu dili sever 😄

🎓 Özet
Dönüşüm	Açıklama
NFA → DFA	Subset (küme) yöntemiyle yapılır
Regex → NFA	Thompson inşası yöntemiyle yapılır
DFA → Regex	Durum eleme (state elimination) yöntemiyle yapılır
Regex ↔ DFA/NFA	Eşdeğer güçte temsil biçimleridir
🧠 Sonuç

NFA’lar soyut, DFA’lar kararlı.

Regex’ler ise bu otomatların dil halidir.

Her biri düzenli dillerin farklı bir temsilidir.

Ve tümü, bilgisayar biliminin “mantıksal temelini” oluşturur. 💻