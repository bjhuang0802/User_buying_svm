cat dic_product_time.txt |grep 'Product'|awk -F ',' '{print $4}' |sort -g|uniq >dic_upid.txt
