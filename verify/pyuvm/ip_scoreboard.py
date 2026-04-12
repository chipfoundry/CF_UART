"""UART scoreboard — filters TX-only for IP side comparisons."""

from cf_verify.base.scoreboard import scoreboard
from ip_item.uart_item import uart_item


class uart_scoreboard(scoreboard):
    async def _compare_ip(self):
        """Only compare TX transactions; RX is verified via register reads."""
        while True:
            dut_tr = await self.ip_dut_fifo.get()
            if hasattr(dut_tr, "direction") and dut_tr.direction == uart_item.TX:
                ref_tr = await self.ip_ref_fifo.get()
                self._check("IP", dut_tr, ref_tr)
