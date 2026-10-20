# Which web addresses the toolkit fetches

Read by every skill that takes a web address from the builder and every agent with
`WebFetch`. Not part of a run on its own.

**The rule.** A web address is fetched only if it is `http` or `https` and its site is on
the public internet. Never fetch an address that:

- uses any other scheme (`file:`, `ftp:`, `gopher:`, `data:`, and so on);
- carries a user name or password (`https://user:pass@...`);
- names `localhost`, a single-word name with no dot, or a name ending in `.localhost`,
  `.local`, `.internal`, `.lan`, `.home.arpa`, `.intranet`, or `.corp`;
- is, or resolves to, a loopback, private, link-local, carrier-grade NAT, multicast, or
  reserved address, written as a number or as a name. That covers `127.0.0.0/8`, `10.0.0.0/8`, `172.16.0.0/12`,
  `192.168.0.0/16`, `169.254.0.0/16` (which holds the cloud metadata service at
  `169.254.169.254`), `100.64.0.0/10`, `0.0.0.0`, `::1`, `fc00::/7`, and `fe80::/10`.

**Why.** The builder's workspace runs in the cloud, where internal addresses and the
metadata service are reachable from inside it. A fetch is a request made from the
workspace, so an address the builder pastes, or a link a page points to, must not be able
to reach anything that is not a public website.

**Skills: check before dispatching.** A skill that hands a builder-supplied address to an
agent checks every address against the rule above first, by reading it. No command runs
for this, so a public address passes with nothing extra on the builder's screen. Pass on
only the addresses that pass. For one that doesn't, tell the builder in one plain line
that the address isn't a public website so it won't be read, and ask for the public
address instead. Never work around a refusal.

**Agents: hold the rule on every fetch.** That covers the address they were handed, the pages they choose to
follow from it, and every result a search returns. Skip any address the rule refuses,
and note it in one line in the output's gaps or read-quality section.
