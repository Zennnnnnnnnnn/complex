import streamlit as st
import pandas as pd 
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt

import math
import re

from buoc3_giaitungdangtoan import *

###############################################################
# hàm chuyển phân sô về float 
###############################################################
def convert_to_float(frac_str):
  try:
    return float(frac_str)
  except ValueError:
    num, denom = frac_str.split('/')
    try:
      leading, num = num.split(' ')
      whole = float(leading)
    except ValueError:
      whole = 0
    frac = float(num) / float(denom)
    return whole - frac if whole < 0 else whole + frac

###############################################################
# phantich1
###############################################################

def phantich1(s, input_list):
  z_split = s.split(" ")
  if z_split[4] == "j":
    z_split[4] = "1j"
  z = complex(int(z_split[2]), int(z_split[4].rstrip("j")))
  tinhtoancoban(z, input_list)

###############################################################
# phantich2
###############################################################
def phantich2(s, input_list):
  c1 = '='
  c2 = 'j'
  index1 = [pos for pos, char in enumerate(s) if char == c1]
  index2 = [pos for pos, char in enumerate(s) if char == c2]
  list_sophuc = []
  for i in range(len(index1)):
    z_string = s[(index1[i]- 2):(index2[i] + 1)]
    z_split = z_string.split(" ")
    if z_split[4] == "j":
      z_split[4] = "1j"
    z = complex(int(z_split[2]), int(z_split[4].rstrip("j")))
    list_sophuc.append(z)

  if input_list[1] in ["tìm tổng", "tìm hiệu"]:
    ketqua = 0 + 0j
    for j in list_sophuc:
      k = tong_hieu(j, ketqua, input_list)
      if list_sophuc.index(j) > 0:
        st.write(k[0])
      ketqua = k[1]
  else: # input_list[1] == "tìm tích"
    ketqua = 1 + 0j
    for j in list_sophuc:
      k = tich_thuong(ketqua, j, input_list)
      if list_sophuc.index(j) > 0:
        st.write(k[0])
      ketqua = k[1]

  for i in range(len(ket_luan)):
    if ket_luan[i] == input_list[1]:
      st.write(trinhBay[i], ketqua)

###############################################################
# phantich3
###############################################################
def layheso(s):
  z_split = s.split(" ")
  vitri_mongoac = []
  vitri_dongngoac = []
  for i in range(len(z_split)):
    if z_split[i] == "(":
      vitri_mongoac.append(i + 1)
    if z_split[i] == ")":
      vitri_dongngoac.append(i)

  list_bieuthuc = []
  for i in range(len(vitri_mongoac)):
    batdau = vitri_mongoac[i]
    ketthuc = vitri_dongngoac[i]
    list_bieuthuc.append(z_split[batdau:ketthuc])
  
  for i in range(len(list_bieuthuc)):
    if i == 0 or i == 4:
      del list_bieuthuc[i][ 0 : 2]

  del_list_bieuthuc = []
  for i in range(len(list_bieuthuc)):
    for j in range(len(list_bieuthuc[i])):
      if list_bieuthuc[i][j] == '+':
        del_list_bieuthuc.append([i, j])

  for i in range(len(del_list_bieuthuc)):
    k, h = del_list_bieuthuc[i]
    del list_bieuthuc[k][h]

  list_a = []
  list_b = []
  for i in range(len(list_bieuthuc)):
    if len(list_bieuthuc[i]) == 2:
      if re.search("j", list_bieuthuc[i][0]):
        list_b.append(list_bieuthuc[i][0])
        list_a.append(list_bieuthuc[i][1])
      else: 
        list_a.append(list_bieuthuc[i][0])
        list_b.append(list_bieuthuc[i][1])

    if len(list_bieuthuc[i]) == 1:
      if re.search("j", list_bieuthuc[i][0]):
        list_a.append('0')
        list_b.append(list_bieuthuc[i][0])
      else: 
        list_a.append(list_bieuthuc[i][0])
        list_b.append('0*j')

    if len(list_bieuthuc[i]) == 0:
      list_a.append('0')
      list_b.append('0*j')

  for i in range(len(list_b)):
    if list_b[i] == "j":
      list_b[i] = "1*j"
      
  return list_a, list_b

def xulyheso(list_a, list_b):
  for i in range(len(list_a)):
    if re.search("float", list_a[i]):
      list_a[i] = convert_to_float(list_a[i].lstrip("float(").rstrip(")"))
    else:
      if re.search("sqrt", list_a[i]):
        list_a[i] = math.sqrt(float(list_a[i].lstrip("sqrt(").rstrip(")")))
      else:
        list_a[i] = float(list_a[i])

  a_1, a_2, a_3, a_4, a_5 = list_a[0], list_a[1], list_a[2], list_a[3], list_a[4]

  for i in range(len(list_b)):
    if re.search("float", list_b[i]):
      list_b[i] = convert_to_float(list_b[i].lstrip("float(").rstrip(")*j"))
    else:
      if re.search("sqrt", list_b[i]):
        list_b[i] = math.sqrt(float(list_b[i].lstrip("sqrt(").rstrip(")*j")))
      else:
        list_b[i] = float(list_b[i].rstrip("*j"))

  b_1, b_2, b_3, b_4, b_5 = list_b[0], list_b[1], list_b[2], list_b[3], list_b[4]
  
  return a_1, b_1, a_2, b_2, a_3, b_3, a_4, b_4, a_5, b_5

def phantich3(s, input_list):
  list_a, list_b = layheso(s)
  a_1, b_1, a_2, b_2, a_3, b_3, a_4, b_4, a_5, b_5 = xulyheso(list_a, list_b)
  z = TimSoPhucThoaPT(a_1, b_1, a_2, b_2, a_3, b_3, a_4, b_4, a_5, b_5)
  tinhtoancoban(z, input_list)

###############################################################
# phantich4
###############################################################
def phantich4(s, input_list):
  z_split = input_list[2].split(" ")
  heso = [z_split[0].rstrip("*z^2"), z_split[2].rstrip("*z"), z_split[4]]
  for i in range(len(heso)):
    if re.search("float", heso[i]):
      heso[i] = convert_to_float(heso[i].lstrip("float(").rstrip(")"))
    else:
      if re.search("sqrt", heso[i]):
        heso[i] = math.sqrt(float(heso[i].lstrip("sqrt(").rstrip(")")))
      else:
        heso[i] = float(heso[i])
  a, b, c = heso[0], heso[1], heso[2]
  
  z1, z2 = giaiPTBac2(a, b, c)
  outputZ1Z2(z1, z2, input_list)


