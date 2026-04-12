"""UART timeout sequence — verifies RX timeout interrupt after idle period."""

import cocotb
from cocotb.triggers import ClockCycles
from pyuvm import uvm_sequence, ConfigDB

from cf_verify.bus_env.bus_seq_lib import write_reg_seq, read_reg_seq
from seq_lib.uart_config import uart_config


class uart_timeout_seq(uvm_sequence):
    async def body(self):
        regs = ConfigDB().get(None, "", "bus_regs")
        addr = regs.reg_name_to_address
        dut = ConfigDB().get(None, "", "DUT")

        # Configure with short timeout (timeout=3 bit times)
        timeout_val = 3
        wlen = 8
        cfg = wlen | (timeout_val << 8)
        config = uart_config("config", config=cfg, im=0x3FF, prescaler=2)
        await config.start(self.sequencer)

        # Wait for timeout to expire (idle on RX line)
        bit_n_cyc = (2 + 1) * 8
        total_wait = (timeout_val + 1) * bit_n_cyc * 2
        await ClockCycles(dut.CLK, total_wait)

        # Check that timeout flag is set
        await read_reg_seq("ris_timeout", addr["RIS"]).start(self.sequencer)
        await read_reg_seq("mis_timeout", addr["MIS"]).start(self.sequencer)

        # Clear timeout interrupt
        await write_reg_seq("ic_timeout", addr["IC"], 1 << 9).start(self.sequencer)
        await read_reg_seq("ris_cleared", addr["RIS"]).start(self.sequencer)
