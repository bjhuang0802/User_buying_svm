data=www_etungo_com_tw
echo '3.Generate no. of session per clientId: dic_sessions.txt'
cat session_sort.csv |awk -F ',' '{print $1}' |uniq -c |awk '{print $2,$1}' OFS="," |sort -t, -k2 -g >dic_2_sessions.txt 
