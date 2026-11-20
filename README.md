# 滑らかな三次超曲面のPoisson構造の代数的量子化

2026-11-21 / v1。**研究の唯一の目標は、滑らかな三次超曲面のPoisson構造の代数的量子化です。** 三次以外への一般化や非可換モジュライの分類を独立目標にしません。

再開時は [研究方針](00_research_plan.md) を最初に確認してください。現行論文は [papers/cubic-quantization.tex](papers/cubic-quantization.tex)（日本語LuaLaTeX、著者欄空欄）、現行研究ノートは [notes/cubic_quantization.md](notes/cubic_quantization.md)、先行文献の確認は [量子化参考文献](papers/quantization-references.tex)、監査ノートは [notes/quantization_audit.md](notes/quantization_audit.md) です。

## 内容と対象範囲

複素数体上の滑らかな三次超曲面 `X⊂P^{n+1}`（`n≥3`）上の正則Poisson構造に対し、代数的パラメータ開でPBW/AS正則ambientと指定Casimirへ特殊化する正則中心三次元を構成する。全正規形ブロック、係数環上の中心持上げ、Fermat/Hesseと特異三変数制限の公式、同変的中心元・三次Veronese降下・障害を扱う。全hでの成立、全qgrの滑らかさ、異なる中心商の非同型性を証明済みとは扱わない。

古典正規形とPoissonモジュライは [poisson-cubic](https://github.com/uedakazushi/poisson-cubic)、この量子化を入力とする非可換三次の復元・モジュライ・Kuznetsov比較は [nc-cubic](https://github.com/uedakazushi/nc-cubic) が正本。量子化の存在証明は復元定理を必要としない。

## ソースと再現

- 主原稿：`papers/cubic-quantization.tex`、節：`papers/sections/quantization/`、プリアンブル：`papers/quantization-common.tex`、文献：`papers/quantization-references.tex`
- 計算・再現： [computations/quantization/README.md](computations/quantization/README.md)、同フォルダ内のPythonスクリプト、JSON証明書と検証結果。 `requirements.txt` を参照
- ソース検査：`python3 scripts/check_sources.py`。組版：リポジトリ直下から `latexmk -lualatex papers/cubic-quantization.tex`。出力は `build/`、SyncTeXあり。VS CodeのLaTeX Workshop設定は `.vscode/`

2026-11-21の分離では `nc-cubic` から既存の論文・量子化節・ノート・計算資産を内容を維持して移した。移管自体を証明や独立計算の再実施とはみなさない。正本はこのリポジトリの `main`、運用は [AGENTS.md](AGENTS.md)。
