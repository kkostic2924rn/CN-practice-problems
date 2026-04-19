import socket

#ovo je uvek isto:
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2026))
s.listen(5)

while True:
    try:
        c, addr = s.accept()
        print('Povezao se klijent', addr)

        #za slanje podataka se koristi:
        #  send - salje sve podatke koje u tom trenutku moze da stavi u bafer
        #  sendall - radi sve isto kao i send, ali salje podatke deo po deo dok ne posalje sve
        #  sendto (bajtovi, adresa) - salje odredjenoj adresi
        #  sendfile - salje fajl direktno na mreznu karticu i preskace slanje na RAM pa u kod pa na karticu
        c.sendall('Dobrodosli na server'.encode())
        #.encode() -> enkriptuje podatke koji treba da se posalju
        data = c.recv(1024)
        #recv = recieve; 1024 - maksimalna kolicina bajtova
        poruka = data.decode()
        print('Poruka klijenta', poruka)

        c.sendall(f'Primio sam [{poruka}]'.encode())
    except (OSError, socket.error) as e:
        print('Greska', e)
    except Exception as e:
        print('Neocekivana greska', e)
    finally:
        print('Gasimo konekciju ka klijentu')
        c.close()
    if poruka == 'kraj':
            break

print('Gasimo server...')
s.close()