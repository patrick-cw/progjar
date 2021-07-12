from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime
from multiprocessing import Process

def kirim_semua():
    texec = dict()
    urls = get_url_list()
    x = 0
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k],k)
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        UDP_IP_ADDRESS = "192.168.122.235"
        UDP_IP_ADDRESS2 = "192.168.122.107"
        if x == 0:
            texec[k] = Process(target=kirim_gambar, args=(UDP_IP_ADDRESS,5050,f"{k}.jpg"))
            print('Entered Server 1 ')
            x = x + 1
        elif x == 1:
            print('Entered Server 2')
            texec[k] = Process(target=kirim_gambar, args=(UDP_IP_ADDRESS2,5050,f"{k}.jpg"))
        texec[k].start()
    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in urls:
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
#fungsi download_gambar akan dijalankan secara multi process
if __name__=='__main__':
    kirim_semua()
