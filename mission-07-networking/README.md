# Mission 7 — Computer Networks

## 1. Task / objective
Explain the main network terms, check from the Terminal that my computer can reach a public website and look up its address with DNS, and describe step by step what happens when a website opens.

## 2. Work completed
- Filled in the table of network concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching, client-server).
- Ran a connectivity test and DNS lookups against `example.com`, and checked the website answered.
- Wrote a six-step explanation of what happens when I open a website.
- Kept my own IP address, Wi-Fi name and DNS server out of the saved output. The commands I chose only print information about `example.com`.

## 3. Commands / tools used

| Command | Purpose |
|---|---|
| `ping -c 4 example.com` | Sends 4 small test messages to `example.com` and reports whether they came back and how long they took |
| `dig example.com A +noall +answer` | Asks DNS for the IPv4 address(es) of the domain and prints only the answer section |
| `dig example.com AAAA +noall +answer` | Same, but for the IPv6 address |
| `curl -sI https://example.com \| head -n 1` | Requests only the headers of the page and shows the first line, which holds the status |

`+noall +answer` hides the part of `dig`'s output that names the DNS server my computer uses, because that would reveal my network.

## 4. My understanding

### Task 7.1 — Network concepts

| Concept | Explanation in my own words | Example |
|---|---|---|
| LAN | A network covering a small area, where devices are close and connected directly | The Wi-Fi at home or a computer lab |
| MAN | A network across a city or a large campus, bigger than a LAN | A college campus network joining several buildings, or a city's cable network |
| WAN | A network spread over big distances, often joining many LANs | The internet itself, or a company linking offices in different cities |
| DNS | The system that turns a name I can remember into the number address a computer needs | Turning `example.com` into `104.20.23.154` |
| Router | A device that joins networks and decides where to forward data next | The home Wi-Fi router connecting my LAN to my internet provider |
| Protocol | A set of agreed rules that devices follow so they understand each other | HTTP for web pages, DNS for lookups, ICMP for ping |
| Packet switching | Data is cut into small packets that can take different routes and are put back together at the end | A web page arriving as many packets |
| Client-server | A client asks for something and a server holds it and sends it back | My browser (client) asking a website's computer (server) for a page |

### Task 7.2 — What I observed
- **Connectivity test:** `ping` reached `example.com` with 4 packets sent and 4 received, 0% loss, and an average round trip of about 28.5 ms. A connectivity test tells me whether my computer can reach another machine over the network and how fast and reliable the connection is. It doesn't prove the website itself works, only that the machine answers.
- **DNS lookup:** `dig` showed the domain name, a TTL (a number of seconds, about 275 for the first answer, meaning how long the answer may be remembered), the record type (`A` for an IPv4 address, `AAAA` for IPv6) and the address. For `example.com` it returned two IPv4 addresses and one IPv6 address, so one name can map to more than one address.
- **Role of DNS in the browser:** computers find each other with IP addresses, not names, so when I type a website name the browser first asks DNS for the matching address, and only then can it contact the server.
- **Website check:** `curl` printed `HTTP/2 200`, which means the server answered successfully.

I did not publish my own IP address, Wi-Fi name or DNS server.

### Task 7.3 — What happens when I open a website

1. I type a web address such as `https://example.com` into the **browser**, which acts as the **client**.
2. The browser needs an IP address, so it asks **DNS** to turn the domain name into one. A cached answer may be used if the question was asked recently.
3. The browser opens a connection to that address using the rules of a **protocol**: HTTPS, which is HTTP with encryption, so what travels is hidden from others.
4. The request is broken into **packets** and passes from my computer through my **router**, then across my internet provider and several other routers, each one forwarding the packets towards the destination.
5. The **server** that hosts the website receives the request, finds the page and sends a response back the same way, again in packets, starting with a status such as `200 OK`.
6. My router passes the packets on to my computer, the browser puts them back together, and the page is **displayed** on my screen.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [evidence/mission-07/network-observations.txt](../evidence/mission-07/network-observations.txt): the `ping`, `dig` and `curl` output. It only contains information about the public website `example.com`.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Pushed to `main` on GitHub and checked there.
