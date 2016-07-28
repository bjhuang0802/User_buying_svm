data=www_etungo_com_tw
echo '4.Time per log, total staying time per clientId'
echo 'and time of product-view per log.'
echo '--> dic_time_per_log.txt, dic_3_tstime.txt, dic_product_time.txt'
python evaltime.py
cat dic_time_per_log.txt |grep 'Product' |awk -F ',' '{if($5>0.0 && $5<10.0)print $1,$4,$5}' OFS=","|tr -d ' ' >dic_product_time.txt
echo 'Evaluate product-view infomation: dic_product_summary.txt'
python evalptime.py