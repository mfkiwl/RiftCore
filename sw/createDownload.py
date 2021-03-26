# -*- coding: utf-8 -*-
# @Author: Ruige Lee
# @Date:   2021-01-20 14:27:44
# @Last Modified by:   Ruige Lee
# @Last Modified time: 2021-01-22 14:14:11


import sys
import os

downloadScript = ""

program = ""

size = os.path.getsize("./riftChip.bin")
with open("./riftChip.bin","rb") as f:
	for i in range(size//8 + 1):
		data1 = f.read(1)
		data2 = f.read(1)
		data3 = f.read(1)
		data4 = f.read(1)
		data5 = f.read(1)
		data6 = f.read(1)
		data7 = f.read(1)
		data8 = f.read(1)
		# print (data, data.hex())

		data = "0x" + data8.hex() + data7.hex() + data6.hex() + data5.hex() +data4.hex() + data3.hex() + data2.hex() + data1.hex()

		# program = program + " 0x" + str(data)
		# print(program)

		downloadScript = downloadScript + "create_hw_axi_txn download_sram" + str(i) + " [get_hw_axis hw_axi_1] -address " + str(hex(2147483648 + 8*i)) +" -data " + data + " -type write -force\n"
		downloadScript = downloadScript + "run_hw_axi download_sram" + str(i) + "\n"
# print(program)



# downloadScript = "create_hw_axi_txn download_sram [get_hw_axis hw_axi_1] -address 0x80000000 -data {" + program + "} -len " + str(size//8 + 1) + " -size 64 -type write -force\n"
# create_hw_axi_txn download_sram


# downloadScript = downloadScript + "run_hw_axi download_sram"

with open("./download.tcl","w") as f:
	f.write(downloadScript)




# run_hw_axi [create_hw_axi_txn readout [get_hw_axis hw_axi_1] -address 0x80000000 -type read -force]









