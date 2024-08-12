import streamlit as st
import pandas as pd 
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt

import math
import re

def phanloaidangtoan(ket_luan, trinhBay, de_bai):
  dang_toan = {'tính toán số phức cơ bản': ['cho số phức'], 
               'tính tổng_hiệu_tích_thương': ['cho các số phức'],
               'giải phương trình bậc 2 số phưc': ['nghiệm của phương trình bậc hai số phức'],
               'tìm số phức thỏa mãn một đẳng thức phức tạp': ['số phức z thỏa mãn đẳng thức']
  }

  de_bai2 =[]

  for i in dang_toan:
    for j in dang_toan[i]:
      if re.search(j, de_bai):
        de_bai2.append(i) # đưa dạng bài toán vào list
  if not de_bai2:
    print("bài toán không giải được")
  else:
    for k in ket_luan:
      if re.search(k, de_bai):
        de_bai2.append(k) # đưa kết luận vào list
    if de_bai2[0] == 'tính toán số phức cơ bản':
      de_bai2.append(de_bai[(de_bai.find('=') - 2):(de_bai.find('j') + 1)]) # đưa giả thuyết vào list
    if de_bai2[0] == 'tính tổng_hiệu_tích_thương':
      de_bai2.append(de_bai[(de_bai.find('=') - 2):(de_bai.rfind('j') + 1)])
    if de_bai2[0] == 'giải phương trình bậc 2 số phưc':
      de_bai2.append(de_bai[(de_bai.find('nghiệm của phương trình bậc hai số phức với hệ số thực như sau: ') + 64):(de_bai.find('= 0') + 3)])
    if de_bai2[0] == 'tìm số phức thỏa mãn một đẳng thức phức tạp':
      de_bai2.append(de_bai[de_bai.find('('):(de_bai.rfind(')') + 1)])

  return de_bai2