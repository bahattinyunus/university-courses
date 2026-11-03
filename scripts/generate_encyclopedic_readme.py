#!/usr/bin/env python3
"""
University Courses (UC) - Encyclopedic README Generator
Evrensel Akademik İşletim Sistemi & Solopreneur Bilgi Mimarisi
"""
import os
import sys

# Safe UTF-8 encoding for Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Containers mappings with titles and 5 comprehensive quotes
CONTAINERS = {'askeri_bilimler_ve_savunma_teknolojileri': {'quotes': ['“En büyük zafer, savaşmadan kazanılan zaferdir; strateji kuvvetten, akıl silahtan üstündür.” — **Sun Tzu**', '“Savaş, siyasetin başka araçlarla devamıdır; hazırlıklı olan milletler barışın teminatıdır.” — **Carl von Clausewitz**', '“Cesaret tehlike karşısında aklın sükunetini korumasıdır.” — **Plutarkhos**', '“Kılıç kınındayken de caydırıcı olmalıdır; stratejist savaşı başlamadan zihninde bitirir.” — **Miyamoto Musashi**', '“Hatt-ı müdafaa yoktur, sath-ı müdafaa vardır. O satıh bütün vatandır.” — **Mustafa Kemal Atatürk**'], 'title': '⚔️ Savunma Sanayii, Harp Doktrini & Askeri Strateji'}, 'edebiyat_ve_diller': {'quotes': ['“Dilimin sınırları, dünyamın sınırlarıdır; kelimeler düşüncenin yaşayan heykelleridir.” — **Ludwig Wittgenstein**', '“Bir dili bilmek bir insan olmaktır, iki dil bilmek iki insan olmaktır.” — **Johann Wolfgang von Goethe**', '“Kitaplar, zamanın dalgaları üzerinde yüzen ve nesilden nesle değer taşıyan düşünce gemileridir.” — **Francis Bacon**', '“Dil, insan zihninin sonsuz sayıda düşünceyi sınırlı sayıda sesle ifade etme mucizesidir.” — **Noam Chomsky**', '“Okumak, geçmiş yüzyılların en erdemli insanlarıyla sohbet etmektir.” — **René Descartes**'], 'title': '📚 Filoloji, Dilbilim & Dünya Edebiyatı'}, 'epistemik': {'quotes': ['“Bilgi bir ışıktır; onu samimiyetle arayan zihin karanlıkta kalmaz. Hakikatin peşinde olmak en yüce insanlık görevidir.” — **El-Bîrûnî**', '“Bütün insanlar doğal olarak bilmek isterler. Bilgelik, ilk ilkelerin ve nedenlerin bilimidir.” — **Aristoteles**', '“Kendini bilmek, tüm bilgeliğin başlangıcıdır.” — **Sokrates**', '“Hakikat akılla keşfedilir; mantık ise o hakikatin yol gösterici feneridir.” — **İbn Rüşd (Averroes)**', '“Düşünceler kavramlar olmaksızın boş, sezgiler kavramlar olmaksızın kördür.” — **Immanuel Kant**'], 'title': '👁️ Epistemik Vizyon & Bilgi Felsefesi'}, 'genel': {'quotes': ['“Bütün büyük işler, küçük ve disiplinli adımların kararlılıkla bir araya gelmesiyle gerçekleşir.” — **Vincent van Gogh**', '“Damlayan su taşı deler; gücünden değil, sürekliliğinden.” — **Ovidius**', '“Yolculuğun kendisi varış noktasından daha öğreticidir.” — **Konfüçyüs**', '“Kendi başına düşünmeyi öğrenmemiş insan, başkalarının fikirlerinin hamalı olur.” — **Arthur Schopenhauer**', '“Dünyada en güç şey, insanın kendini bilmesi ve tanımasıdır.” — **Thales**'], 'title': '📂 Genel Metodoloji, Arşiv & Ortak Alanlar'}, 'guzel_sanatlar': {'quotes': ['“Sanat, doğanın gizemlerini keşfetme ve görünmeyeni görünür kılma çabasıdır.” — **Leonardo da Vinci**', '“Sanat, ruhlarımızdaki günlük hayatın tozunu silip süpürür.” — **Pablo Picasso**', '“Güzellik, hakikatin parıltısıdır.” — **Platon**', '“Sanatçı olmak, kendi gözleriyle görmek ve kalbiyle hissetmektir.” — **Auguste Rodin**', '“Sanat, insanın doğayla kurduğu en derin ve en kutsal diyalogdur.” — **John Ruskin**'], 'title': '🖼️ Güzel Sanatlar, Estetik & Görsel Kültür'}, 'hukuk_bilimi': {'quotes': ['“Adalet mülkün temelidir; hukukun bittiği yerde tiranlık, karmaşa ve haksızlık başlar.” — **John Locke**', '“Devletin nihai amacı özgürlüktür; adalet ise o özgürlüğün koruyucu kalkanıdır.” — **Baruch Spinoza**', '“Hukuk, aklın tutkulardan arınmış sesidir.” — **Aristoteles**', '“Bir tek kişiye yapılan haksızlık, bütün topluma yöneltilmiş bir tehdittir.” — **Montesquieu**', '“Kanunların kuvveti, halkın vicdanında bulduğu yankı kadardır.” — **Cicero**'], 'title': '⚖️ Adalet, Hukuk Kuramı & Yasal Düzen'}, 'ilahiyat_ve_din': {'quotes': ['“İlim ilim bilmektir, ilim kendin bilmektir; sen kendini bilmezsin, ya nice okumaktır.” — **Yunus Emre**', '“Aklını kullanmayanların üzerine pislik yağar.” — **Yunus Suresi, 100**', '“Hakikat nereden gelirse gelsin onu kabul etmek gerekir; hakikatten daha değerli bir şey yoktur.” — **El-Kindî**', '“Dünle beraber gitti cancağızım, ne kadar söz varsa düne ait; şimdi yeni şeyler söylemek lazım.” — **Mevlana Celaleddin-i Rumi**', '“Kalp gözüyle görmeyen akıl, hakikatin derinliğini kavrayamaz.” — **İmam Gazali**'], 'title': '📚 İlahiyat, Dinler Tarihi & Karşılaştırmalı Felsefe'}, 'iletisim': {'quotes': ['“Ortam, mesajın ta kendisidir; insan iletişim kurduğu ve anlam ürettiği ölçüde var olur.” — **Marshall McLuhan**', '“İletişimdeki en büyük sorun, anlaşıldığı yanılsamasıdır.” — **George Bernard Shaw**', '“Doğru söz etkileyicidir, ama yerinde bir sükût hiçbir söze değişilmez.” — **Mark Twain**', '“Haber basıldığında gerçeğin yerini alır; medyanın mimarisi kamusal zihni inşa eder.” — **Walter Lippmann**', '“Televizyon ve dijital ekranlar bizi bilgilendirmez, eğlendirerek uyuşturur; hakiki bilgi derin tefekkür ister.” — **Neil Postman**'], 'title': '📡 İletişim, Medya Ekolojisi & Dijital Anlatı'}, 'kariyer_ve_sertifikasyonlar': {'quotes': ['“Şans, yalnızca hazırlıklı ve yetkin zihinlere güler; profesyonel ustalık kesintisiz inşa edilir.” — **Louis Pasteur**', '“Kalite bir eylem değil, bir alışkanlıktır.” — **Will Durant (Aristoteles yorumu)**', '“Yaptığınız işi mükemmel yapın; öyle ki insanlar sizi görmezden gelemesin.” — **Steve Martin**', '“Geleceği tahmin etmenin en iyi yolu onu inşa etmektir; verimli çalışan bir kariyer sistemli alışkanlıkların eseridir.” — **Peter Drucker**', '“Bilgiye yapılan yatırım her zaman en yüksek faizi öder.” — **Benjamin Franklin**'], 'title': '🚀 Kariyer, Portfolyo, Standartlar & Sertifikasyon'}, 'meta_muhendislik': {'quotes': ['“Bilim insanları var olan dünyayı inceler; mühendisler ise daha önce hiç var olmamış dünyaları yaratır.” — **Theodore von Kármán**', '“Bir makine insan emeğini hafifletmiyorsa ve zihni özgürleştirmiyorsa, sadece karmaşık bir demir yığınıdır.” — **Nikola Tesla**', '“Mühendislik, bilimi insanlığın refahı için gerçeğe dönüştürme sanatıdır.” — **Neil Armstrong**', '“Uygulamaya dökülmeyen tasarım zihinde bir hayalden ibarettir; hakiki mühendislik çalışan mekanizmadır.” — **El-Cezerî**', '“Bir araya gelmek bir başlangıçtır, beraberliği sürdürmek bir ilerlemedir, birlikte çalışmak ise gerçek başarıdır.” — **Henry Ford**'], 'title': '🛠️ Mühendislik & İleri Teknoloji Bilimleri'}, 'meta_yetkinlikler_ve_gelisim': {'quotes': ['“Düşünceleriniz ne ise hayatınız da odur; kendi zihnini yöneten, tüm dünyaya yön verir.” — **Marcus Aurelius**', '“İnsanın en büyük zaferi, kendi nefsine ve zaaflarına karşı kazandığı zaferdir.” — **Platon**', '“Rüzgarın yönünü değiştiremezsiniz, ancak yelkenlerinizi hedefinize göre ayarlayabilirsiniz.” — **Epiktetos**', "“Yaşamak için bir 'neden'i olan insan, her türlü 'nasıl'a katlanabilir.” — **Friedrich Nietzsche / Viktor Frankl**", '“Disiplin, neyi en çok istediğin ile şu anda neyi istediğin arasındaki seçimdir.” — **Abraham Lincoln**'], 'title': '🧠 Meta-Zihin, Otonom İrade & Bilişsel Disiplin'}, 'mimarlik_ve_tasarim': {'quotes': ['“Mimarlık, taşın ve ışığın sessiz şiiridir; mekân ise insan ruhunun biçim bulmuş halidir.” — **Mimar Sinan**', '“Biçim daima işlevi takip eder; bu doğanın en temel yasasıdır.” — **Louis Sullivan**', '“Bir binayı tasarlarken, geleceğin hatıralarını inşa edersiniz.” — **Juhani Pallasmaa**', '“İyi mimarlık sağlamlık, işlevsellik ve güzellik üçlüsünün kusursuz dengesidir.” — **Vitruvius**', '“Mimarlık, ışık altında bir araya getirilmiş kütlelerin ustaca, doğru ve görkemli oyunudur.” — **Le Corbusier**'], 'title': '🏛️ Mimarlık, Tasarım & Mekânsal Şehircilik'}, 'ogretmenlik': {'quotes': ['“Bana bir harf öğretenin kırk yıl kölesi olurum; zira akılları inşa edenler medeniyetin hakiki mimarlarıdır.” — **Hz. Ali**', '“Eğitim, dünyayı değiştirmek için kullanabileceğiniz en güçlü silahtır.” — **Nelson Mandela**', '“Öğretmek, iki kez öğrenmektir.” — **Joseph Joubert**', '“Eğitim hayata hazırlık değildir; eğitimin kendisi doğrudan hayatın ta kendisidir.” — **John Dewey**', '“Çocuğa gösterilen hürmet, insanlığın geleceğine duyulan saygıdır.” — **Maria Montessori**'], 'title': '🎓 Eğitim Fakültesi, Pedagoji & Didaktik'}, 'on_lisans_programlari': {'quotes': ['“Uygulamaya dökülmeyen bilgi bir yüktür; maharet ve teknik ustalık teorinin can damarıdır.” — **El-Cezerî**', '“Bir işi iyi yapmak, ona ruhunu ve emeğini katmak demektir; hak ile sabır dileyip usta olan pirdir.” — **Ahi Evran**', '“Bana anlatırsan unuturum, gösterirsen hatırlarım, yaptırırsan anlarım.” — **Konfüçyüs**', '“Kalite, kimse bakmadığı zaman bile işi doğru yapmaktır.” — **Henry Ford**', '“Ölçemediğiniz şeyi yönetemez ve geliştiremezsiniz.” — **W. Edwards Deming**'], 'title': '📋 Mesleki Yüksekokul & Uygulamalı Teknik Disiplinler'}, 'ozel_arastirma_alanlari': {'quotes': ['“Geleceği tahmin etmenin en emin yolu, onu bizzat icat etmektir.” — **Alan Kay**', '“Hayal gücü bilgiden daha önemlidir; çünkü bilgi sınırlıyken hayal gücü tüm dünyayı kucaklar.” — **Albert Einstein**', '“Sadece sınırları aşmayı göze alanlar, ne kadar ileri gidebileceklerini keşfedebilirler.” — **T. S. Eliot**', '“Yeterince gelişmiş bir teknoloji büyüden ayırt edilemez.” — **Arthur C. Clarke**', '“Gelecek çoktan geldi, sadece homojen bir biçimde dağıtılmadı.” — **William Gibson**'], 'title': '🔬 Özel Araştırma, Füzyon & Sınır Disiplinler'}, 'saglik': {'quotes': ['“Şifanın esası bedenin ve ruhun ahengini kavramaktır; tıp, insanın doğayla uyum sanatıdır.” — **İbn-i Sînâ (Avicenna)**', '“Hastalık yoktur, hasta vardır; doğanın iyileştirici gücü hekimin en büyük yardımcısıdır.” — **Hipokrat**', '“Bedeninize iyi bakın; yaşamak zorunda olduğunuz yegâne eviniz orasıdır.” — **Jim Rohn**', '“Tıbbın gayesi acıyı dindirmek ve yaşamı korumaktır; mikrop değil zemin her şeydir.” — **Louis Pasteur**', '“Bütün maddeler zehirdir; zehir ile ilacı birbirinden ayıran tek şey dozdur.” — **Paracelsus**'], 'title': '🩺 Sağlık Bilimleri, Klinik Tıp & Yaşam'}, 'sosyal_ve_beseri_bilimler': {'quotes': ['“Coğrafya kaderdir; lakin toplumların yükselişi ve çöküşü adalet, asabiyet ve üretim dengesine bağlıdır.” — **İbn-i Haldun**', '“Düşünüyorum, öyleyse varım.” — **René Descartes**', '“İncelenmemiş bir hayat, yaşanmaya değer değildir.” — **Sokrates**', '“İnsan kendi ördüğü anlam ağlarında asılı duran bir varlıktır.” — **Max Weber**', '“Bütün zenginliklerin kaynağı emektir ve o emeğin akılla yönlendirilmesidir.” — **Adam Smith**'], 'title': '⚖️ Sosyal, Beşeri, İdari & Davranışsal Bilimler'}, 'spor_bilimleri': {'quotes': ['“Bedenin terbiyesi zihnin keskinliğidir; disiplin, arzu ile başarı arasındaki köprüdür.” — **Platon**', '“Hiç kimse bedeninin ulaşabileceği potansiyeli görmeden yaşlanma hakkına sahip değildir.” — **Sokrates**', '“Zorluklar bedeni güçlendirir, tıpkı çalışma ve tefekkürün zihni güçlendirdiği gibi.” — **Seneca**', '“Sağlam kafa sağlam vücutta bulunur.” — **Mustafa Kemal Atatürk / Juvenalis**', '“Suyun şeklini al; su gibi ak veya kaya gibi çarp. Sınırları aşan irade esnek olandır.” — **Bruce Lee**'], 'title': '🏅 Spor Bilimleri, Kinetik & Fiziksel Performans'}, 'tarim_ve_ziraat_bilimleri': {'quotes': ['“Toprak berekettir; tohumu sabır, emek ve ilimle işleyen milletin hakiki efendisidir.” — **Mustafa Kemal Atatürk**', '“Toprak işlenmedikçe zenginlik vermez; doğanın yasalarına uymayan hiçbir sistem ayakta kalamaz.” — **Ksenophon**', '“Ektiğini biçmek sadece tarımın değil, evrensel adaletin de kanunudur.” — **Cicero**', '“Tarım insanlığın en temel direğidir; toprak verimli oldukça medeniyet yükselir.” — **Norman Borlaug**', '“Bitkiler doğanın kimyagerleridir; toprağın inorganik minerallerini canlı hayata dönüştürürler.” — **Justus von Liebig**'], 'title': '🌱 Tarım, Ziraat, Biyosistem & Doğa Bilimleri'}, 'temel_bilimler': {'quotes': ['“Evrenin kitabı matematik dilinde yazılmıştır; onun harfleri üçgenler, daireler ve geometrik formlardır.” — **Galileo Galilei**', '“Doğanın sırlarını çözmek istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün.” — **Nikola Tesla**', '“Matematik, bilimlerin kraliçesidir; sayı teorisi ise matematiğin kraliçesidir.” — **Carl Friedrich Gauss**', '“Tabiat hiçbir şeyi boşuna yapmaz; en az vasıtayla en çok neticeyi elde eder.” — **Sir Isaac Newton**', '“Bilim adamı laboratuvarda sadece bir teknisyen değil, doğa masallarını dinleyen bir çocuktur.” — **Marie Curie**'], 'title': '🧪 Temel Fen Bilimleri (Fizik, Kimya, Matematik)'}, 'turizm_ve_gastronomi': {'quotes': ['“Dünyayı gezmek zihindeki önyargıları kaldırır; lezzet ve misafirperverlik ise insanlığın ortak lisanıdır.” — **Evliya Çelebi**', '“Yemek yemek bir zorunluluktur, ancak akıllıca ve zevkle yemek bir sanattır.” — **François de La Rochefoucauld**', '“Yolculuk, sadece yeni manzaralar görmek değil; dünyaya yeni gözlerle bakabilmektir.” — **Marcel Proust**', '“Bana ne yediğini söyle, sana kim olduğunu söyleyeyim.” — **Jean Anthelme Brillat-Savarin**', '“Yemek kültürü, bir milletin toprağıyla, tarihiyle ve ruhuyla kurduğu en samimi bağdır.” — **Anthony Bourdain**'], 'title': '🏨 Turizm, Ağırlama & Gastronomi Sanatı'}}

def format_dept_name(d):
    dept_name = d.replace('_', ' ').title()
    dept_name = (dept_name
                 .replace('Muhendisligi', 'Mühendisliği')
                 .replace('Insaat', 'İnşaat')
                 .replace('Isletme', 'İşletme')
                 .replace('Ulasim', 'Ulaşım')
                 .replace('Bilisim', 'Bilişim')
                 .replace('Sagligi', 'Sağlığı')
                 .replace('Egitimi', 'Eğitimi')
                 .replace('Ogretmenligi', 'Öğretmenliği')
                 .replace('Programciligi', 'Programcılığı')
                 .replace('Iktisat', 'İktisat')
                 .replace('Iletisim', 'İletişim'))
    return dept_name

def generate_encyclopedic_readme():
    total_depts = 0
    total_tiers = 0
    
    # Pre-calculate counts
    for folder in CONTAINERS.keys():
        c_path = os.path.join(ROOT_DIR, folder)
        if os.path.exists(c_path):
            depts = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and not d.startswith('.')]
            total_depts += len(depts)
            for d in depts:
                dp = os.path.join(c_path, d)
                tiers = [t for t in os.listdir(dp) if os.path.isdir(os.path.join(dp, t)) and t.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_'))]
                total_tiers += len(tiers)

    header = f"""<div align="center">

![UAOS Banner](assets/uaos_hero_banner.png)

# 🌌 UNIVERSITY COURSES (UC)
### *Evrensel Akademik İşletim Sistemi & Solopreneur Bilgi Mimarisi* 🌐🧬🏗️

[![Versiyon](https://img.shields.io/badge/%C3%87EK%C4%B0RDEK-v4.6--RESEARCH-00A9E0?style=for-the-badge&logo=target)](./)
[![Mimar](https://img.shields.io/badge/M%C4%B0MAR-Yunus_%C3%87etin-D4AF37?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/arch-yunus)
[![Repo](https://img.shields.io/badge/REPO-university--courses-black?style=for-the-badge&logo=github)](https://github.com/bahattinyunus/university-courses)
[![Kapsam](https://img.shields.io/badge/KAPSAM-{total_depts}_Disiplin-18453B?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Kademeler](https://img.shields.io/badge/KADEMELER-{total_tiers}_Mod%C3%BCl-6f42c1?style=for-the-badge&logo=diagram)](./SUMMARY.md)
[![Monograflar](https://img.shields.io/badge/MONOGRAFLAR-20_Derin_Arastirma-ff69b4?style=for-the-badge&logo=googlescholar&logoColor=white)](./assets/curriculum_index.json)

---

> *“Eğer daha uzağı görebildiysem, bu benden önceki devlerin omuzlarında durduğum içindir.”*  
> — **Sir Isaac Newton**

> *“İlim cesaret ister; cehaletin karanlığını sadece hakikatin sarsılmaz ışığı dağıtabilir.”*  
> — **El-Farabi**

> *“Basitlik, en üst düzeydeki gelişmişliktir.”*  
> — **Leonardo da Vinci**

> *“Bilim ve sanat, takdir edilmediği yerden göç eder.”*  
> — **İbn-i Sînâ**

> *“Evren her an gözlemimize açıktır; fakat onun dilini ve yazıldığı harfleri öğrenmeden anlaşılamaz. O dil matematiktir.”*  
> — **Galileo Galilei**

---

## 📜 EVRENSEL AKIL VE BİREYSEL EGEMENLİK MANİFESTOSU

**University Courses (UC)**; sıradan bir ders notu arşivi veya pasif bir dokümantasyon havuzu değildir. **Yüksek Kaldıraçlı Bireyin (Solopreneur Polymath) Zihinsel Karargâhı, Bilişsel İşletim Sistemi ve Epistemik Sermaye Mimarisi**dir.

Bilginin hızla çoğaldığı ama derinliğin, odaklanmanın ve sentez gücünün aşındığı modern bilgi çağında, asıl üstünlük bilginin ham hacminde değil; onun **bütüncül kavranışında, felsefi temellendirilişinde, zihinsel modellerle sentezlenmesinde ve somut katma değere dönüştürülme mimarisindedir.**

Eğitimi tek tip kalıpların, hantal bürokratik duvarların ve dar uzmanlaşma tuzaklarının ötesine taşıyarak; **İslam Altın Çağı'nın polimatik dehasını, Rönesans'ın evrensel araştırma merakını ve modern bilişim çağının yüksek teknoloji disiplinini** tek bir epistemik çatı altında birleştiriyoruz.

---

## 🏛️ BÜYÜK DÜŞÜNÜRLER VE POLİMATLAR PANTEONU (THE POLYMATH PANTHEON)

> *“Bütün bilimler birbirine bağlıdır; biri tam kavranmadan diğeri hakkıyla anlaşılamaz.”* — **Roger Bacon**

### 1. 🧪 Bilim, Matematik ve Doğa Felsefesi
*   > *“Matematik, doğanın gizli kalmış armonisini insan aklına tercüme eden ilahi dildir.”* — **Leonhard Euler**
*   > *“Doğa kanunları öylesine kusursuz bir simetriye sahiptir ki, onları keşfetmek adeta bir ibadettir.”* — **Johannes Kepler**
*   > *“Fizikte önemli olan gerçeği bulmaktır, popüler olanı değil.”* — **Richard Feynman**
*   > *“Evren, matematiksel bir düşünceden ibarettir.”* — **Sir James Jeans**
*   > *“Bir kuramın güzelliği, onun doğruluğunun en güçlü kanıtıdır.”* — **Paul Dirac**
*   > *“Matematik esas olarak sabır olayıdır. Ezberleyerek değil, keşfederek anlamak gerekir.”* — **Cahit Arf**
*   > *“Bilim yapmak sadece zeka işi değildir; bilakis büyük bir tutku, disiplin ve fedakarlık gerektirir.”* — **Aziz Sancar**
*   > *“Hayatta hiçbir şeyden korkmayın, yalnızca anlamaya çalışın. Şimdi daha fazlasını anlama ve daha az korkma zamanıdır.”* — **Marie Curie**
*   > *“Bana bir dayanak noktası verin, dünyayı yerinden oynatayım.”* — **Arşimet (Archimedes)**

### 2. 👁️ Epistemoloji, Mantık ve Zihin Mimarisi
*   > *“Zihin doldurulacak bir kap değil, tutuşturulacak bir meşaledir.”* — **Plutarkhos**
*   > *“Mantık, aklı hataya düşmekten koruyan bir terazi ve hakikatin mihenk taşıdır.”* — **İbn-i Sînâ**
*   > *“Aklını kullanma cesaretini göster! (Sapere Aude!)”* — **Immanuel Kant**
*   > *“Şüphe etmek düşünmektir; düşünmek ise var olmaktır.”* — **René Descartes**
*   > *“Dilimin sınırları, zihnimin evrenidir.”* — **Ludwig Wittgenstein**
*   > *“Hakikat arayışı, insanın kendi aklına ve vicdanına borçlu olduğu en asil vazifedir.”* — **İbn Rüşd (Averroes)**
*   > *“Özgürlük, aklın zorunlulukları kavraması ve ona göre eylemesidir.”* — **Baruch Spinoza**
*   > *“Bilim yanılabilir teorilerin cesurca öne sürülmesi ve onların acımasızca sınanması sürecidir.”* — **Karl Popper**
*   > *“Bildiğim tek şey, hiçbir şey bilmediğimdir.”* — **Sokrates**

### 3. ⚙️ Mühendislik, Sibernetik ve Hesaplama Zekası
*   > *“Makineler düşünebilir mi sorusu, denizaltılar yüzebilir mi sorusu kadar anlamsızdır.”* — **Edsger W. Dijkstra**
*   > *“Geleceği tahmin etmeye çalışma; geleceği kodla ve inşa et.”* — **Alan Kay**
*   > *“Entelektüel bir problemi çözmenin ilk adımı, onu çözülebilir alt bileşenlerine ayırmaktır.”* — **Claude Shannon**
*   > *“Mükemmellik, eklenecek bir şey kalmadığında değil, çıkarılacak bir şey kalmadığında elde edilir.”* — **Antoine de Saint-Exupéry**
*   > *“Bilgisayar bilimi, teleskopun astronomiyle ilişkisi neyse bilgisayarlarla o kadar ilgilidir; asıl mesele hesaplamanın doğasıdır.”* — **Hal Abelson**
*   > *“Yalnızca kısa bir mesafe ilerisini görebiliriz, ama orada yapılması gereken ne çok iş olduğunu açıkça fark ederiz.”* — **Alan Turing**
*   > *“Basit bir mekanizma tasarlamak karmaşık bir mekanizma tasarlamaktan yüz kat daha fazla zeka ister.”* — **El-Cezerî**
*   > *“Mühendislik, kaynakların sınırlı olduğu bir dünyada hayal gücünü gerçeğe dönüştürme disiplinidir.”* — **John von Neumann**
*   > *“Biz makineleri biçimlendiririz, sonra da makineler bizi biçimlendirir.”* — **Norbert Wiener**

### 4. ⚔️ Strateji, İrade ve Bilişsel Disiplin (Stoic & Strategic Mastery)
*   > *“Dış olayları kontrol edemezsin, ama kendi zihnini ve tepkilerini her an kontrol edebilirsin.”* — **Marcus Aurelius**
*   > *“Zorluklar olmasaydı, insanın büyüklüğü ve iradesi nasıl ortaya çıkardı?”* — **Epiktetos**
*   > *“Planlar hiçbir şeydir, lakin planlama her şeydir.”* — **Dwight D. Eisenhower**
*   > *“Stratejisi olmayan taktik, yenilgiden önceki son gürültüdür.”* — **Sun Tzu**
*   > *“Kendine hakim olan, tüm dünyaya hakim olur.”* — **Lao Tzu**
*   > *“Bin günlük eğitimle başlarsın, on bin günlük disiplinle ustalaşırsın.”* — **Miyamoto Musashi**
*   > *“Zihni sakinleştirmeden dünyayı fethedemezsiniz; en büyük savaş kendi dürtülerinizle yapılandır.”* — **Seneca**
*   > *“Beni öldürmeyen şey, beni daha güçlü kılar.”* — **Friedrich Nietzsche**
*   > *“Savaşta kuvvetten çok muhakeme, hırstan çok sükunet kazandırır.”* — **Carl von Clausewitz**

### 5. 🌌 Kozmoloji, Evren ve Varlık Düzeni
*   > *“Bir yerlerde inanılmaz bir şey keşfedilmeyi bekliyor.”* — **Carl Sagan**
*   > *“Evren hakkındaki en anlaşılmaz şey, onun anlaşılabilir olmasıdır.”* — **Albert Einstein**
*   > *“Ayaklarınızın altına değil, yıldızlara bakın. Gördüğünüz şeylerin mantığını anlamaya ve evrenin neden var olduğunu kavramaya çalışın.”* — **Stephen Hawking**
*   > *“Göklerin ilmi aklın kanatlarıdır; insan yıldızlara baktıkça kendi hakiki yerini idrak eder.”* — **Ali Kuşçu**
*   > *“Hakikat zamanın kızıdır; otoritenin değil.”* — **Giordano Bruno**
*   > *“Düşünce, bir kıvılcımdan ibarettir sonsuz karanlıkta; lakin her şeyi aydınlatan da o kıvılcımdır.”* — **Henri Poincaré**

### 6. 🎨 Estetik, Sanat ve Yaratıcı Deha
*   > *“Sanat, doğanın gizemlerini keşfetme ve görünmeyeni görünür kılma çabasıdır.”* — **Leonardo da Vinci**
*   > *“Sanat, ruhlarımızdaki günlük hayatın tozunu silip süpürür.”* — **Pablo Picasso**
*   > *“Güzellik, hakikatin parıltısıdır.”* — **Platon**
*   > *“Taşın içindeki heykeli görüyorum; tek yapmam gereken fazlalıkları yontup onu özgür bırakmak.”* — **Michelangelo**
*   > *“Bilmek yetmez, uygulamalıyız. İstemek yetmez, yapmalıyız.”* — **Johann Wolfgang von Goethe**
*   > *“Sanatçı, doğanın kölesi değil, onun sırdaşı ve tamamlayıcısıdır.”* — **John Ruskin**

### 7. 📜 Medeniyet, Tarihsel Dinamikler ve Toplum Kuramı
*   > *“Coğrafya kaderdir; lakin toplumların yükselişi ve çöküşü adalet, asabiyet ve üretim dengesine bağlıdır.”* — **İbn-i Haldun**
*   > *“Tarih, geleceğin haritasını geçmişin ışığıyla çizen en büyük kılavuzdur.”* — **Alexis de Tocqueville**
*   > *“İnsan, kendi yarattığı kurumların tutsağı olmamak için sürekli sorgulayan varlıktır.”* — **Max Weber**
*   > *“İşbölümü ve uzmanlaşma insanlığın zenginliğini artırır; lakin sentez gücü o zenginliğe ruh verir.”* — **Adam Smith**
*   > *“Medeniyetler dışarıdan fethedilmeden önce içeriden çözülürler.”* — **Arnold Toynbee**

### 8. 🧬 Biyoloji, Yaşamın Kodu ve Adaptasyon
*   > *“Hayatta kalanlar en güçlüler ya da en zekiler değil; değişime en hızlı ayak uydurabilenlerdir.”* — **Charles Darwin**
*   > *“Yaşam, entropinin kaosuna karşı düzen ve bilgi inşa etme sanatıdır.”* — **Erwin Schrödinger**
*   > *“Doğa acele etmez, yine de her şey vaktinde tamamlanır.”* — **Lao Tzu**
*   > *“Hücrelerimizin her birinde milyarlarca yıllık evrimsel mirasın şifresi saklıdır.”* — **Francis Crick**

---

## 🌟 TARİHİN BÜYÜK POLİMATLARININ ZİHİNSEL İLKELERİ

Evrensel dehaların düşünme ve üretme yöntemleri, bu repo mimarisinin ilham kaynağıdır:

```mermaid
graph TD
    subgraph "Leonardo da Vinci Prensipleri"
        L1["Curiosità<br/>(Doyumsuz Merak)"]
        L2["Dimostrazione<br/>(Deneyimle Sınama)"]
        L3["Sensazione<br/>(Duyusal Keskinlik)"]
        L4["Sfumato<br/>(Belirsizliği Kucaklama)"]
        L5["Arte/Scienza<br/>(Mantık & Hayal Dengesi)"]
        L6["Corporalita<br/>(Beden & Zihin Uyumu)"]
        L7["Connessione<br/>(Sistemik Bağlantısallık)"]
    end
```

*   **1. Leonardo da Vinci Modeli (Bütüncül Görsel & Mekanik Zeka):**
    *   *Curiosità:* Yaşam boyu kesintisiz öğrenme ve çocuksu merakı kaybetmeme.
    *   *Dimostrazione:* Bilgiyi deneyim ve pratik aracılığıyla test etme; dogmaları reddetme.
    *   *Connessione:* Görünüşte alakasız alanlar (anatomi, hidrolik, resim, müzik, harp sanatı) arasında yapısal örüntüler kurma.
*   **2. İbn-i Sînâ Modeli (Ansiklopedik Epistemoloji & Sentez):**
    *   Tıbbi gözlem ile Aristo mantığını ve metafiziği sentezleyerek dönemin tüm bilgisini *El-Kânûn fî't-Tıbb* ve *Kitâbü'ş-Şifâ* ile modülerleştirdi.
*   **3. Gottfried Wilhelm Leibniz Modeli (Evrensel Karakteristika):**
    *   Matematiksel kalkülüsü, felsefi monadolojiyi ve ikili sayı sistemini (binary) tek bir evrensel sembolik dil potasında eritti.
*   **4. Johann Wolfgang von Goethe Modeli (Morfolojik Düşünce):**
    *   Edebiyat şaheserleri üretirken aynı zamanda bitki morfolojisi, anatomi ve renk teorisi üzerine çığır açan bilimsel eserler verdi.
*   **5. Nikola Tesla Modeli (Zihinsel Simülasyon & Prototipleme):**
    *   Fikirleri fiziksel olarak üretmeden önce zihninde 3 boyutlu çalıştırıp aşınma paylarına kadar test etme yeteneği.

---

## 🧠 ZİHİNSEL MODELLER VE POLİMATİK DÜŞÜNCE ALET ÇANTASI

Modern polimatın zihinsel alet çantasında yer alan temel akıl yürütme modelleri:

| Zihinsel Model | Açıklama | Temsilci Düşünür |
| :--- | :--- | :--- |
| **First Principles (İlk İlkeler)** | Bir problemi kabullerden değil, temel doğa gerçeklerinden sıfırdan kurma | Aristoteles, Elon Musk |
| **Second-Order Thinking** | "Ve sonra ne olacak?" sorusuyla kararların dolaylı sonuçlarını analiz etme | Howard Marks, Frédéric Bastiat |
| **Inversion (Tersine Çevirme)** | Başarıyı nasıl elde edeceğini değil, başarısızlıktan nasıl kaçınacağını planlama | Carl Jacobi, Charlie Munger |
| **Systems Thinking (Sistem Düşüncesi)** | Parçaları değil, aralarındaki geri besleme döngülerini ve dinamikleri anlama | Norbert Wiener, Donella Meadows |
| **Occam's Razor (Ockham'ın Usturası)** | Eşit geçerlilikteki hipotezlerden en az varsayım içerenini tercih etme | William of Ockham |
| **Antifragility (Antikırılganlık)** | Şok ve stres altında kırılmak yerine güçlenen yapılar inşa etme | Nassim Nicholas Taleb |
| **Pareto İlkesi (80/20 Kuralı)** | Sonuçların %80'inin girdilerin %20'sinden kaynaklandığı kaldıraç odağı | Vilfredo Pareto |
| **Circle of Competence** | Gerçekte bildiğin ile bildiğini sandığın arasındaki sınırı net çizme | Warren Buffett, Richard Feynman |

---

## 📜 POLİMATIN 10 EPİSTEMİK AKSİYOMU

1. **Aksiyom I — Evrensel Bütünlük:** Hiçbir disiplin izole bir ada değildir; tüm bilimler, sanatlar ve teknikler aynı hakikat ağacının dallarıdır.
2. **Aksiyom II — İlk Prensipler Sadakati:** Ezberlenmiş analogiler yerine sistemin en temel aksiyomlarına inerek düşünün.
3. **Aksiyom III — Bimodal Yetkinlik:** Sol beynin analitik kesinliği (kod, matematik, fizik) ile sağ beynin sentetik derinliğini (felsefe, estetik, dil) birleştirin.
4. **Aksiyom IV — Yüksek Kaldıraç:** Zamanınızı sıfır marjinal maliyetle çoğaltılabilen bilgi, kod, medya ve sistem sermayesine yatırın.
5. **Aksiyom V — Antikırılgan Zihin:** Hataları felaket değil, veri kaynağı olarak konumlandırın; belirsizlikten güç kazanın.
6. **Aksiyom VI — Pratik Olmayan Bilgi Ölüdür:** Sadece tüketici değil, daima prototipleyen, üreten ve inşa eden bir solopreneur olun.
7. **Aksiyom VII — Zihinsel Netlik ve Sadelik:** Bir fikri 10 yaşındaki bir çocuğa basitçe anlatamıyorsanız, onu henüz tam kavramamışsınızdır.
8. **Aksiyom VIII — Stoik Zihinsel Hakimiyet:** Dış gürültüyü, sosyal onay arayışını ve geçici dikkat tuzaklarını susturun; derin odaklanmaya (Deep Work) sığının.
9. **Aksiyom IX — Sürekli Not Alma ve İkinci Beyin:** Zihninizi depolama alanı değil, fikir üretme fabrikası olarak kullanın; bilginizi bağlamsal bir ağda arşivleyin.
10. **Aksiyom X — Alçakgönüllü Merak:** Ne kadar çok bilirseniz bilin, bilmediklerinizin okyanusunda bir damla olduğunuzu unutmayın.

---

## ⚙️ SİSTEMATİK YAPI: 7-KADEMELİ STANDARTLAŞTIRILMIŞ PROTOKOL (00-06)

UAOS bünyesindeki her bir bilgi düğümü, çıraklıktan bağımsız üretim ustalığına kadar uzanan 7 kademeli bir omurga ile yönetilir:

> [!TIP]
> **Bilişsel Yolculuk:** `Veri ➔ Enformasyon ➔ Kuram ➔ Pratik ➔ İleri Uzmanlık ➔ AR-GE / Sentez ➔ Bağımsız Üretim`.

```mermaid
graph LR
    A["00: Hazırlık & Dil"] --> B["01: Teorik Temeller"]
    B --> C["02: Alan Dersleri"]
    C --> D["03: İleri Uzmanlık"]
    D --> E["04: AR-GE & Sentez"]
    E --> F["05: Lisansüstü & Kariyer"]
    F --> G["06: Standartlar & Hakimiyet"]
    style A fill:#00A9E0,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#D4AF37,stroke:#333,stroke-width:2px,color:#000
```

1. **`00 — Akademik Hazırlık ve Dil`**: Terminoloji, metodolojik kurulum ve küresel dil yetkinliği.
2. **`01 — Temel Bilimler ve Giriş`**: Aksiyomatik prensipler, doğa kanunları ve kuramsal omurga.
3. **`02 — Alan Dersleri ve Pratik`**: Disiplinin çekirdek müfredatı, laboratuvar ve problem çözümleri.
4. **`03 — Seçmeli & İleri Uzmanlık`**: Niş alanlar, derinleşme modülleri ve mikro-uzmanlıklar.
5. **`04 — Araştırma, AR-GE ve Sentez`**: Özgün projeler, açık kaynak kodlama ve Proof-of-Concept üretimi.
6. **`05 — Lisansüstü ve Akademik Kariyer`**: Literatür taraması, tez çalışmaları ve akademik yayın hazırlığı.
7. **`06 — Sertifikasyon ve Endüstriyel Standartlar`**: Uluslararası akreditasyonlar, ISO/IEEE normları ve sektörel yetkinlik.

---

## 📖 THE UNIVERSAL DISCIPLINE MATRIX ({total_depts} BÖLÜM / {total_tiers} KADEME)

Tüm akademik ve profesyonel disiplinler açık, doğrudan erişilebilir ve yapılandırılmış 3-sütunlu ızgarada listelenmiştir.

</div>

"""

    # Build container sections
    body = ""
    for folder, meta in CONTAINERS.items():
        title = meta['title']
        quotes = meta['quotes']
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"### {title} ({len(depts)} Alan)\n\n"
        for q in quotes:
            section += f"> *{q}*\n\n"
        
        section += "|   |   |   |\n"
        section += "| :--- | :--- | :--- |\n"
        
        cols = 3
        for i in range(0, len(depts), cols):
            row_depts = depts[i:i+cols]
            row_cells = []
            for d in row_depts:
                dept_name = format_dept_name(d)
                link = f"[{dept_name}](./{folder}/{d}/)"
                row_cells.append(link)
            while len(row_cells) < cols:
                row_cells.append(" ")
            section += f"| {' | '.join(row_cells)} |\n"
            
        section += "\n---\n\n"
        body += section

    footer = f"""<div align="center">

## 🧠 SİSTEMATİK ÖĞRENME & BİLİŞSEL KALDIRAÇ METODOLOJİLERİ

Bu kütüphanedeki verimi en üst düzeye çıkarmak için kanıtlanmış bilişsel metodolojileri uygulayın:

*   **Zettelkasten & İkinci Beyin (PKM):** Notlarınızı izole depolamak yerine çift yönlü bağlantılarla (bidirectional links) birbirine bağlayarak disiplinlerarası yeni sentezler üretin.
*   **Feynman Tekniği:** Bir konuyu gerçekten anlamak için, onu en temel diliyle, analojilerle ve karmaşık terimlerden arındırarak 10 yaşındaki birine anlatır gibi açıklayın.
*   **Aralıklı Tekrar (Spaced Repetition & Anki):** Belleğin Ebbinghaus unutma eğrisini yenmek için bilgiyi genişleyen zaman aralıklarında aktif olarak geri çağırın (active recall).
*   **İlk Prensiplerden Çözümleme (First Principles):** Karmaşık sistemleri en temel doğrularına ve fizik kanunlarına indirgeyip sıfırdan inşa edin.
*   **Derin Çalışma (Deep Work & Monk Mode):** Dikkat dağıtıcı uyaranları tamamen susturarak bilişsel akış (Flow State) durumunda kesintisiz odak blokları oluşturun.
*   **Solopreneur Kaldıraç Matrisi:** Öğrendiğiniz her soyut teoriyi, sıfır marjinal maliyetle çoğaltılabilen yazılıma, açık kaynak araca veya dijital esere dönüştürün.

---

## 🗺️ PROJE YOL HARİTASI (ROADMAP)

- [x] **Faz 1:** Temel mühendislik ve bilim disiplinlerinin 7-kademeli iskeletinin oluşturulması.
- [x] **Faz 2:** Universal Discipline Matrix ({total_depts} Akademik Alan / {total_tiers} Kademe) entegrasyonu.
- [x] **Faz 3:** CI/CD otomatik repo bütünlüğü ve indeks doğrulama test hattı.
- [x] **Faz 4:** Polimatik zihinsel modeller, düşünürler panteonu ve felsefi aksiyomların mimariye kazandırılması.
- [x] **Faz 5:** İnteraktif CLI arama motoru ve 20 derin akademik araştırma monografı (`scripts/search_curriculum.py` & `assets/curriculum_index.json`).
- [ ] **Faz 6:** Uluslararası çok dilli akademik genişleme.

---

## ❓ SIKÇA SORULAN SORULAR (SSS)

**S: Neden bu kadar geniş ve çok disiplinli bir yapı kuruldu?**  
**C:** Çünkü gerçek dünya ve çığır açan keşifler tek bir alana sıkışmış değildir. Tıbbı yapay zekayla, hukuku bilişimle, mühendisliği felsefeyle sentezleyebilen "T-Tipi" ve "Pi-Tipi" polimat zihinler geleceğin egemen bireyleri olacaktır.

**S: İçerikler tamamen açık kaynak ve ücretsiz mi?**  
**C:** Evet, tüm sistem **MIT Lisansı** altında korunmakta olup, bilgiye erişim evrensel bir insanlık hakkıdır.

**S: Bir disiplini çalışırken 7 kademeyi nasıl takip etmeliyim?**  
**C:** `00` ile terminoloji ve dil hazırlığını tamamlayın; `01` ve `02` ile teorik ve çekirdek müfredatı hazmedin; `03` ile niş alanlarda derinleşip `04` ve `06` ile somut açık kaynak projeler ve endüstriyel sertifikasyonlarla süreci taçlandırın.

---

## 🤝 KATKIDA BULUNMA
Bu kütüphane kolektif aklın ve açık bilimin bir tezahürü olarak büyümektedir. Katkı sağlamak için [CONTRIBUTING.md](./CONTRIBUTING.md) rehberini inceleyebilir ve Pull Request gönderebilirsiniz. Topluluk normları için [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) belgesine bakabilirsiniz.

---

## ⚖️ YASAL YÖNETİŞİM VE LİSANS
Bu proje **MIT Lisansı** altında lisanslanmıştır. Bilgi insanlığın ortak mirasıdır. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.

**Mimari ve Tasarım**  
### Bahattin Yunus Çetin  
*Yazılım Mühendisi & Araştırmacı*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bahattinyunuscetin) 
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bahattinyunus)

---
> *“Bilgi arayışı; merakla beslenen, akılla terbiye edilen ve hakikatle taçlanan sonu olmayan kutlu bir yolculuktur.”*

---
© 2024-2026 Evrensel Akademik İşletim Sistemi (UAOS).
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'readme.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"readme.md generated successfully. Total: {total_depts} depts, {total_tiers} tiers in 3-column open grid with rich quotes.")

if __name__ == "__main__":
    generate_encyclopedic_readme()
