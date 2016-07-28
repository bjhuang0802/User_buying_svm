data=www_etungo_com_tw
#cat $data|jq -r '"\(.[":clientId"]),\(.Time),\(.uradTracker.Event),\(if .uradTracker.Event == "Product" then .uradTracker.Items|.[].ProductID else "0" end)"' |sort -t, -k1 -k2 -g >logs_sort.csv
cat $data|jq -r '"\(.[":clientId"]),\(.Time),\(.uradTracker.Event),\(if .uradTracker.Event == "Product" then .uradTracker.Items|.[].ProductID else "0" end)"' 
