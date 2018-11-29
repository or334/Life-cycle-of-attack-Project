import subprocess

numbers = [000]
ip = "192.168.42."  # get_ip_range()
for i in range(1, 254):
    hostname = ip + str(i)  # range
    try:
        response = subprocess.check_output(['ping', '-n', '1', '-l', '1',hostname])  # in linux -c
        print(hostname, 'is up!')
        numbers.append(i)
    except subprocess.CalledProcessError:
        print(hostname, 'is down!')

print(numbers.__len__())
print(numbers)






