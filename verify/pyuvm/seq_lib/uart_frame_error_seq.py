"""UART frame error sequence — sends corrupted frames to trigger frame errors."""

import cocotb
from cocotb.triggers import ClockCycles
from pyuvm import uvm_sequence, ConfigDB

from seq_lib.uart_config import uart_config


class uart_frame_error_seq(uvm_sequence):
    """Drives the RX line directly to inject frame errors (bad stop bits)."""

    async def body(self):
        regs = ConfigDB().get(None, "", "bus_regs")
        addr = regs.reg_name_to_address
        dut = ConfigDB().get(None, "", "DUT")

        # Configure UART via bus side first
        from cf_verify.bus_env.bus_seq_lib import write_reg_seq
        # Enable clock gate
        if "GCLK" in addr:
            await write_reg_seq("gclk", addr["GCLK"], 1).start(self.sequencer)
        await write_reg_seq("ctrl_off", addr["CTRL"], 0).start(self.sequencer)
        await write_reg_seq("pr", addr["PR"], 2).start(self.sequencer)
        cfg = 8 | (0x3F << 8)  # 8 bit, no parity, no extra stop
        await write_reg_seq("cfg", addr["CFG"], cfg).start(self.sequencer)
        await write_reg_seq("im", addr["IM"], 0x3FF).start(self.sequencer)
        await write_reg_seq("ctrl_on", addr["CTRL"], 0x07).start(self.sequencer)

        bit_n_cyc = (2 + 1) * 8

        for _ in range(3):
            # Start bit
            dut.RX.value = 0
            await ClockCycles(dut.CLK, bit_n_cyc)

            # 8 data bits
            for i in range(8):
                dut.RX.value = (0xA5 >> i) & 1
                await ClockCycles(dut.CLK, bit_n_cyc)

            # Bad stop bit (0 instead of 1)
            dut.RX.value = 0
            await ClockCycles(dut.CLK, bit_n_cyc)

            # Recovery
            dut.RX.value = 1
            await ClockCycles(dut.CLK, bit_n_cyc * 3)

        # Check frame error flag
        from cf_verify.bus_env.bus_seq_lib import read_reg_seq
        await read_reg_seq("ris_fe", addr["RIS"]).start(self.sequencer)
