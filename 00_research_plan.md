# 研究方針：滑らかな三次超曲面のPoisson構造の代数的量子化

2026-11-21 / v1。研究の再開時には本書、`AGENTS.md`、`notes/cubic_quantization.md`、`papers/cubic-quantization.tex` の順で読む。研究全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。

## 唯一の研究目標と達成基準

**滑らかな三次超曲面のPoisson構造の代数的量子化。** 複素数体上の任意の滑らかな射影三次超曲面 `X=V(F)⊂P^{n+1}`（`n≥3`）上の正則Poisson構造について、原点を含む代数的パラメータ開上で古典極限を指定した次数付きPBW・AS正則ambientと正則中心三次元・中心商を構成し、正則性、係数環上の選択、同変性、降下の成立範囲と障害を明らかにする。各ブロックの量子化を一ブロックに制限せず、全次元・全Poisson正規形を扱う。関連する中心線束、gerbe、二次包絡、点曲線の計算は**この一目標を達成・検証するための手段・付随結果**であり、別の研究目標ではない。三次以外の超曲面や完全交叉への一般化は本プロジェクトの研究目標に含めない。

## 主な現行到達点・仮定・証明の所在

- 全次元・全正規形ブロックの零パラメータ近傍の代数的中心三次量子化：`papers/sections/quantization/algebraic_quantization.tex` と `general_dimension_universal_quantization.tex`。滑らかな全体三次Fを仮定し、三変数制限の滑らかさは要求しない。全パラメータ値での結論ではない。
- 係数環上のCasimir中心持上げとCramer式：`universal_casimir_determinant.tex`。普遍Hesse・Fermat・節点・尖点の公式は各対応する節。
- 全support階数二と満support多ブロックの同変な選択、三次Veronese降下および `gcd(n+2,3)` に依存するgerbe：`intrinsic_rank_two_center.tex`、`full_support_quantization.tex`、`equivariant_central_lifts.tex`。零切断近傍での結果と全パラメータの主張を区別する。
- 精密な主張、証明、仮定は [主論文](papers/cubic-quantization.tex)、証明以外の現行知識・未解決障害は [量子化ノート](notes/cubic_quantization.md)、先行結果・確認済み箇所は [参考文献](papers/quantization-references.tex)、厳密計算と証明書は [computations/quantization](computations/quantization/README.md)。既存原稿に証明があることと今回証明を再検証したことを区別する。既知のEtingof–Ginzburg、Mori–Smith等の結果を本研究の新規性と取り違えない。

## 最優先の未解決課題と着手方法

1. 中心変数の残る複数ブロック（`m>0, k≥2`）で、中心三次の係数環上の同変な選択・降下が成立する範囲を判定する。該当層の古典中心核とコホモロジー・対称群作用を調べ、満supportのアフィン底の場合を無条件には流用しない。
2. 特異な三変数制限に対する中心元の有限・明示的表示と、正則な中心商の成立開を精密化する。`computations/quantization` の保存証明書と独立計算で公式を照合する。
3. 相対的な選択の一意性・規格化・中心idealの違い、固定した非零パラメータでの同型類の像を整理する。証明のない非同型・全h・qgr滑らかさを主張しない。
4. 現行原稿の各定理の仮定と引用元を一次文献で精査し、既知定理との重複を解消して公表可能な日本語LuaLaTeX論文に仕上げる。

## 他研究との関係

古典Poisson正規形・退化・モジュライは [poisson-cubic](https://github.com/uedakazushi/poisson-cubic) を入力とする。一般中心三次変形のMF移送・可換復元・O-marked moduli・Kuznetsov比較は [nc-cubic](https://github.com/uedakazushi/nc-cubic) の独立研究であり、**本研究の量子化の存在証明にKu比較を使わない**。量子化論文はambientをA、中心商をBと記す。nc-cubicでは逆なので引用時に明示する。

## 研究全体に共通する一般原則と保存許可

- 重要性・新規性・正確性・実現可能性を総合して研究方針を更新する。ただしユーザー指定の上記唯一の研究目標を勝手に拡張しない。方針・ノートは履歴ではなく現行内容へ整理し、有効な証明・反例・再現資産を失わない。
- 証明済み、追加仮定付き、未完成、予想、計算的観察を区別し、主張の仮定・証明箇所・依存結果・未解決箇所を記す。原稿記載、今回の証明点検、計算、形式的検証の状態を混同しない。誤りは依存する要約・本文も訂正する。
- 公表用原稿は日本語LuaLaTeXで `papers/cubic-quantization.tex` を本文のある正本とする。著者欄は空欄。主張に必要な証明・入力・コード・証明書を保持し、中間生成物、旧版、ログ、キャッシュ、PDF・ZIPをGitで追跡しない。
- `main` を唯一の現行正本とし、確認できた研究の区切りに通常コミット・pushを再承諾なしに行う。長い作業は約15–30分で保存する。force push、GitHub Actionsの追加・起動は禁止。他の作業者の変更を保持する。Libraryへの定常的二重保存はしない。push不能時の緊急保存だけを例外とし、既存Libraryファイルを指示なく削除しない。
- 組版は `latexmk` / LuaLaTeX / SyncTeX と VS Code のLaTeX Workshopで可能にし、入力・引用・欠落と必要な範囲の計算を確認する。未実行の検証を成功と記さない。
- 作業の区切りにはまず本repoの原稿・ノート・方針・READMEを `main` に保存し、その結果に基づいて [research-hub](https://github.com/uedakazushi/research-hub) の該当研究を更新する。hubには到達点、確実性、次の課題、依存関係、再開先と実際の確認日だけを簡潔に記す。両repoの反映を別々に確認する。
