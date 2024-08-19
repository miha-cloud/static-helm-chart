#!/bin/bash

# Kiểm tra số lượng tham số đầu vào
if [ "$#" -ne 2 ]; then
    echo "Sử dụng: $0 <địa chỉ IP> <tên host>"
    exit 1
fi

# Lưu địa chỉ IP và tên host từ tham số dòng lệnh
ip_address=$1
host_name=$2

# Thêm cấu hình vào /etc/hosts
echo "$ip_address    $host_name" | sudo tee -a /etc/hosts > /dev/null

echo "Đã thêm $host_name với địa chỉ IP $ip_address vào /etc/hosts."
