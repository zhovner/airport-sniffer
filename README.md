This is quite simple script. You can do all this stuff manually without the script.

It uses Airport Extreme card for grab your pattern from wireless traffic.

It can be used **only in open Wi-Fi network**.

#### How it works: 

* Turn Airport card into monitor mode on selected channel.

```sudo "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport" sniff 10```

It will write dump in .cap file localted in /tmp/.

To find out what channel number is used on your network hold ```Alt``` and click on wifi icon:

![CHANNEL](http://i.imgur.com/oeZrN1m.png)

* In cycle matches your regexp in .cap file and excluding duplicate strings.

#### Usage:

```sudo ./airsniff.py <channel> <"pattern">```

 **channel** — wifi channel

 **"pattern"** — regexp that will grep /tmp/*.cap file. Quotes  required!

Example for vk.com:

```sudo ./airsniff.py 10 "remixsid=[a-z0-9]{53}"```
