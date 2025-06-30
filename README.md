🛡️ AegisSec Siber Güvenlik Takımı - Ağ ve Sızma Testi Projeleri
Bu repoda, takımımızın temel ağ keşfi, MAC adres değiştirme ve ARP zehirleme (spoofing) saldırısı için geliştirdiği Python scriptleri bulunmaktadır. Projeler, ağ güvenliği ve saldırı tespit/pratik çalışmalarında kullanılmak üzere hazırlanmıştır.

Projeler
1. ARP Zehirleme Saldırısı (ARP Spoofing)
Dosya: arp_spoof.py (örnek isimlendirme)

Hedef IP ve Gateway IP girilerek ARP zehirleme saldırısı yapılır.

Hedef ve ağ geçidi arasındaki ARP tabloları değiştirilerek trafik saldırgan üzerinden geçer.

Kullanıcı tarafından Ctrl+C ile durdurulduğunda ARP tabloları eski haline döndürülür.

Scapy kütüphanesi kullanılarak Ethernet ve ARP paketleri elle oluşturulur.

2. MAC Adres Değiştirme (MAC Changer)
Dosya: mac_changer.py

Kullanıcının belirttiği ağ arayüzünün MAC adresini değiştirir.

Linux sistemlerde ifconfig komutu ile ağ arayüzü önce kapatılır, yeni MAC atanır, sonra açılır.

Değişiklik başarılıysa kullanıcı bilgilendirilir.

Python subprocess ve re modülleri ile işletim sistemi komutları yönetilir.

3. Ağ Tarama (Network Scanner)
Dosya: network_scanner.py

Kullanıcının belirttiği IP aralığında ARP isteği göndererek ağdaki aktif cihazları keşfeder.

Cihazların IP ve MAC adreslerini listeler.

Scapy modülü kullanılarak Ethernet yayını ve ARP sorguları yapılır.

Kullanım
Ortak Gereksinimler
Python 3.x

scapy kütüphanesi (pip install scapy)

Çalıştırma Örnekleri
bash
Kopyala
Düzenle
python arp_spoof.py -t 192.168.1.5 -g 192.168.1.1
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
python network_scanner.py -i 192.168.1.0/24
Notlar
ARP zehirleme ve MAC değiştirme scriptleri için root yetkileri gerekebilir.

Ağ taraması IP aralığı doğru formatta girilmelidir (örneğin: 192.168.1.0/24).

Proje Amacı
AegisSec ekibi olarak temel ağ güvenliği tekniklerini öğrenmek, uygulamak ve takım içi bilgi paylaşımı yapmak için bu scriptleri geliştirdik. Gerçek saldırı/test ortamlarında dikkatli ve etik kurallar çerçevesinde kullanılması önemlidir.
