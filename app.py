import os
from prettytable import PrettyTable
import pandas as pd
import datetime as dt
import platform
import random

# Menghapus text sebelumnya
def clearTerminal():
	# Untuk sistem Windows
	if( platform.system() == "Windows" or platform.system() == "Win" ):
		clear = lambda: os.system('cls')
		clear()
	if( platform.system() == "Linux" ):
		clear = lambda: os.system('clear')
		clear()

# Menampilkan Daftar produk
def list_produk ():
    print('1. Hijab Pasmina : Rp. 25,000')
    print('2. Hijab Segi Empat : Rp. 20,000')
    print('3. Hijab Bergo : Rp. 18,000')

# Header Aplikasi
print("="*20)
print('BOUTIQUE HIJAB')
print("="*20)
print('')


# Input Tanggal
tanggal = int(input('Masukan Tanggal : '))
bulan = int(input('Masukan Bulan : '))
tahun = int(input('Masukan Tahun : '))

format_tanggal = dt.date(tahun, bulan, tanggal)

clearTerminal()

# Input banyaknya barang yang akan dibeli
jumlah_data = int(input('Berapa banyak barang yang akan dibeli? '))

clearTerminal()

# Daftar barang yang sudah dipilih
barang_terpilih = list()
# Jumlah barang yang sudah dipilih
banyak_barang = list()
# Harga per barang
harga_perbarang = list()

def pemesanan_ulang ():
	while (str(input('Apakah anda ingin memesan ulang? (Y/N) ' == 'Y'))):
		jumlah_data
		main()
	struk()

# Berapa banyak produk yang akan dibeli

'''Mulai Aplikasi'''

print("="*20)
print('BOUTIQUE HIJAB')
print("="*20)
print('')

# Menampilan Daftar Produk yang dimiliki
def main ():

	def struk():
		print("="*20)
		print('BOUTIQUE HIJAB')
		print("="*20)
		print(format_tanggal)

		# Table Jumlah Barang
		table = PrettyTable(['Nama Barang', 'Jumlah Barang', 'Total Harga'])
		for x in range(jumlah_data) :
			table.add_row([barang_terpilih[x], banyak_barang[x], harga_perbarang[x]] )
		print(table)

		# Table Total
		table2 = PrettyTable(['Total Harga Keseluruhan', f'{total_seluruh:,}'])
		print(table2)
		uang_buyer = int(input('> Jumlah uang yang dibayarkan : '))
		kembalian = uang_buyer - int(total_seluruh)
		print('Kembalian : ', f'{kembalian:,}')

	total = 0
	for i in range(jumlah_data):

		list_produk()
		print('Barang ke - ', i+1)
		barang_dibeli = str(input('> Masukan Barang yang akan dibeli : '))
		jumlah_beli = int(input('> M20asukan Jumlah Barang yang akan dibeli : '))
		banyak_barang.append(jumlah_beli)
			
		# Perhitungan harga barang
		if (barang_dibeli == '1') :
			harga_barang = 25000
			nama_barang = 'Hijab Pasmina'
			barang_terpilih.append(nama_barang)
			
		elif (barang_dibeli == '2' or barang_dibeli == 'Hijab Segi Empat') :
			harga_barang = 20000
			nama_barang = 'Hijab Segi Empat'
			barang_terpilih.append(nama_barang)
			
		elif (barang_dibeli == '3' or barang_dibeli == 'Hijab Bergo'):
			harga_barang = 18000
			nama_barang = 'Hijab Bergo'
			barang_terpilih.append(nama_barang)
			
		else :
			print('Maaf barang yang anda pilih tidak tersedia')
			while (str(input('Apakah anda ingin memesan ulang? (Y/N) ' == 'Y'))):
				jumlah_data
				main()
			struk()
		
		total_harga = int(harga_barang*jumlah_beli)
		harga_perbarang.append(total_harga)
		total_seluruh = total + int(total_harga)
		clearTerminal()

	struk()

main()
		















        
