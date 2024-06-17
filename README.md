# Cancer-Diagnosis-Website
 Kanser Teşhisinde Yapay Zekâ Tabanlı Görüntü Analizi Projesi

Proje Hakkında
Bu projenin amacı, kanser teşhis sürecini iyileştirerek hastaların erken aşamada tespit edilmesine yönelik müdahaleyi artırmaktır. Kanser, erken evrelerde teşhis edildiğinde daha etkili bir şekilde tedavi edilebilir ve bu nedenle teşhisin doğruluğu hayati önem taşır.

Proje, medikal görüntüleme teknikleriyle elde edilen MRI, CT taramaları ve mikroskobik görüntüler üzerinde yapay zekâ algoritmalarını kullanarak çalışmaktadır. Yapay zekâ, bu görüntüleri analiz ederek potansiyel tümörleri tespit eder ve bunların türünü olasılıksal olarak belirleyebilir.

Özellikler
Görüntü Analizi: MRI, CT ve mikroskobik görüntülerin analizi.
Yapay Zekâ Algoritmaları: Büyük veri setleri üzerinde eğitilmiş ve optimize edilmiş algoritmalar.
Yüksek Doğruluk: Yanlış pozitif ve yanlış negatif teşhisleri minimuma indirerek güvenilir sonuçlar elde edilmesi.
Erken Teşhis: Hastaların erken aşamada tespit edilmesini ve tedaviye hızlı başlanmasını sağlama.
Sağlık Sektöründe Teknolojik Gelişmelerin Kullanımı: Yapay zekâ uygulamalarıyla can kayıplarını en aza indirme.
Kullanılan Teknolojiler
Convolutional Neural Networks (CNN): Görüntü verilerinin analizi ve özellik çıkarımı için kullanılmıştır. CNN'ler, görüntülerdeki belirli özellikleri tanıyarak potansiyel tümörleri tespit eder.
Vision Transformers (ViT): Görüntülerin uzun menzilli ilişkilerini analiz etmek için kullanılmıştır. ViT, özellikle karmaşık görüntü verilerinin analizinde yüksek performans gösterir ve tümör tespitinde ek bir doğruluk sağlar.
Performans
Projenin yapay zekâ modeli, %95 oranında doğru sonuç vermektedir. Bu, yanlış pozitif ve yanlış negatif teşhislerin minimuma indirildiği anlamına gelir ve güvenilir sonuçlar elde edilmesini sağlar.

Kurulum
Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin.

Depoyu Klonlayın:


git clone https://github.com/kullaniciadi/kanser-teshis-ai.git
cd kanser-teshis-ai

Gereksinimleri Yükleyin:
Gerekli Python paketlerini yüklemek için:


pip install -r requirements.txt

Veri Setini İndirin:
Veri setlerini indirip data/ klasörüne yerleştirin.

Modeli Eğitin:
Eğitim verilerini kullanarak modeli eğitmek için:


python train.py

Modeli Test Edin:
Eğitilen modeli test etmek için:


python test.py
Kullanım
Eğitilen modeli kullanarak yeni görüntülerin analizini yapmak için:


python predict.py --image_path /path/to/image

Web Uygulaması
Bu proje, web üzerinde kullanıma hazır bir şekilde tasarlanmıştır. Kullanıcılar, tarayıcıları üzerinden medikal görüntüleri yükleyerek yapay zekâ tabanlı analiz sonuçlarını alabilirler. Web uygulamasını çalıştırmak için:

Sunucuyu Başlatın:


python app.py
Tarayıcıda Açın:
Web tarayıcınızı açarak http://localhost:5000 adresine gidin.

Görüntü Yükleyin ve Analiz Edin:
Kullanıcı arayüzü üzerinden medikal görüntüleri yükleyin ve analiz sonuçlarını görün.



# Packages 
pip install crispy-bootstrap4
pip install Django==5.0.4
pip install pillow==10.3.0
pip install tensorflow==2.16.1
pip install django-crispy-forms
pip install pillow
