data=www_etungo_com_tw
echo '5.How many AD click per clientId?: no.AD_per_clientId.txt'
cat $data|jq -r '"\(.[":clientId"]),\(.["Time"]),\(.uradTracker.CurrentURL)"' |grep 'UTM'|awk -F ',' '{print $1}'|sort |uniq -c|awk '{print $2,$1}' OFS="," >dic_4_ADs.txt
