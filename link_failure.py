from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet

log = core.getLogger()

# Handle PacketIn (CUSTOM LOGIC)
def _handle_PacketIn(event):
    packet = event.parsed
    log.info("Packet received from %s to %s", packet.src, packet.dst)

# Detect Link Failure
def _handle_LinkEvent(event):
    if event.added:
        log.info("Link Added: %s", event.link)
    elif event.removed:
        log.info("Link Removed (Failure Detected): %s", event.link)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow_discovery.addListenerByName("LinkEvent", _handle_LinkEvent)
    log.info("Custom SDN Controller Loaded")
