# python 2
import socket

results = []

def main():
    n_lines = raw_input()
    n_lines = int(n_lines)

    validate_first_input(n_lines)

    for i in xrange(n_lines):
        addr = raw_input()
        validate_length_input(addr)
        if(is_valid_ipv4_address(addr)):
            print_valid_ipv4()
        elif(is_valid_ipv6_address(addr)):
            print_valid_ipv6()
        else:
            print_invalid_ip()

    for i in results:
        print(i)



def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def print_invalid_ip():
    str = "Neither"
    results.append(str)


def print_valid_ipv4():
    str = "IPv4"
    results.append(str)


def print_valid_ipv6():
    str = "IPv6"
    results.append(str)


def validate_length_input(a):
    assert (len(a) < 500 ), "The number of characters in each line will not exceed 500."


def validate_first_input(a):
    assert (a > 0), "First input shoud must be > 0."
    assert (a <= 50), "First input should be < 50."


if __name__ == "__main__":
    main()
