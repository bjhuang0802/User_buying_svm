data=www_etungo_com_tw
echo '0.Generate unique clientId for Final: dic_uid_ever_final.txt'
cat $data|grep 'Final' |jq -r '.[":clientId"]' |sort -g |uniq >dic_ever_final.txt
