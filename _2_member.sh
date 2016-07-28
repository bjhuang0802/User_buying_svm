data=www_etungo_com_tw
echo '2.Generate unique Member: dic_member.txt'
cat $data |jq -r '"\(.[":clientId"]),\(.["uradTracker"].Member)"' |awk -F ',' '{if($2==1) print $1}'|sort -g|uniq  >dic_1_member.txt
