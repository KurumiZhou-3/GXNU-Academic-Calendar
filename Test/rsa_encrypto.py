import math
from sys import executable


def rsa_encrypt(password, exponent, modulus):
    """
    实现教务系统SSO登录的RSA加密逻辑
    :param password: 原始密码字符串
    :param exponent: RSA公钥指数（通常为"10001"）
    :param modulus: RSA模数（十六进制字符串）
    :return: 加密后的密码字符串
    """
    # 1. 字符串反转
    reversed_pwd = password[::-1]

    # 2. 将模数转换为整数
    modulus_int = int(modulus, 16)
    exponent_int = int(exponent, 16)

    # 3. 计算chunkSize
    # 在JavaScript中: chunkSize = 2 * biHighIndex(m)
    # 在Python中: biHighIndex(m) = (modulus_int.bit_length() - 1) // 16 * 2
    # 但更准确的计算方式是:
    # chunkSize = (modulus_int.bit_length() // 8) - 1
    # 但根据JavaScript代码注释，chunkSize = 2 * (number of digits in modulus - 1)
    # 我们用更准确的方式计算：
    hex_modulus = hex(modulus_int)[2:]
    num_hex_digits = len(hex_modulus)
    chunk_size = (num_hex_digits // 2) * 2 - 2  # 每个十六进制数字4位，2个字节

    # 4. 将字符串转换为字符码数组
    char_codes = [ord(c) for c in reversed_pwd]

    # 5. 补零使长度能被chunkSize整除
    while len(char_codes) % chunk_size != 0:
        char_codes.append(0)

    # 6. 分块处理并加密
    result = []
    for i in range(0, len(char_codes), chunk_size):
        # 取出当前块
        block = char_codes[i:i + chunk_size]

        # 将字符码转换为BigInt（Python的int可以直接处理）
        # 每两个字符组成一个16位数字
        block_int = 0
        for j in range(len(block)):
            block_int = (block_int << 8) | block[j]

        # 7. RSA加密：pow(block_int, exponent_int, modulus_int)
        encrypted_block = pow(block_int, exponent_int, modulus_int)

        # 8. 转换为十六进制字符串
        hex_block = hex(encrypted_block)[2:]
        # 补零到固定长度
        hex_block = hex_block.zfill(num_hex_digits)
        result.append(hex_block)

    # 9. 用空格分隔各块
    return " ".join(result)

def rsa_encrypt2(password, exponent, modulus):
    """
    精确复现广西师范大学教务系统前端RSA加密逻辑
    参数：
        password: 原始密码字符串（如 "#//Zzpxv13423138646"）
        exponent: 公钥指数（如 "10001"）
        modulus: 模数（十六进制字符串，如 "A1B2C3..."）
    返回：
        加密后的字符串，格式如："ABC123 DEF456 ..."
    """
    # Step 1: 字符串反转
    reversed_pwd = password[::-1]

    # Step 2: 将十六进制字符串转为大整数
    e_int = int(exponent, 16)
    n_int = int(modulus, 16)

    # Step 3: 计算 chunkSize（关键！必须与JS一致）
    # JS: chunkSize = 2 * biHighIndex(this.m)
    # biHighIndex(m) = m的十六进制字符长度 // 2 - 1？不，是BigInt内部digit数组的最高索引
    # 在JS中，biHighIndex计算的是非零最高位digit的索引
    # 我们用更精确的方式：模拟JS的biHighIndex

    def bi_high_index(n):
        """模拟JS中RSAUtils.biHighIndex的行为"""
        if n == 0:
            return 0
        # JS中每个digit是16位（0-65535），所以计算需要多少个digit
        bits = n.bit_length()
        digits = (bits + 15) // 16  # 向上取整
        return digits - 1

    chunk_size = 2 * bi_high_index(n_int)

    # Step 4: 字符串转字符码数组
    a = [ord(c) for c in reversed_pwd]

    # Step 5: 补零到chunkSize的整数倍
    while len(a) % chunk_size != 0:
        a.append(0)

    # Step 6: 分块加密
    result_parts = []
    al = len(a)

    for i in range(0, al, chunk_size):
        # 创建block（模拟JS中的BigInt）
        # JS: block.digits[j] = a[k++] + (a[k++] << 8)
        block_value = 0
        j = 0
        k = i
        # 注意：JS中是每两个字节组成一个16位数，存入digits数组
        # 但我们不需要模拟整个BigInt类，只需要计算最终的整数值
        digits = []
        while k < i + chunk_size:
            low_byte = a[k]
            k += 1
            if k < i + chunk_size:
                high_byte = a[k]
                k += 1
            else:
                high_byte = 0
            digit_value = low_byte + (high_byte << 8)
            digits.append(digit_value)

        # 将digits数组转换为一个大整数（模拟JS的BigInt存储方式）
        # JS中digits[0]是最低位，digits[1]是次低位，以此类推
        block_int = 0
        for digit_idx in range(len(digits) - 1, -1, -1):
            block_int = (block_int << 16) | digits[digit_idx]

        # Step 7: 执行模幂运算（RSA核心）
        crypt = pow(block_int, e_int, n_int)

        # Step 8: 转换为十六进制字符串（无前缀，大写）
        hex_text = hex(crypt)[2:].lower()

        # JS中biToHex不会补零，直接输出实际长度
        result_parts.append(hex_text)

    # Step 9: 用空格连接，去掉末尾空格
    return " ".join(result_parts)

if __name__ == '__main__':
    password = "#//Zzpxv13423138646"
    exponent = "10001"
    execution = "b951bd5efbf2bf7503fefcba60c7803c7f9649ddcbb6e7a19fc1863e4cbcee0856999d0d2e99238ac68691a2b718c01f464f124f73e7149447ea23cdf9cb28ab"

    enc_str = rsa_encrypt2(password, exponent, execution)
    print(enc_str)