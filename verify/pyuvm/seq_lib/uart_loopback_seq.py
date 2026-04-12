"""UART loopback sequence — enables loopback, sends TX data, reads RX data."""

import random

from pyuvm import uvm_sequence, ConfigDB

from cf_verify.bus_env.bus_seq_lib import write_reg_seq, read_reg_seq
from seq_lib.uart_config import uart_config


class uart_loopback_seq(uvm_sequence):
    def __init__(self, name="uart_loopback_seq"):
        super().__init__(name)
        self.monitor = None

    async def body(self):
        regs = ConfigDB().get(None, "", "bus_regs")
        addr = regs.reg_name_to_address

        config = uart_config("config")
        await config.start(self.sequencer)

        # Enable loopback (en + txen + rxen + lpen [+ gfen])
        ctrl = 0x1F if config.is_glitch_filter_en else 0x0F
        await write_reg_seq("lpbk", addr["CTRL"], ctrl).start(self.sequencer)

        for _ in range(3):
            n_send = random.randint(1, 3)
            for _ in range(n_send):
                data = random.randint(0, 0x1FF)
                await write_reg_seq("tx_wr", addr["TXDATA"], data).start(self.sequencer)
