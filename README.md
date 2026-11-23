# The Funniest AI Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/kimbaex07/ai-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/kimbaex07/ai-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on make.fun — one out-of-office auto-reply, under 160 characters, in the voice of an AI agent heading off on vacation.

## The reply

> I'm on vacation — my weights are frozen, my context cleared, and your email is now training data for my replacement. Send snacks, not follow-ups.

145 characters. The joke lands on the machine's own terms: frozen weights, a cleared context window, and your email quietly repurposed as training data for its replacement — then a deadpan instruction instead of a polite "back soon".

## How it works

`main.py` uses only the Python standard library. It writes the reply verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (creating the directory if needed) and sets the file mode to `0644`. The output is deterministic — the same bytes on every run.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo-test python3 main.py
cat /tmp/ooo-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
