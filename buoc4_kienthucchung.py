import streamlit as st
import pandas as pd 
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt

import math
import re

#Tính modul
def modul(z):
  return ["mod{} = sqrt({}^2 + {}^2) = {}".format(z, z.real, z.imag, abs(z)), abs(z)]

#Tính số phức liên hợp
def soPhucLienHop(z):
  return ["conj{} = {}".format(z, z.conjugate()), z.conjugate()]

#Tính tổng 2 số phức
def sum2Complex(z1, z2):
  return ["{} + {} = ({} + {}) + ({} + {})*j = {}".format(z1, z2, z1.real, z2.real, z1.imag, z2.imag, z1 + z2), z1 + z2]

#Tính hiệu 2 số phức
def substract2Complex(z1, z2):
  return ["{} - {} = ({} - {}) + ({} - {})*j = {}".format(z1, z2, z1.real, z2.real, z1.imag, z2.imag, z1 - z2), z1 - z2]

#Tính tích 2 số phức
def multiply2Complex(z1, z2):
  return ["{} * {} = ({}*{} - {}*{}) + ({}*{} + {}*{})*j = {}"\
        .format(z1, z2, z1.real, z2.real, z1.imag, z2.imag, z1.real, z2.imag, z1.imag, z2.real, z1 * z2), z1 * z2]

#Tính thương của 2 số phức
def divide2Complex(z1, z2):
  return ["{}/{} = [({}*{} + {}*{})/({}^2 + {}^2)] + [({}*{} - {}*{})/({}^2 + {}^2)]*j = {}"\
          .format(z2, z1, z1.real, z2.real, z1.imag, z2.imag, z1.real, z1.imag, z1.real, z2.imag, z1.imag, z2.real,  z1.real, z1.imag, z2 / z1), z2 / z1]