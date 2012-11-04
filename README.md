This is quite simple script. You can do all this stuff manually without the script.

It use built-in Airport Extreme card for grab your pattern from wireless traffic.

It can be used **only in open Wi-Fi network**.

#### What it doing: 

* Swith Airport card into monitor mode on selected channel.
```sudo "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport" en0 sniff 10```
Where en0 - Aiport card, 10 - channel. It will write dump in .cap file localted in /tmp/.

To find which channel use your network hold ```Alt``` and click on wifi icon:

![CHANNEL](http://cdn.zhovner.com/forever/wifi_channel.png)

* Match your regexp in .cap file in cycle and exclude duplicates strings.

#### Usage:

```sudo airsniff.py <channell> <\"pattern\">````

 ** <channell> ** — wifi channel

 **<\"pattern\">** — regexp that will grep /tmp/*.cap file. Quotes and backslashes required!

Example for vk.com:

```airsniff.py 10 \"remixsid=[a-z0-9]{68}\"```

