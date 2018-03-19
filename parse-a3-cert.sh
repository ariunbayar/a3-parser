#!/bin/bash

script_dir=$(dirname "$(readlink -e "$0")")

a=1

while [[ $a -le 450 ]]; do
    curl 'https://tender.gov.mn/mn/exam/examcertificatelist' \
        -H 'Pragma: no-cache' \
        -H 'Origin: https://tender.gov.mn' \
        -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Accept-Language: en-US,en;q=0.8,ru;q=0.6' \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' \
        -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \
        -H 'Cache-Control: no-cache' \
        -H 'X-Requested-With: XMLHttpRequest' \
        -H 'Cookie: PHPSESSID=6eou1tcbt522do1enbi7pdvu66' \
        -H 'Connection: keep-alive' \
        -H 'Referer: https://tender.gov.mn/mn/exam/' \
        --data "certificateNumber=&lastName=&firstName=&industryId=&startDate=&endDate=&aimagId=&districtId=&page=$a" \
        --compressed 2> /dev/null | "$script_dir/manage.py" parse-a3
    echo "Current page: $a, Date: $(date -Iseconds)"
    a=$(($a + 1))
done

echo
echo "+-------------+"
echo "|  COMPLETED  |"
echo "+-------------+"
echo
