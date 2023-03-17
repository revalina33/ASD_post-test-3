# ASD_post-test-3

Pada program pembelian pulsa ini terdapat 2 pengguna,yaitu user dan admin.pada menu admin terdapat pilihan beli pulsa dan menampilkan Riwayat pembelian pulsa,pada menu admin terdapat pilihan menghapus Riwayat pembelian pulsa yang di lakukan user,menampilkan Riwayat pembelian yang dilakukan user dan mencari tanggal pembelian melalui jumlah pulsa yang dibeli.
Pada program ini terdapat class purchase dan purchasehistory yang digunakan untuk merekam pembelian pulsa.  Pada class purchase terdapat timestamp dan amount (jumlah pulsa). selanjutnya pembelian yang dilakukan oleh user tesebut akan ditambahkan ke dalam purchasehistory menggunakan metode add_purchase.dengan adanya metode add_purchase maka setiap kali user melakukan pembelian pulsa Riwayat tersebut akan tersimpan/di tambahkan ke dalam linked list.dengan adanya Riwayat pembelian tersebut user dapat melihat Riwayat pembelian pulsa yang pernah dilakukan. Untuk menampilkan Riwayat tersebut dapat menggunakan metode print_history,maka program akan menampilkan Riwayat pembelian.
Pada program menu admin terdapat fitur menghapus pembelian pulsa,pada fitur ini program akan menghapus data sesuai dengan data yang pertama masuk/di input oleh pengguna menggunakan metode deque,lalu data akan ditampilkan menggunakan display.dalam program bagian admin ini juga terdapat fitur mencari Riwayat pembelian berdasarkan jumlah/nominal pulsa yang dicari,jika jumlah pulsa yang dimasukan sama dengan pulsa yang ada di dalam Riwayat pembelian maka program akan menampilkan tanggal dari transaksi tersebut.

**OUTPUT**

**Menu user**



![image](https://user-images.githubusercontent.com/126893682/225895780-c83fac3c-4528-43e9-b3e7-61d7cbfee06c.png)

Diatas merupakan tampilan pada menu user jika user memilih angka satu maka akan tampil jumlah pulsa yang ingin dibeli,setelah melakukan pembelian maka program akan menampilkan pertayaan apakah ingin membeli pulsa lagi jika user menginput y maka user akan diminta memasukkan jumlah pulsa yang ingin dibeli lagi ,tetapi jika user memilih t maka program akan Kembali ke tampilan menu pembeli.


![image](https://user-images.githubusercontent.com/126893682/225895908-1f4af5af-155f-4cb0-a0f1-282e81feb049.png)


Jika user memilih angka 2 maka program akan menampilkan tanggal dan jumlah transaksi pulsa tersebut terjadi.



**ADMIN**


![image](https://user-images.githubusercontent.com/126893682/225896066-d8ddce18-44be-48a0-97dc-4d40ea8ddaf2.png)


Untuk menampilkan Riwayat pembelian pulsa yang sudah dilakukan oleh admin user dapat memilih pilihan 2.

![image](https://user-images.githubusercontent.com/126893682/225896129-c86eeea4-1fd4-4f00-b976-10b30d1c06b2.png)


Untuk menghapus data admin bisa memilih pilihan ke 1,maka program akan menghapus data pada Riwayat pembelian user.program tersebut menggunakan FIFO(First in First Out),jadi data yang masuk di awal program akan dihapus pertama.


![image](https://user-images.githubusercontent.com/126893682/225896206-141e596a-3341-4531-9a46-bdd87afc0191.png)

 
Untuk mencari Riwayat pembelian pulsa berdasarkan nominal pulsa admin dapat memilih pilihan 3 lalu menginput jumlah pulsa yang ada di dalam Riwayat.jika tidak maka akan tampil tulisan Riwayat pulsa tidak di temukan.
