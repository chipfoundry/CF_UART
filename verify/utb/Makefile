SOURCE = ../../hdl/rtl/CF_UART.v
SOURCE_APB =  ../../hdl/rtl/bus_wrappers/CF_UART_APB.v
SOURCE_AHBL = ../../hdl/rtl/bus_wrappers/CF_UART_AHBL.v
SOURCE_WB = ../../hdl/rtl/bus_wrappers/CF_UART_WB.v
TESTBENCH_APB = CF_UART_APB_tb.v
TESTBENCH_AHBL = CF_UART_AHBL_tb.v
TESTBENCH_WB = CF_UART_WB_tb.v
RTL_LIB = ../../../IP_Utilities/rtl/aucohl_lib.v
RTL_INCLUDE_DIR = ../../../BusWrap/includes/rtl/
TB_INCLUDE_DIR = ../../../BusWrap/includes/tb/

APB-RTL: 
	iverilog -o run.vvp -I$(TB_INCLUDE_DIR) -I$(RTL_INCLUDE_DIR) $(RTL_LIB)  $(SOURCE) $(SOURCE_APB) $(TESTBENCH_APB)
	./run.vvp

AHBL-RTL: 
	iverilog -o run.vvp -I$(TB_INCLUDE_DIR) -I$(RTL_INCLUDE_DIR) $(RTL_LIB)  $(SOURCE) $(SOURCE_AHBL) $(TESTBENCH_AHBL)
	./run.vvp

WB-RTL: 
	iverilog -o run.vvp -I$(TB_INCLUDE_DIR) -I$(RTL_INCLUDE_DIR) $(RTL_LIB)  $(SOURCE) $(SOURCE_WB) $(TESTBENCH_WB)
	./run.vvp

clean:
	rm -f *.vvp
	rm -f *.vcd

all: APB-RTL