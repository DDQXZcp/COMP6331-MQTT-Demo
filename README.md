# Mosquitto
## Local MQTT
### Subscriber
```
mosquitto_sub -h localhost -t "comp3310/demo" -q 2
```
### Publisher
```
mosquitto_pub -h localhost -t "comp3310/demo" -q 2 -m "Hello students, this is MQTT QoS 2!"
```
## LAN MQTT
### Subscriber
```
mosquitto_sub -h <Broker IP Addr> -t "comp3310/demo" -q 2
```
### Publisher
```
mosquitto_pub -h <Broker IP Addr> -t "comp3310/demo" -q 2 -m "Hello from publisher"
```