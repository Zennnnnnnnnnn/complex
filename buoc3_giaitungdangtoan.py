import streamlit as st
import pandas as pd 
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt

import math
import re

from buoc4_kienthucchung import *

ket_luan = ["tìm số phức", "tìm điểm biểu diễn", "tìm mô đun", "tìm số phức liên hợp", "tìm tổng", "tìm hiệu", "tìm tích", "tìm thương"]
trinhBay = ["số phức z cần tìm là: ", "điểm biểu diễn của số phức z là: ", "mô đun của số phức z là: ", "số phức liên hợp của z là: ", "tổng các số phức là: ", "hiệu các số phức là: ", "tính các số phức là: ", "thương các số phức là: "]


###############################################################
#dạng 2.4.1. số phức thỏa mãn một đẳng thức
###############################################################
def TimSoPhucThoaPT(a_1, b_1, a_2, b_2, a_3, b_3, a_4, b_4, a_5, b_5):
  khaiTrien = '({} + {}*j)*z + ({}*{} + {}*{} + {})*j + ({}*{} - {}*{} + {}) \
  = ({} + {}*j)*z~ + ({}*{} + {}*{})*j + ({}*{} - {}*{})'\
  .format(a_2, b_2, a_2, b_1, b_2, a_1, b_3, a_2, a_1, b_2, b_1, a_3, a_4, b_4, a_4, b_5, b_4, a_5, a_4, a_5, b_4, b_5)

  khaiTrienTuongDuong1 = '({} + {}*j)*z - ({} + {}*j)*z~ \
  = ({}*{} + {}*{})*j - ({}*{} + {}*{} + {})*j + ({}*{} - {}*{}) - ({}*{} - {}*{} + {})'\
  .format(a_2, b_2, a_4, b_4, a_4, b_5, b_4, a_5, a_2, b_1, b_2, a_1, b_3, a_4, a_5, b_4, b_5, a_2, a_1, b_2, b_1, a_3)

  soAo1 = ((a_4*b_5 + b_4*a_5) - (a_2*b_1 + b_2*a_1 + b_3))
  soThuc1 = (a_4*a_5 - b_4*b_5) - (a_2*a_1 - b_2*b_1 + a_3)
  khaiTrienTuongDuong2 = '({} + {}*j)*z - ({} + {}*j)*z~ = {} + {}*j'\
  .format(a_2, b_2, a_4, b_4, soThuc1, soAo1)

  khaiTrienTuongDuong3 = '({} + {}*j)*(a + b*j) - ({} + {}*j)*(a - b*j) = {} + {}*j'\
  .format(a_2, b_2, a_4, b_4, soThuc1, soAo1)

  khaiTrienTuongDuong4 ='({}*a + {}*b*j + {}*a*j + {}*b*(-1)) - ({}*a - {}*b*j + {}*a*j - {}*b*(-1)) \
  = {} + {}*j'\
  .format(a_2, a_2, b_2, b_2, a_4, a_4, b_4, b_4, soThuc1, soAo1)

  khaiTrienTuongDuong5 ='({}*a - {}*b) + ({}*b + {}*a)*j - ({}*a + {}*b) + ({}*b - {}*a)*j \
  = {} + {}*j'\
  .format(a_2, b_2, a_2, b_2, a_4, b_4, a_4, b_4, soThuc1, soAo1)

  khaiTrienTuongDuong6 ='({}*a - {}*b - {}*a - {}*b) + ({}*b + {}*a + {}*b - {}*a)*j \
  = {} + {}*j'\
  .format(a_2, b_2, a_4, b_4, a_2, b_2, a_4, b_4, soThuc1, soAo1)

  khaiTrienTuongDuong7 ='(({} - {})*a - ({} + {})*b) + (({} - {})*a + ({} + {})*b)*j \
  = {} + {}*j'\
  .format(a_2, a_4, b_2, b_4, b_2, b_4, a_2, a_4, soThuc1, soAo1)

  pTu_soThuc01 = a_2-a_4
  pTu_soThuc02 = b_2+b_4
  pTu_soAo01 = b_2-b_4
  pTu_soAo02 = a_2+a_4
  khaiTrienTuongDuong8 ='({}*a - {}*b) + ({}*a + {}*b)*j \
  = {} + {}*j'\
  .format(pTu_soThuc01, pTu_soThuc02, pTu_soAo01, pTu_soAo02, soThuc1, soAo1)

  khaiTrienTuongDuong9 ='  {}*a - {}*b = {} \nvà {}*a + {}*b = {}'\
  .format(pTu_soThuc01, pTu_soThuc02, soThuc1,pTu_soAo01, pTu_soAo02, soAo1)

  khaiTrienTuongDuong10 ='a = ({} + {}*b)/{} \nvà {}*[({} + {}*b)/{}] + {}*b = {}'\
  .format(soThuc1, pTu_soThuc02, pTu_soThuc01, pTu_soAo01, soThuc1, pTu_soThuc02, pTu_soThuc01, pTu_soAo02, soAo1)

  pTu_a01 = soThuc1/pTu_soThuc01
  pTu_a02 = pTu_soThuc02/pTu_soThuc01
  pTu_b01 = pTu_soAo01*(soThuc1/pTu_soThuc01)
  pTu_b02 = pTu_soAo01*(pTu_soThuc02/pTu_soThuc01) + pTu_soAo02
  khaiTrienTuongDuong11 ='a = {} + {}*b \nvà {} + {}*b = {}'\
  .format(pTu_a01, pTu_a02, pTu_b01, pTu_b02, soAo1)

  pTu_b = (soAo1 - pTu_b01)/pTu_b02
  khaiTrienTuongDuong12 ='a = {} + {}*b \nvà b = {}'\
  .format(pTu_a01, pTu_a02, pTu_b)

  pTu_a = pTu_a01 + pTu_a02*pTu_b
  khaiTrienTuongDuong13 ='a = {} \nvà b = {}'.format(pTu_a, pTu_b)

  st.write("phương trình sau khi khai triển ra là: \n", khaiTrien)
  st.write("<=>", khaiTrienTuongDuong1)
  st.write("<=>", khaiTrienTuongDuong2)
  st.write("\nthay z = a + b*i và z~ = a - b*i vào phương trình trên, ta thu được: \n", khaiTrienTuongDuong3)
  st.write("<=>", khaiTrienTuongDuong4)
  st.write("<=>", khaiTrienTuongDuong5)
  st.write("<=>", khaiTrienTuongDuong6)
  st.write("<=>", khaiTrienTuongDuong7)
  st.write("<=>", khaiTrienTuongDuong8)
  st.write("\ntiến hành giải hệ phương trình sau: \n", khaiTrienTuongDuong9)
  st.write("<=>", khaiTrienTuongDuong10)
  st.write("<=>", khaiTrienTuongDuong11)
  st.write("<=>", khaiTrienTuongDuong12)
  st.write("<=>", khaiTrienTuongDuong13)
  st.write("\nvậy số phức z là: z = {} + {}*j".format(pTu_a, pTu_b))

  z = complex(pTu_a, pTu_b)
  return z

###############################################################
#dạng 2.4.2. giải phương trình bậc 2 số phức
###############################################################
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            st.write("Vì a=0 và b=0 nên phương trình vô nghiệm!");
        else:
            st.write("Vì a=0 và b != 0 nên phương trình có một nghiệm: z = ", + (-c / b));
        return;
 
    # tính delta
    st.write("Bước 1: ")
    delta = b * b - 4 * a * c;
    st.write("Delta = b^2 - 4ac = ", delta)
    # tính nghiệm
    st.write("Bước 2: ")
    if (delta > 0):
        z1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        z2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        st.write("Vì delta > 0 nên phương trình có 2 nghiệm là: z1 = ", z1, " và z2 = ", z2);
    elif (delta == 0):
        z1 = (-b / (2 * a));
        st.write("Vì delta = 0 nên phương trình có nghiệm kép: z1 = z2 = ", z1);
    else:
        z1 = complex(round(-b/(2 * a), 2), round(math.sqrt(abs(delta))/(2 * a),2));
        z2 = complex(round(-b/(2 * a),2), round(- math.sqrt(abs(delta))/(2 * a),2));
        st.write("Vì delta < 0 nên phương trình có 2 nghiệm phức là: z1 = ", z1, " và z2 = ", z2);
    return z1, z2

#Xuất thông tin nghiệm z1, z2 trường hợp số phức:
def outputZ1Z2(z1, z2, input_list):
  ket_luan = ["tìm số phức", "tìm điểm biểu diễn", "tìm mô đun", "tìm số phức liên hợp", "tìm tổng", "tìm hiệu", "tìm tích", "tìm thương"]
  
  if input_list[1] == ket_luan[1]:
    st.write("điểm biểu diễn của nghiệm z1 là: ", "M({}, {})".format(z1.real, z1.imag))
    st.write("điểm biểu diễn của nghiệm z2 là: ", "M({}, {})".format(z2.real, z2.imag))
  if input_list[1] == ket_luan[2]:
    st.write("Modul của nghiệm z1 là: ", modul(z1)[0])
    st.write("Modul của nghiệm z2 là: ", modul(z2)[0])
  if input_list[1] == ket_luan[3]:
    st.write("Số phức liên hợp của nghiệm z1 là: ", soPhucLienHop(z1)[0])
    st.write("Số phức liên hợp của nghiệm z2 là: ", soPhucLienHop(z2)[0])
  if input_list[1] == ket_luan[4]:
    st.write("Tổng của 2 nghiệm là: ", sum2Complex(z1,z2)[0])
  if input_list[1] == ket_luan[5]:
    st.write("Hiệu của 2 nghiệm là: ", substract2Complex(z1, z2)[0])
  if input_list[1] == ket_luan[6]:
    st.write("Tích của 2 nghiệm là: ", multiply2Complex(z1, z2)[0])
  if input_list[1] == ket_luan[7]:
    st.write("Thương của 2 nghiệm là: ", divide2Complex(z1,z2)[0])

###############################################################
# dạng 2.4.3.a Tính toán số phức
###############################################################
def tinhtoancoban(z, input_list):
  hamTraVe = [z, "M({}, {})".format(z.real, z.imag), modul(z), soPhucLienHop(z)]

  for i in range(len(ket_luan)):
    if ket_luan[i] == input_list[1]:
      if i in [0, 1]:
        st.write(trinhBay[i], hamTraVe[i])
      else: # i in [2,3]
        st.write(hamTraVe[i][0])
        st.write(trinhBay[i], hamTraVe[i][1])

###############################################################
#dạng 2.4.3.b Tính tổng_hiệu_tích_thương
###############################################################
def tong_hieu(z1, z2, input_list):
  hamTraVe = [sum2Complex(z1,z2), substract2Complex(z1, z2)] 

  for i in range(len(ket_luan)):
    if ket_luan[i] == input_list[1]:
      return hamTraVe[i - 4]

def tich_thuong(z1, z2, input_list):
  hamTraVe = [multiply2Complex(z1, z2), divide2Complex(z1,z2)]

  for i in range(len(ket_luan)):
    if ket_luan[i] == input_list[1]:
      return hamTraVe[i - 6]