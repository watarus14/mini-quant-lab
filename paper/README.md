# paper/
論文・文書（編集はローカル）。
- ビルド: `cd paper && latexmk -outdir=build main.tex`
- figures/: 採用した図だけ。`scripts/pick-figure.sh` で results/ から選んでコピーする（出所が SOURCES.tsv に残る）
