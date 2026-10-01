import random


class Story:

    # Sınıf seviyesindeki liste için şablon olduğunu net belirten isim
    story_templates = [
    # 1. Klasik Absürt / Ajan
    "Gizli ajan {name}, {city} sokaklarında elinde {item} ile tam havaya girmiş devriye gezerken, çalıların arasından terlikli bir {animal} fırlayıp çantayı kaptı ve arkasına bile bakmadan kaçtı!",
    # 2. Temel & Dursun Tarzı Fıkra
    "Temel ile {name}, {city} sahilinde dertleşirken uzaktan koşarak gelen bir {animal} gördüler. {name} panikle elindeki {item} nesnesini fırlattı ama {animal} bunu oyun sanıp {item} ile geri geldi!",
    # 3. Nasreddin Hoca Tarzı Fıkra
    "Bir gün Nasreddin Hoca ile {name}, {city} pazarında gezerken satıcının biri dev bir {animal} gösterip 'Bu hem konuşur hem de {item} tamir eder!' dedi. {name} cebindeki tüm parayı basıp hayvanı aldı ama evde sadece miyavladı.",
    # 4. Belediye / Bürokrasi Komedisi
    "{city} belediyesi, {name} onuruna meydana dev bir {animal} heykeli dikti. Açılış günü kordonu kesmek yerine heykelin eline hediye olarak kocaman bir {item} tutuşturdular, millet alkıştan yıkıldı!",
    # 5. Sirk Kasosu
    "Ünlü sirke katılan {name}, tam gösterinin ortasında yanlışlıkla elindeki {item} nesnesini düşürdü. Bunu gören hipnoz olmuş {animal} panikleyip doğruca {city} trafiğine daldı!",
    # 6. Antik Eşya / Cin Mantığı
    "{name}, {city} bitpazarından pazarlıkla ucuz bir {item} satın aldı. Evde bezle ovalarken içinden dumanlar çıktı ama cin yerine uykusu bölünmüş sinirli bir {animal} fırladı!",
    # 7. Garip Haberler
    "Bir sabah {city} haberlerinde şok iddia: {name} adındaki bir vatandaşın, dev bir {animal} sırtında elinde {item} sallayarak kırmızı ışıkta geçtiği görüldü!",
    # 8. Metro / Toplu Taşıma
    "{city} metrosunda seyahat eden {name}, koltukta elindeki {item} nesnesini unuttu. Neyse ki arkadan gelen gözlüklü bir {animal} eşyayı kapıp 'Hemşerim eşyanı unuttun!' diye peşinden koştu.",
    # 9. Dedektif Parodisi
    "Dünyanın en sakar dedektifi {name}, {city} müzesinden çalınan paha biçilemez {item} izini sürerken tek ana şüphelinin şapka takmış eğitimsiz bir {animal} olduğunu fark etti!",
    # 10. Kamp / Doğa Macerası
    "{city} ormanlarında kamp yapan {name}, gece çadırının önünde dev bir {animal} gördü. Onu korkutup kaçırmak için elindeki {item} ile tenekeye vurur gibi ses çıkardı ama {animal} ritme ayak uydurup göbek atmaya başladı!",
    # 11. Çılgın Profesör
    "Çılgın profesör {name}, {city} laboratuvarında genetik deney yaparken tüpe yanlışlıkla {item} düşürdü. Sonuç: Şerbetli tatlı hastası devasa bir {animal} klonlandı!",
    # 12. Yerli Süper Kahraman
    "Mahallenin gururu süper kahraman {name}, {city} halkını kurtarmak için sahneye çıktı. En büyük kozu ise sihirli bir {item} ve mahalleden topladığı sadık dostu bir {animal} idi!",
    # 13. Bektaşi / Nükte Hikayesi
    "Bektaşi ile {name}, {city} sıcaklarında bir ağaç altında otururken yanlarına aç bir {animal} geldi. {name} hemen elindeki {item} nesnesini uzatıp 'Ye mübarek' dedi, hayvan koklayıp arkasını döndü.",
    # 14. Düğün / Halay Kaosu
    "{city} merkezindeki bir sokak düğününde {name}, elindeki {item} ile halay başı çekiyordu. Aniden çalgıcıların arasından çıkan bir {animal} mendili kapıp halayın başına geçti!",
    # 15. Esnaf Lokantası
    "{city} esnaf lokantasında {name}, garsona 'Bize bir {item} getir' dedi. Garson tabağı getirdiğinde içinden canlı bir {animal} kafasını çıkarıp 'Afiyet olsun hemşerim' dedi!",
]

    def __init__(self, name, item, animal, city):
        self.name = name
        self.item = item
        self.animal = animal
        self.city = city

    def generate_story(self):
        """Rastgele bir şablon seçer ve verilerle doldurarak hikayeyi döndürür."""
        selected_template = random.choice(self.story_templates)

        formatted_story = selected_template.format(
            name=self.name,
            item=self.item,
            animal=self.animal,
            city=self.city,
        )

        return formatted_story


# Kullanıcı girdileri
character_name = input("Character name: ")
target_item = input("Object/Item name: ")
animal_type = input("Animal: ")
city_name = input("City: ")

# Nesne oluşturma ve çalıştırma
story_generator = Story(
    name=character_name,
    item=target_item,
    animal=animal_type,
    city=city_name,
)

print("\n--- Oluşturulan Hikaye ---")
print(story_generator.generate_story())