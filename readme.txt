/*
	Copyright 2024 Efabless Corp.

	Author: Efabless Corp. (ip_admin@efabless.com)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

# CF_UART IP Core

## Overview
This repository contains the CF_UART IP core, a Universal Asynchronous Receiver-Transmitter (UART) implementation designed for integration into System-on-Chip (SoC) designs.

## Repository Structure

### Core Files
- **CF_UART_regs.h**: Header file containing the register definitions for the CF_UART interface.

### Hardware Description Language (HDL) Files
- **CF_UART.v**: Verilog source code for the CF_UART design, including the core logic of the UART module.

### Bus Interface Wrappers
- **CF_UART_AHBL.v**: Verilog wrapper to interface the CF_UART with the AMBA High-performance Bus (AHB-Lite) protocol.
- **CF_UART_APB.v**: Verilog wrapper to interface the CF_UART with the Advanced Peripheral Bus (APB) protocol.
- **CF_UART_WB.v**: Verilog wrapper to interface the CF_UART with the Wishbone bus protocol.

### Design for Test (DFT) Wrappers
- **CF_UART_AHBL_DFT.v**: Verilog wrapper with Design for Test (DFT) support specific to the AHB-Lite interface of the CF_UART .
- **CF_UART_APB_DFT.v**: Verilog wrapper with DFT support specific to the APB interface of the CF_UART.
- **CF_UART_WB_DFT.v**: Verilog wrapper with DFT support specific to the Wishbone interface of the CF_UART.

### Documentation
- **CF_UART.pdf**: Comprehensive documentation for the CF_UART, including its features, configuration, and usage.