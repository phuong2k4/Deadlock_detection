from detect_deadlock import detect_deadlocks

def nhap_so_nguyen(cau_hoi, nho_nhat):
   while True:
      try:
         so = int(input(cau_hoi))
      except ValueError:
         print("Lỗi: bạn phải nhập một số nguyên.")
         continue

      if so < nho_nhat:
         print("Lỗi: số phải lớn hơn hoặc bằng", nho_nhat)
         continue

      return so


def nhap_mot_dong(cau_hoi, so_phan_tu):
   while True:
      text = input(cau_hoi)
      cac_phan_tu = text.split()

      if len(cac_phan_tu) != so_phan_tu:
         print("Lỗi: cần đúng", so_phan_tu, "số, bạn nhập", len(cac_phan_tu), "số.")
         continue

      dong = []
      hop_le = True

      for chu in cac_phan_tu:
         try:
               so = int(chu)
         except ValueError:
               print("Lỗi:", chu, "không phải số nguyên.")
               hop_le = False
               break

         if so < 0:
               print("Lỗi: không được nhập số âm (", so, ")")
               hop_le = False
               break

         dong.append(so)

      if hop_le:
         return dong

def nhap_ma_tran(ten, so_hang, so_cot):
   print()
   print("Nhập ma trận", ten, "(", so_hang, "hàng x", so_cot, "cột )")
   ma_tran = []
   for i in range(so_hang):
      dong = nhap_mot_dong("  " + ten + " của P" + str(i) + ": ", so_cot)
      ma_tran.append(dong)
   return ma_tran

def in_ma_tran(ten, ma_tran):
   print()
   print(ten + ":")
   for i in range(len(ma_tran)):
      print("  P" + str(i), ma_tran[i])


def kiem_tra_canh_bao(n, m, allocation, request, available):
   tong = []
   for j in range(m):
      cong = available[j]
      for i in range(n):
         cong = cong + allocation[i][j]
      tong.append(cong)

   print()
   print("Tổng tài nguyên của hệ thống (Total):", tong)

   co_canh_bao = False
   for i in range(n):
      for j in range(m):
         if request[i][j] > tong[j]:
               print("Cảnh báo: P" + str(i), "xin", request[i][j], "đơn vị R" + str(j),
                     "nhưng cả hệ thống chỉ có", tong[j])
               co_canh_bao = True

   if not co_canh_bao:
      print("Không có cảnh báo nào.")

def main():
   print("=== NHẬP DỮ LIỆU PHÁT HIỆN DEADLOCK ===")

   n = nhap_so_nguyen("Nhập số tiến trình (n): ", 1)
   m = nhap_so_nguyen("Nhập số loại tài nguyên (m): ", 1)

   allocation = nhap_ma_tran("Allocation", n, m)
   request = nhap_ma_tran("Request", n, m)

   print()
   print("Nhập vector Available (", m, "số )")
   available = nhap_mot_dong("  Available: ", m)

   print()
   print("=== DỮ LIỆU ĐÃ NHẬP ===")
   print("n =", n, ", m =", m)
   in_ma_tran("Allocation", allocation)
   in_ma_tran("Request", request)
   print()
   print("Available:", available)

   kiem_tra_canh_bao(n, m, allocation, request, available)
   
   deadlock_processes, safe_sequences = detect_deadlocks(n ,available, allocation, request)
   print(f"Deadlock_processes = {deadlock_processes}")
   print(f"Safe sequence = {safe_sequences}")
   print()
   print("=> Dữ liệu hợp lệ.")




main()
