This is quite simple script. You can do all this stuff manually without this script.

It use built-in Airport Extreme card for grab your pattern from wireless traffic.

It can be used **only in open Wi-Fi network**.

#### What it doing: 

* Swith Airport card into monitor mode on selected channel.
```sudo "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport" en0 sniff 10```
Where en0 - Aiport card, 10 - channel

To find which channel use your network hold ```Alt``` and click on wifi icon:

![CHANNEL](http://cdn.zhovner.com/forever/wifi_channel.png)

