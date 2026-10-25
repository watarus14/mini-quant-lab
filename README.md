# mini-quant-lab

目的: (ここに書く)

## サーバー


## 運用
研究室の運用ルール（lab-workflow）を参照。
- notebooks/: サーバーで編集（Jupyterで対話的に） → commit/push
- src scripts config paper docs: ローカルで編集 → commit/push。試すだけなら `scripts/sync.sh <server> code-push`
- commit/push は変更を作った場所で。サーバー側の pull は `git pull --rebase --autostash`
- ローカル: `git pull --rebase`、`scripts/sync.sh <server> results-pull`（結果の保管）
- 実行ごとに `scripts/new-run.sh <tag>` で runs/<run_id>/ を作る
- 論文の図: `scripts/pick-figure.sh <server> <run_id> <path>`
