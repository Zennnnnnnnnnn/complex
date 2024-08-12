import streamlit as st
import pandas as pd
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt
import math
import re

from buoc1_phanloaidangtoan import *
from buoc2_phantich import *

###############################################################
# Hướng dẫn
###############################################################
# Tiêu đề
st.title("Ứng dụng Tính Toán Số Phức")

# Hướng dẫn
st.header("Hướng Dẫn Sử Dụng")

# Ví dụ
st.subheader("**Ví dụ:**")

# Nội dung hướng dẫn
st.markdown("""
**Nhập đề bài:**

1. **Tìm mô đun của số phức**  
   `cho số phức z = 1 + 2j tìm mô đun của z`

2. **Tìm hiệu của các số phức**  
   `cho các số phức z = 1 + j, t = 3 + 5j tìm hiệu của các số phức`

3. **Tìm tích của các số phức**  
   `cho các số phức z = 5 + 4j, t = 3 + 2j và k = 2 + j tìm tích của các số phức`

4. **Tìm điểm biểu diễn của số phức thỏa mãn đẳng thức**  
   `tìm điểm biểu diễn của số phức z thỏa mãn đẳng thức ( z + 1 + 2*j ) ( 3 + 4*j ) + ( 5 + 6*j ) = ( 7 + 8*j ) ( z~ + 9 + 10*j )`

5. **Tìm số phức thỏa mãn đẳng thức**  
   `tìm số phức z thỏa mãn đẳng thức ( z + sqrt(2)*j ) ( 1 + 3*j ) + ( ) = ( sqrt(3) ) ( z~ + float(5/3)*j )`

6. **Tìm mô đun của số phức thỏa mãn đẳng thức**  
   `tìm mô đun của số phức z thỏa mãn đẳng thức ( z + 5*j ) ( 2021 + 2022*j ) + ( 0.5 + 0.75*j ) = ( 0.1 + 0.2*j ) ( z~ + j )`

7. **Tìm nghiệm của phương trình bậc hai số phức**  
   `tìm số phức z1, z2 là nghiệm của phương trình bậc hai số phức với hệ số thực như sau: 5*z^2 + 4*z + 9 = 0`

8. **Tìm nghiệm của phương trình bậc hai số phức khác**  
   `tìm số phức z1, z2 là nghiệm của phương trình bậc hai số phức với hệ số thực như sau: sqrt(2)*z^2 + 4*z + float(5/3) = 0`

9. **Tìm điểm biểu diễn của hai số phức trong mặt phẳng Oxy**  
   `Trong mặt phẳng Oxy, tìm điểm biểu diễn của hai số phức z1, z2 biết rằng z1, z2 là nghiệm của phương trình bậc hai số phức với hệ số thực như sau: sqrt(2)*z^2 + sqrt(3)*z + sqrt(2) = 0`

---
""")

st.subheader("Đến lượt bạn: ")
###############################################################
# Main
###############################################################

ket_luan = ["tìm số phức", "tìm điểm biểu diễn", "tìm mô đun", "tìm số phức liên hợp", "tìm tổng", "tìm hiệu", "tìm tích", "tìm thương"]
trinhBay = ["số phức z cần tìm là: ", "điểm biểu diễn của số phức z là: ", "mô đun của số phức z là: ", "số phức liên hợp của z là: ", "tổng các số phức là: ", "hiệu các số phức là: ", "tính các số phức là: ", "thương các số phức là: "]

de_bai = st.text_input("Nhập đề bài: ")
st.write(de_bai)

input_list = phanloaidangtoan(ket_luan, trinhBay, de_bai)
#st.write(input_list)

# Kiểm tra danh sách input_list
st.write("Danh sách input_list:", input_list)
st.write("Chiều dài của danh sách:", len(input_list))

# Xử lý trường hợp danh sách không đủ dài
if len(input_list) > 2:
    s = input_list[2]
else:
    st.write("Danh sách không đủ phần tử để truy cập chỉ mục 2")
    s = None

# Kiểm tra và gọi hàm tương ứng
if len(input_list) > 0:
    if input_list[0] == 'tính toán số phức cơ bản':
        if s is not None:
            phantich1(s, input_list)
    elif input_list[0] == 'tính tổng_hiệu_tích_thương':
        if s is not None:
            phantich2(s, input_list)
    elif input_list[0] == 'tìm số phức thỏa mãn một đẳng thức phức tạp':
        if s is not None:
            phantich3(s, input_list)
    elif input_list[0] == 'giải phương trình bậc 2 số phưc':
        if s is not None:
            phantich4(s, input_list)
    else:
        st.write("Loại bài toán không được nhận diện.")
else:
    st.write("Danh sách input_list không chứa dữ liệu.")
