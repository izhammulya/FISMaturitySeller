#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

input_jumlah_transaksi_B2B_TOP = int(input("TRXb2b: "))
input_jumlah_transaksi_Retail_Direct = int(input("TRXdir: "))
input_jumlah_listing_produk = int(input("produk: "))
input_gmv = int(input("GMV: "))
    
# # input_jumlah_transaksi_B2B_TOP = int(a)
# print('jumlah_transaksi_B2B_TOP ',a)
# input_jumlah_transaksi_Retail_Direct = int(b)
# print('jumlah_transaksi_Retail_Direct ',b)
# #     if c >= 1500:
# #         c = 1499
# #         input_jumlah_listing_produk = c
# #     else:
# #         input_jumlah_listing_produk = int(c)
# input_jumlah_listing_produk = int(c)
# print('jumlah_listing_produk ',c)
# input_gmv = int(d)/1000000
# print('gmv ',d)

x_b2b = np.arange(0, 500, 1)
x_dir = np.arange(0, 500, 1)
#     x_prod = np.arange(0, 1500, 1)
x_prod = np.arange(0, 200000, 1)
# x_gmv= np.arange(0, 1000000000, 100000)
x_gmv = np.arange(0,20000,1)
y_out = np.arange(0, 100, 1)

print("Simulasi Seller Dewasa\n\n")


b2b_sedikit = mf.trapmf(x_b2b, [0, 0, 5, 10])
b2b_sedang = mf.trapmf(x_b2b, [5, 10, 25, 100]) 
b2b_banyak = mf.trapmf(x_b2b, [25, 100, 500, 500])

dir_low = mf.trapmf(x_b2b, [0, 0, 5, 10])
dir_mid = mf.trapmf(x_b2b, [5, 10, 25, 100]) 
dir_high = mf.trapmf(x_b2b, [25, 100, 500, 500])

prod_dikit= mf.trapmf(x_prod, [0, 0, 100, 200])
prod_sdg= mf.trimf(x_prod, [100, 200, 500])
#     prod_banyk= mf.trapmf(x_prod, [250, 500,1500, 1500])
prod_banyk= mf.trapmf(x_prod, [250, 500, 200000, 200000])

gmv_dikit = mf.trapmf(x_gmv,[0,0,6,10])
gmv_sedeng = mf.trimf(x_gmv,[6,10,40])
gmv_akeh = mf.trapmf(x_gmv,[35,40,20000,20000])

    # gmv_dikit = mf.trapmf(x_gmv,[0,0,100000000,250000000])
    # gmv_sedeng = mf.trimf(x_gmv,[100000000,250000000,400000000])
    # gmv_akeh = mf.trapmf(x_gmv,[250000000,400000000,500000000,1000000000000])

less_priority = mf.trapmf(y_out, [0 ,0 ,50 ,70])
consideration = mf.trimf(y_out, [50 ,70 ,80])
priority = mf.trapmf(y_out, [70 ,80, 100 ,100])

plt.tight_layout()

    # Derajat Keanggotaan

b2b_trx_sedikit = fuzz.interp_membership(x_b2b, b2b_sedikit, input_jumlah_transaksi_B2B_TOP)
b2b_trx_sedang = fuzz.interp_membership(x_b2b, b2b_sedang, input_jumlah_transaksi_B2B_TOP)
b2b_trx_banyak = fuzz.interp_membership(x_b2b, b2b_banyak, input_jumlah_transaksi_B2B_TOP)

dir_trx_low = fuzz.interp_membership(x_dir, dir_low, input_jumlah_transaksi_Retail_Direct)
dir_trx_mid = fuzz.interp_membership(x_dir, dir_mid, input_jumlah_transaksi_Retail_Direct)
dir_trx_high = fuzz.interp_membership(x_dir, dir_high, input_jumlah_transaksi_Retail_Direct)

prod_num_dikit = fuzz.interp_membership(x_prod, prod_dikit, input_jumlah_listing_produk)
prod_num_sdg = fuzz.interp_membership(x_prod, prod_sdg, input_jumlah_listing_produk)
prod_num_banyk = fuzz.interp_membership(x_prod, prod_banyk, input_jumlah_listing_produk)

gmv_dikit = fuzz.interp_membership(x_gmv, gmv_dikit, input_gmv)
gmv_sedeng = fuzz.interp_membership(x_gmv, gmv_sedeng, input_gmv)
gmv_akeh = fuzz.interp_membership(x_gmv, gmv_akeh, input_gmv)
    
rule1 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_dikit), gmv_dikit), less_priority)
rule2 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_dikit), gmv_sedeng), consideration)
rule3 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_dikit), gmv_akeh), consideration)

rule4 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_sdg), gmv_dikit), less_priority)
rule5 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_sdg), gmv_sedeng), consideration)
rule6 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_sdg), gmv_akeh), consideration)

rule7 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_banyk), gmv_dikit), less_priority)
rule8 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_banyk), gmv_sedeng), consideration)
rule9 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_low),prod_num_banyk), gmv_akeh), consideration)

rule10 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_dikit), gmv_dikit), less_priority)
rule11 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_dikit), gmv_sedeng), consideration)
rule12 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_dikit), gmv_akeh), consideration)

rule13 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_sdg), gmv_dikit), less_priority)
rule14 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_sdg), gmv_sedeng), consideration)
rule15 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_sdg), gmv_akeh), priority) #eval

rule16 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_banyk), gmv_dikit), less_priority)
rule17 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_banyk), gmv_sedeng), consideration) 
rule18 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_mid),prod_num_banyk), gmv_akeh), priority) #eval

rule19 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_dikit), gmv_dikit), less_priority)
rule20 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_dikit), gmv_sedeng), consideration) 
rule21 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_dikit), gmv_akeh), priority) #eval

rule22 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_dikit), less_priority)
rule23 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_sedeng),consideration) 
rule24 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_akeh), priority) 

rule25 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_dikit), less_priority)
rule26 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_sedeng),consideration) 
rule27 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedikit, dir_trx_high),prod_num_sdg), gmv_akeh), priority) 

rule28 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_dikit), gmv_dikit), less_priority)
rule29 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_dikit), gmv_sedeng),consideration) 
rule30 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_dikit), gmv_akeh), consideration) #eval

rule31 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_sdg), gmv_dikit), less_priority)
rule32 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_sdg), gmv_sedeng),consideration) #eval
rule33 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_sdg), gmv_akeh), priority) #eval

rule34 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_banyk), gmv_dikit), less_priority)
rule35 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_banyk), gmv_sedeng),consideration) #eval
rule36 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_low),prod_num_banyk), gmv_akeh), priority)

rule37 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_dikit), gmv_dikit), less_priority)#eval
rule38 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_dikit), gmv_sedeng),consideration) 
rule39 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_dikit), gmv_akeh), priority)

rule40 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_sdg), gmv_dikit), consideration)#eval
rule41 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_sdg), gmv_sedeng),consideration) 
rule42 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_sdg), gmv_akeh), priority)

rule43 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_banyk), gmv_dikit), consideration)
rule44 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_banyk), gmv_sedeng),priority) #eval
rule45 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_mid),prod_num_banyk), gmv_akeh), priority)

rule46 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_dikit), gmv_dikit), consideration) #eval
rule47 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_dikit), gmv_sedeng),priority) 
rule48 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_dikit), gmv_akeh), priority)

rule49 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_sdg), gmv_dikit), priority) #eval
rule50 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_sdg), gmv_sedeng),priority) 
rule51 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_sdg), gmv_akeh), priority)

rule52 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_banyk), gmv_dikit), priority) #eval
rule53 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_banyk), gmv_sedeng),priority) 
rule54 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_sedang, dir_trx_high),prod_num_banyk), gmv_akeh), priority)

rule55 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_dikit), gmv_dikit), less_priority) 
rule56 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_dikit), gmv_sedeng),consideration) #eval
rule57 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_dikit), gmv_akeh), consideration) #eval

rule58 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_sdg), gmv_dikit), less_priority) 
rule59 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_sdg), gmv_sedeng),consideration) #eval
rule60 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_sdg), gmv_akeh), priority) #eval

rule61 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_banyk), gmv_dikit), consideration) #eval 
rule62 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_banyk), gmv_sedeng),priority) #eval
rule63 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_low),prod_num_banyk), gmv_akeh), priority) #eval

rule64 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_dikit), gmv_dikit), less_priority) 
rule65 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_dikit), gmv_sedeng),priority) #eval
rule66 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_dikit), gmv_akeh), priority) #eval

rule67 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_sdg), gmv_dikit), consideration) 
rule68 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_sdg), gmv_sedeng),priority) #eval
rule69 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_sdg), gmv_akeh), priority) #eval

rule70 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_banyk), gmv_dikit), consideration) 
rule71 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_banyk), gmv_sedeng),priority) #eval
rule72 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_mid),prod_num_banyk), gmv_akeh), priority) 

rule73 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_dikit), gmv_dikit), consideration) 
rule74 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_dikit), gmv_sedeng),priority) #eval
rule75 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_dikit), gmv_akeh), priority) 

rule76 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_sdg), gmv_dikit), priority) 
rule77 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_sdg), gmv_sedeng),priority)
rule78 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_sdg), gmv_akeh), priority) 

rule79 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_banyk), gmv_dikit), priority) 
rule80 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_banyk), gmv_sedeng),priority) #eval
rule81 = np.fmin(np.fmin(np.fmin(np.fmin(b2b_trx_banyak, dir_trx_high),prod_num_banyk), gmv_akeh), priority) 

out_low = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1,rule4),rule7),rule10),rule13),rule16),rule19),rule22),rule25),rule28),rule31),rule34),rule37),rule55),rule58),rule64)
out_mid = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule14, rule15),rule17),rule2),rule5),rule8),rule11),rule29),rule20),rule3),rule6),rule9),rule12),rule21),rule23),rule26),rule30),rule32),rule35),rule38),rule40),rule41),rule43),rule46),rule56),rule57),rule59),rule61),rule67),rule70),rule73)
out_high = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule36, rule33),rule27),rule24),rule18),rule39),rule42),rule44),rule45),rule47),rule48),rule49),rule50),rule51),rule52),rule53),rule54),rule60),rule62),rule63),rule65),rule66),rule68),rule69),rule71),rule72),rule74),rule75),rule76),rule77),rule78),rule79),rule80),rule81)
put0 = np.zeros_like(y_out)

out_risk = np.fmax(np.fmax(out_mid, out_high),out_low)
defuzzified  = fuzz.defuzz(y_out, out_risk, 'centroid')
result = fuzz.interp_membership(y_out, out_risk, defuzzified)
result = fuzz.interp_membership(y_out, out_risk, defuzzified)
print("skor:", defuzzified)
if defuzzified >= 80:
    print("Hasil klarifikasi:", 'seller dewasa')
elif defuzzified < 80 and defuzzified > 60:
    print("Hasil klarifikasi:", 'consideration')
else:
    print("Hasil klarifikasi:", 'seller PMS (nggak dewasa)')
ig, ax0 = plt.subplots(figsize=(7, 4))

ax0.plot(y_out, less_priority, 'r', linewidth = 1, linestyle = '--')
ax0.plot(y_out, consideration, 'g', linewidth = 1, linestyle = '--')
ax0.plot(y_out, priority, 'b', linewidth = 1, linestyle = '--')

ax0.fill_between(y_out, put0, out_risk, facecolor = 'Orange', alpha = 0.7)
ax0.plot([defuzzified , defuzzified], [0, result], 'k', linewidth = 1.5, alpha = 0.9)
ax0.set_title('Simulasi hasil rule DSS Seller')

plt.tight_layout()


# In[ ]:




