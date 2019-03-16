belanja = int(input("Total Belanja : Rp."))
bayar	= int(input("Masukan uang : Rp."))
kembalian = bayar-belanja
print ("Kembalian Rp.",kembalian,"dengan rincian")
uang=[500, 1000, 2000, 5000, 10000, 20000, 50000]

for x in range (0,10):
	i=0
while kembalian >= uang[x]:
	kembalian = kembalian - uang[x]
	i = i+1
if(i>0):
	print("Uang Rp.%d sebnyak %d lembar" %(d[x], i))
else:
	print("Selesai")
