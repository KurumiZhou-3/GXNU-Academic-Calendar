import psutil
import socket
import pprint


class Interface:
    @staticmethod
    def get_local_net_interface_name() -> list:
        """
        (Base on psutil)\n
        Return the local machine net interface name in a list
        :return:
        """
        return list(psutil.net_if_addrs().keys())

    @staticmethod
    def get_local_net_interface() -> list:
        """
        (Base on psutil)\n
        Return the local machine net interface items(psutil) in a list
        :return:
        """
        return list(psutil.net_if_addrs().items())

    @staticmethod
    def get_ipv4_interface() -> dict:
        """
        (Base on psutil)\n
        Return the net interface item of using the ipv4 address from all the local net interface
        :return:
        """
        ipv4_dict = {}
        for name, addrs in psutil.net_if_addrs().items():
            ipv4_dict[name] = [addr for addr in addrs if addr.family == socket.AF_INET][0]
        return ipv4_dict

    @staticmethod
    def get_ipv6_interface() -> dict:
        """
        (Base on psutil)\n
        Return the net interface item of using the ipv6 address from all the local net interface
        :return:
        """
        ipv6_dict = {}
        for name, addrs in psutil.net_if_addrs().items():
            ipv6_dict[name] = [addr for addr in addrs if addr.family == socket.AF_INET6][0]
        return ipv6_dict

    @staticmethod
    def get_ipv4_address() -> list:
        """
        (Base on psutil)\n
        Return all ipv4 address from local net interface in a list
        :return:
        """
        return [addr.address for addr in Interface.get_ipv4_interface()]

    @staticmethod
    def get_ipv6_address() -> list:
        """
        (Base on psutil)\n
        Return all ipv6 address from local net interface in a list
        :return:
        """
        return [addr.address for addr in Interface.get_ipv6_interface()]

    @staticmethod
    def get_detail_interface_ipv4(interface_name: str) -> str:
        """
        (Base on psutil)\n
        Give a local net interface_name and return its ipv4 address
        :param interface_name:
        :return:
        """
        ipv4_interface_dict = Interface.get_ipv4_interface()
        result_return = None

        for temp_interface_name, interface_data in ipv4_interface_dict.items():
            if temp_interface_name == interface_name:
                result_return = interface_data.address

        return result_return

    @staticmethod
    def get_detail_interface_ipv6(interface_name: str) -> str:
        """
        (Base on psutil)\n
        Give a local net interface_name and return its ipv6 address
        :param interface_name:
        :return:
        """
        ipv4_interface_dict = Interface.get_ipv6_interface()
        result_return = None

        for temp_interface_name, interface_data in ipv4_interface_dict.items():
            if temp_interface_name == interface_name:
                result_return = interface_data.address

        return result_return


if __name__ == "__main__":
    # pprint.pprint(Interface.get_detail_interface_ipv6("以太网"))

    pprint.pprint(Interface.get_ipv4_interface())
