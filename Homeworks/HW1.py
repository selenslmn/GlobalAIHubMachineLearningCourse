# Homework 1

#Question 1
"İstatistiksel işlemler ile veriler üzerinden çıkarımlar yaparak tahminlerde bulunan sistemlerin bilgisayarlar ile modellenmesidir."

#Question 2
"Denetimli Öğrenmede etiketlenmiş veriler kullanılır, eğitim verisi hem girdilerden hem de çıktılardan oluşur, veri setindeki çıkışlar kategorik ise sınıflandırma nümerik ise regresyon algoritmaları kullanılır."
"Denetimsiz Öğrenmede ise etiketlenmemiş veriler üzerinden bilinmeyen bir yapıyı tahmin etmek için bir algoritma kullanan makine öğrenmesi tekniğidir, burada giriş verisinin hangi sınıfa ait olduğu belirsizdir."
"Denetimli Öğrenme algoritmalarına k-en yakın komşu, karar ağaçları ve lojistik regresyonu örnek verebiliriz."
"K-en yakın komşu: k bir veri kümesindeki sonuçları sınıflandırmak veya tahmin etmek için kullanılan en yakın komşuların sayısını ifade eder. \n" 
"Her yeni gözlemin sınıflandırması veya tahmini, ağırlıklı ortalamalara göre belirlenen bir mesafeye (yani En Yakın Komşu) göre hesaplanır."
"Karar Ağaçları: Bir karar ağacı, çok sayıda kayıt içeren bir veri kümesini, bir dizi karar kuralları uygulayarak daha küçük kümelere bölmek için kullanılan bir yapıdır. \n"
"Yani basit karar verme adımları uygulanarak, büyük miktarlardaki kayıtları, çok küçük kayıt gruplarına bölerek kullanılan bir yapıdır."
"Lojistik regresyon: Sonuç, ikili bir değişkenle ölçülür (1-0, yalnızca iki olası sonuç vardır). \n"
"Bağımlı değişken ile ilgili bir dizi bağımsız değişken arasındaki ilişkiyi tanımlamak için en uygun modeli bulmaktır."
"Denetimsiz Öğrenme algoritmalarına K-kümeleme, Hiyerarşik kümeleme ve kohonen ağları örnek verebiliriz."
"K-kümeleme: K değeri küme sayısını belirler ve bu değeri parametre olarak alması gerekir. Rastgele K tane merkez noktası seçer. \n" 
"Her veri ile rastgele belirlenen merkez noktaları arasındaki uzaklığı hesaplayarak veriyi en yakın merkez noktasına göre bir kümeye atar. \n" 
"Bu durum sistem kararlı hale gelene kadar devam eder."
"Hiyerarşik kümeleme: ilk önce tüm veriler bir küme haline getirilir yani N tane eleman varsa N tane küme oluşur. \n"
"Daha sonra birbirine mesafe olarak yakın olan kümeler birleşerek yada parçalanarak yeni bir küme oluşturur. Bu durum sistem kararlı oluncaya kadar devam eder." 
"Kohonen ağları: Bu tür sinir hücrelerinin kendilerini belirli girdi değerlerini göre düzenleyerek bir özellik haritası çıkartmasıyla oluşur. \n"
"Tek katmanlı bir ağ olup giriş ve çıkış nöronlarından oluşur. Giriş nöronlarının sayısını veri setindeki değişken sayısı belirler, Çıkış nöronlarının her biri bir kümeyi temsil eder."

#Question 3
"Eğitim seti: Modelin eğitildiği veri kümesidir. \n
Test seti: Bir eğitim kümesinde geliştirilen modeli değerlendirmek için kullanılan bir veri kümesidir. \n
Doğrulama seti: Modelin üzerinde eğitim alınmamış ve hiperparametreleri ayarlamak için kullanılan veriler. \n 
"Modelleme veya tahminlemede bulunmadan önce veri setimizi bir eğitim ve test setine ayırmalıyız. Böylelikle eğitim seti üzerinde modelimizi eğitir ve test seti üzerinde tahminler yapabiliriz. \n
Eğitim setimiz büyüdükçe modelimiz daha iyi öğrenecektir. Test setimiz büyüdükçe ise değerlendirme metriklerimize daha iyi güvenebileceğimiz daha sıkı güven aralıklarımız olacaktır. \n
Doğrulama seti ile her eğitim sonunda model etkinliğini test edip nihai modele karar verdikten sonra test seti ile test ederek modelimizin etkinliği daha sağlıklı bir şekilde gözlemleyebiliriz."

#Question 4
"Veri Ön İşleme veri setinin model eğitimine hazır hale getirilmesine ilişkin tüm adımları içerir. \n"
"-Duplicate Values: Tekrarlayan verilerin silinmesi, \n
-Dengesiz Veri(Imbalanced Data): Veride sınıfların dengesiz dağıldığını ve bunun da çoğunluk sınıftan yana sapmaya yol açtığı için bunu düzeltmek gerek. \n
-Kayıp Veriler: Hemen hemen her veri setinde çıkar. Çünkü veri tabiatı itibariyle kötüdür. Verilerin dağılımına göre ortadan kaldırılır yada ortalama veya medyan ile doldurulur. \n
-Outlier detection: Aykırılık yaratan verilerin tespiti yapılır. İstatistiksel yöntemler veya makine öğrenmesi yöntemleri kullanılır. \n
-Feature Scaling: Değişkenleri makine öğrenmesi algoritmalarına sokmadan önce belirlediğimiz aralıklara indirgiyoruz. En Çok Kullanılan Feature Scaling Türleri; \n
Standardization: Değişkenleri, ortalaması 0 std sapması 1 olan bir dağılıma çeviriyor . Veri setindeki tüm verilerden ilgili sütun ortalaması çıkartılıp yine sütun std sapmasına bölünerek bulunuyor. Böylelikle veri setindeki tüm gözlem birimleri -1 ile 1 arasında değer almış oluyor. \n
Normalization: Veri setindeki her bir değeri, ilgili sütundaki min max değerlere göre ölçeklendiriyor. Verileri 0–1 arasına çeker. \n
Robust Scaler: Outlierlara karşı robust olan IQR istatistiğine göre veri seti ölçeklendiriliyor. Not: IQR= Q3-Q1 \n
-Feature selection: Model eğitiminde kullanılacak verilere karar verilir. Problemi çözmek için gereksiz ve problemin çözümüne etkisi olmayan özellikleri tespit ederek bunları kullanmamaktır. \n
Gereksiz özellikler gereksiz korelasyonlar oluşturur ve modelin genellenebilirliğini zayıflatır. Özellik seçimi ayrıca aşırı öğrenme (overfitting) olasılığını da azaltır, \n
model eğitiminde gereksiz kaynak tüketiminin önüne geçer. Daha az özellik, daha anlaşılır ve yorumlanır modellerin oluşturulmasını sağlar."
"-Bucketing(Binning): Gürültülü verilerin etkilerini en aza indirmek için kullanılır. \n
Orijinal veri değerleri, küçük aralıklara bölünür ve daha sonra bu bölme için hesaplanan genel bir değerle değiştirilir. \n
-Feature Extraction: Nitelik çıkarımı orijinal nitelikleri karıştırarak yeni ancak gereksiz olmayan değişkenler elde edilmesini sağlar. \n
-Feature Encoding: Çeşitli kodlama yöntemlerini içerir. Veriler üzerinde, orijinalliğini korurken makine öğrenimi algoritmaları için kolayca girdi olacak şekilde dönüşümler gerçekleştirmektir. \n
-Train/Validation/Test split: Hangi algoritmanın kullanılması gerektiğine karar vermeden önce her zaman veri setini 2 veya bazen 3 parçaya bölmek tavsiye edilir. \n
Makine Öğrenimi algoritmaları veya bu konudaki herhangi bir algoritma, gerçek dünya verileriyle başa çıkmak için dağıtılmadan önce önce mevcut veri dağıtımı konusunda eğitilmeli ve ardından doğrulanmalı ve test edilmelidir. \n
-Cross Validation: Makine öğrenmesi modelinin görmediği veriler üzerindeki performansını mümkün olduğunca objektif ve doğru bir şekilde değerlendirmek için kullanılan istatistiksel bir yeniden örnekleme yöntemidir."

#Question 5
"Sürekli: Bir aralıktaki tüm değerleri alabilen verilerdir. Reel sayılar ile ifade edilir. Değerler ölçülerek elde edilir. Histogram grafiği ile ifade edilebilir. (Örn: Boy, ağırlık, sıcaklık) \n
Kesikli: Sayılabilen türdeki verilerdir. Tam sayılar ile ifade edilirler. Değerler sayılarak elde edilir. Bar grafiği ile ifade edilebilir. (Örn: Medeni durum, cinsiyet, kardeş sayısı)"

#Question 6
"Kitle, örneklem, gözlem birimi, değişken, değişken türleri, ölçek türleri, merkezi eğilim ölçüleri, dağılım ölçüleri, vb."

#Question 7
"Grafik: Normal dağılım grafiği \n
Değişken türü: Sayısal(nicel) değişken, sürekli \n
Dağılımı: Sağa(pozitif) çarpık \n
Ön işlemler: Ortalama ve medyan birbirinden uzaktır ve aykırı değerler olabilir. Bu yüzden keyıp veriler medyan kullanılarak doldurma yapılabilir. \n
Standardizasyon işlemi yapılarak ölçeklendirebiliriz. "
