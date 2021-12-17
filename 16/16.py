from typing import NamedTuple
import typing as T
from functools import reduce

class Literal(NamedTuple):
    version: int
    typeid: int
    value: int
    def children(self)->list["ParsedPacket"]:
        return []
    def eval(self) -> int:
        return self.value

class Operator(NamedTuple):
    version: int
    typeid: int
    operands: list["ParsedPacket"]
    def children(self)->list["ParsedPacket"]:
        return self.operands
    def eval(self) -> int:
        if self.typeid==0:
            return sum(child.eval() for child in self.operands)
        elif self.typeid==1:
            return reduce(lambda x, y: x*y, (child.eval() for child in self.operands))
        elif self.typeid==2:
            return min(child.eval() for child in self.operands)
        elif self.typeid==3:
            return max(child.eval() for child in self.operands)
        elif self.typeid==5:
            return self.operands[0].eval() > self.operands[1].eval()
        elif self.typeid==6:
            return self.operands[0].eval() < self.operands[1].eval()
        elif self.typeid==7:
            return self.operands[0].eval() == self.operands[1].eval()
        assert 0, self.typeid
        return 0

ParsedPacket = T.Union[Literal, Operator]

def hex_to_bits(data: str) -> str:
    return "".join(bin(int(chr, 16)).split("b")[1].rjust(4, "0") for chr in data)

def parse_literal_payload(version:int, typeid:int, bits: str):
    outbits = ""
    cont = True
    while cont:
        byte, bits = bits[0:5],bits[5:]
        if byte is None:
            break
        cont, payload = bool(int(byte[0])), byte[1:]
        outbits += "".join(payload)

    return Literal(version, typeid, int(outbits, 2)), bits


def parse_operator(version: int, typeid: int, bits: str) -> tuple[ParsedPacket, str]:
    length_type_ID, bits = int(bits[0]), bits[1:]
    operator = Operator(version, typeid, [])
    if length_type_ID == 0:
        length, bits = int(bits[0:15], 2), bits[15:]
        sub_packet_data, bits = bits[0:length], bits[length:]
        while sub_packet_data:
            sub_packet, sub_packet_data = parse_packet(sub_packet_data)
            operator.operands.append(sub_packet)
    else:
        num_subpackets, bits = int(bits[0:11], 2), bits[11:]
        for _ in range(num_subpackets):
            subpacket, bits = parse_packet(bits)
            operator.operands.append(subpacket)

    return operator, bits

def parse_message(data:str) -> ParsedPacket:
    bits = hex_to_bits(data)
    return parse_packet(bits)[0]


def parse_packet(bits:str) -> tuple[ParsedPacket, str]:
    version, bits = bits[0:3], bits[3:]
    typeid, bits = bits[0:3], bits[3:]
    version, typeid = int(version, 2), int(typeid, 2)
    if typeid == 4:
        return parse_literal_payload(version, typeid, bits)
    else:
        return parse_operator(version, typeid, bits)

def count_version_sums(message: ParsedPacket) -> int:
    return message.version + sum(count_version_sums(child) for child in message.children())


# assert parse_message("D2FE28").version == 6
# assert parse_message("D2FE28").typeid == 4
# assert parse_message("D2FE28").value == 2021
print(parse_message("38006F45291200"))
print(parse_message("EE00D40C823060"))
print(count_version_sums(parse_message("8A004A801A8002F478")))
print(count_version_sums(parse_message(open("16.txt").read())))
print(parse_message("9C0141080250320F1802104A08").eval())
print(parse_message(open("16.txt").read()).eval())
