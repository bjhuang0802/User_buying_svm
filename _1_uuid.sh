data=www_etungo_com_tw
echo '1.Generate unique clientId: dic_uniq_uid.txt'
cat $data|jq -r '.[":clientId"]' |sort -g |uniq  >dic_0_uuid.txt
