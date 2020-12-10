# RiftCore

![License](https://img.shields.io/github/license/whutddk/RiftCore)



--------------------------------------------

Currently, RiftCore is an 8-stage, multi-issue, out of order 64-bits RISC-V Core, which temporarily supports RV64IC.

![architecture](./doc/riftCore%20micro-architecture.png)



### [Wiki Here](https://github.com/whutddk/RiftCore/wiki)


------------------------------------

## status

|Last Commit|![GitHub last commit](https://img.shields.io/github/last-commit/whutddk/RiftCore)|Status|![GitHub Workflow Status](https://img.shields.io/github/workflow/status/whutddk/RiftCore/CI)|Support ISA|![ISA](https://img.shields.io/badge/ISA-RV64IC-yellowgreen)|
| --- | --- | --- | --- | --- | --- |
|![ISA](https://img.shields.io/badge/ISA-RV64I-yellowgreen)|
|![rv64ui-p-add](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-add.json)|![rv64ui-p-addiw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-addiw.json)|![rv64ui-p-addw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-addw.json)|![rv64ui-p-and](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-and.json)|![rv64ui-p-andi](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-andi.json)|![rv64ui-p-auipc](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-auipc.json)|
|![rv64ui-p-beq](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-beq.json)|![rv64ui-p-bge](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-bge.json)|![rv64ui-p-bgeu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-bgeu.json)|![rv64ui-p-blt](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-blt.json)|![rv64ui-p-bltu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-bltu.json)|![rv64ui-p-bne](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-bne.json)|
|![rv64ui-p-jal](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-jal.json)|![rv64ui-p-jalr](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-jalr.json)|![rv64ui-p-lb](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lb.json)|![rv64ui-p-lbu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lbu.json)|![rv64ui-p-ld](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-ld.json)|![rv64ui-p-lh](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lh.json)|
|![rv64ui-p-lhu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lhu.json)|![rv64ui-p-lui](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lui.json)|![rv64ui-p-lw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lw.json)|![rv64ui-p-lwu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-lwu.json)|![rv64ui-p-or](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-or.json)|![rv64ui-p-ori](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-ori.json)|
|![rv64ui-p-sb](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sb.json)|![rv64ui-p-sd](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sd.json)|![rv64ui-p-sh](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sh.json)|![rv64ui-p-sll](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sll.json)|![rv64ui-p-slli](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-slli.json)|![rv64ui-p-slliw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-slliw.json)|
|![rv64ui-p-sllw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sllw.json)|![rv64ui-p-slt](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-slt.json)|![rv64ui-p-slti](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-slti.json)|![rv64ui-p-sltiu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sltiu.json)|![rv64ui-p-sltu](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sltu.json)|![rv64ui-p-sra](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sra.json)|
|![rv64ui-p-srai](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-srai.json)|![rv64ui-p-sraiw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sraiw.json)|![rv64ui-p-sraw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sraw.json)|![rv64ui-p-srl](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-srl.json)|![rv64ui-p-srli](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-srli.json)|![rv64ui-p-srliw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-srliw.json)|
|![rv64ui-p-srlw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-srlw.json)|![rv64ui-p-sub](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sub.json)|![rv64ui-p-subw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-subw.json)|![rv64ui-p-sw](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-sw.json)|![rv64ui-p-xor](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-xor.json)|![rv64ui-p-xori](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-xori.json)|
|![rv64mi-p-access](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-access.json)|![rv64mi-p-breakpoint](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-breakpoint.json)|![rv64mi-p-csr](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-csr.json)|![rv64mi-p-ma_addr](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-ma_addr.json)|![rv64mi-p-ma_fetch](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-ma_fetch.json)|![rv64mi-p-mcsr](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64mi-p-mcsr.json)|
|![rv64ui-p-fence_i](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-fence_i.json)|![rv64ui-p-simple](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64ui-p-simple.json)|
|![ISA](https://img.shields.io/badge/ISA-RV64C-yellowgreen)|
|![rv64uc-p-rvc](https://img.shields.io/endpoint?style=plastic&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhutddk%2FRiftCore%2Fgh-pages%2Fci%2Frv64uc-p-rvc.json)|









------------------------------------

## Sponsors

![BTC](https://img.shields.io/badge/BTC-124egseDMD983etDrsAzUnXvi6twpWtjLd-orange)
![ETH](https://img.shields.io/badge/ETH-0x2f8aeb5f9dfe2936632f47363a42d7f71810c62b-lightgrey)


