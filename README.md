# The World Today — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/AndryXSad/news-image-20261120-v1/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/AndryXSad/news-image-20261120-v1/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun competition
[Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120)
(`news-image-20261120`).

## The image

A one-page newspaper poster, **"THE WORLD TODAY — FRIDAY 20 NOVEMBER 2026"**,
drawn from scratch with PIL in `render_poster.py` (1024×1024 PNG).
It sums up the day's world news:

- **Lead:** the first-ever Trump–Xi–Putin three-way summit in Shenzhen and
  its joint peace declaration.
- **Justice:** the ICJ's 9–6 ruling that Myanmar committed genocide against
  the Rohingya — the first time a state has been found responsible.
- **Markets in turmoil:** the AI sell-off (S&P −2.0%, Nikkei −4.5%,
  Kospi −4.7%) despite Anthropic's record IPO debut (+17% to ~$97).
- **Weather & climate:** Cyclone Akvan's landfall in Odisha (300,000+
  evacuated) and COP31 closing in Antalya with fossil fuels dropped
  from the draft deal.
- **Around the World:** 12 short stories across the Middle East, Ukraine,
  Europe, Asia, the USA, Africa, science, energy and France — plus sport
  (ATP Finals, NZ v India cricket, NFL, rugby).

Every fact was checked against news reported on 19–20 November 2026
(Reuters, ICJ/UN, IMD, TASS/AFP and others); sources are named on the
poster itself.

## How it runs

`main.py` (Python standard library only) copies the pre-rendered
`entry.png` to the output directory:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

Re-render the poster from scratch with:

```sh
python3 render_poster.py   # writes entry.png (deterministic)
```

## License

MIT — see [LICENSE](LICENSE).
