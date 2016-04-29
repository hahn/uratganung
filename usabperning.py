import os, sys
import suku

vokal = ['a', 'i', 'u', 'e', 'o']

def fUsabPerning(kata):
	kata = kata.lower()
	v_ganti1 = ''
	v_ganti2 = ''

	katanya = suku.pecah(kata)
	panjang = len(katanya)
	x = ''
	# print "kata: " + kata
	# print "panjang: ", panjang
	if(panjang == 2):
		
		#ambil vokal di sukukata2
		for j in katanya[1]:
			isVokal = (j in vokal)
			if isVokal:
				v_ganti2 += j

		#ganti vokal di sukukata2 dengan 'a'
		for v in vokal:
			katanya[1] = katanya[1].replace(v,'a')

		
		#tambah sukukata1 dengan v_ganti2 + 'ng'
		katakedua = katanya[0]
		# print katakedua[-1:]
		if katakedua[-1:] is 'n':
			katakedua = katakedua[:-1]
		#tambah u+v_ganti + vokal di sukukata2
		hasilnya = 'u' + katanya[1] + katakedua + 'n' + v_ganti2 + 'ng'

		#print 'u'+katanya[1] + katanya[0]+'ang'
	else:
		for i in range(0,panjang):
			x += katanya[i]
		hasilnya = x
	return hasilnya

if __name__=='__main__':
	# print len(sys.argv)
	for i in range(1,len(sys.argv)):
		kata = sys.argv[i]
		print fUsabPerning(kata), 
    # if len(sys.argv)>1:
    #     kata = sys.argv[1]
    #     print fUsabPerning(kata)