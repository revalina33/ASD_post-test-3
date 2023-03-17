import time 

class Purchase:
    def __init__(self, timestamp, amount):
        self.timestamp = timestamp
        self.amount = amount
        self.next = None

class PurchaseHistory:
    def __init__(self):
        self.head = None

    def add_purchase(self, amount):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_purchase = Purchase(timestamp, amount)
        if self.head is None:
            self.head = new_purchase
        else:
            current_purchase = self.head
            while current_purchase.next is not None:
                current_purchase = current_purchase.next
            current_purchase.next = new_purchase

    def print_history(self):
        current_purchase = self.head
        while current_purchase is not None:
            print("Timestamp: " + str(current_purchase.timestamp) + ", Amount: " + str(current_purchase.amount))
            current_purchase = current_purchase.next
            
            
    def cari_nominal(self, amount):
        current = self.head
        while current is not None:
            if current.amount == amount:
                return current
            current = current.next
        return None
    
    
    def is_empty(self):
        return self.head is None
    
    def dequeue(self):
            removed_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_node.amount

    def display(self):
        curr = self.head
        while curr:
            print(curr.amount, end=" ")
            curr = curr.next
        print()

    def menu(self):
        while True:
            print("="*100)
            print(" "*40, "menu awal")
            print("="*100)
            print("1.user")
            print("2.admin")
            print("3.keluar")
            choice = int(input("Enter choice: "))
            if choice == 1:
             while True:
                print("="*100)
                print(" "*40,"Menu pembeli:")
                print("="*100)
                print("1. beli pulsa")
                print("2. riwayat")
                print("3. keluar")
                pilih=input("masukan pilihan: ")
                if pilih=="1":
                 while True:
                  amount = int(input("masukan jumlah pulsa yang ingin dibeli: "))
                  if amount>0:
                   history.add_purchase(amount)
                  else:
                      print("pulsa harus lebih dari 0")
                  n=input("apakah anda ingin mengisi pulsa lagi:")
                  if n=="t":
                    break
                elif pilih == "2":
                  self.print_history()
                elif pilih == "3":
                  break
                else:
                  print("pilihan tidak tersedia.")
            
            elif choice == 2:
              while True:
                print("="*100)
                print(" "*40, "menu admin")
                print("="*100)
                print("1. hapus pembelian")
                print("2. riwayat pembelian user")
                print("3. cari pulsa berdasarkan jumlah")
                print("4. keluar")
                pilihan=input("masukan pilihan: ")
                if pilihan =="1":
                     print("riwayat awal: ")
                     history.display()
                     print("sesudah dihapus")
                     history.dequeue()
                     history.display()
                     
                elif pilihan =="2":
                     self.print_history()
                       
                elif pilihan == "3":
                         amount = int(input("Masukkan jumlah pulsa yang ingin dicari: "))
                         cari_jumlah = history.cari_nominal(amount)
                         if cari_jumlah is None:
                           print("Riwayat pembelian tidak ditemukan")
                         else:
                          print(f"Jumlah: {cari_jumlah.amount},pembelian tanggal: {cari_jumlah.timestamp}")
                elif pilihan == "4":
                     break
                else:
                    print("pilihan tidak ada")

            elif choice==3:
                break
            else:
                print("pilihan tidak tersedia")


history = PurchaseHistory()
history.menu()




   
    
