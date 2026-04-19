import socket

s = socket.socket() #TCP nad IPv4 po default-u
# s -> socket servera
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#SOL_SOCKET ->
#SO_REUSEADDR ->
s.bind(('0.0.0.0', 2026))
#bind -> da bi socket primio poruke koje mu stizu mora prvo da se poveze za neku lokalnu adresu
#127.0.0.1 -> ip localhost-a, koristi se za testiranje na kompjuterima
s.listen(1)
#s.listen(1) -> On definiše dužinu queue zaostatka, što je broj dolaznih veza koje su završene od strane
# TCP/IP steka, ali još uvek nisu prihvaćene od strane aplikacije.
#1 -> duzina vec spomenutog queue

c, addr = s.accept()
#c -> veza sa klijentom; addr -> adresa klijenta
print("Povezao se klijent", addr)
print("Gasimo sve konekcije...")
c.close()
#c.close() -> zatvara konekciju sa klijentom
s.close()
#s.cloes() -> zatvara server