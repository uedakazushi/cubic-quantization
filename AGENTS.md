# AGENTS.md — cubic-quantization

2026-11-21 / v1。再開時には必ず `00_research_plan.md` を先に読み、`notes/cubic_quantization.md` と公表原稿を確認する。hub入口は https://github.com/uedakazushi/research-hub 。

- **唯一の研究目標**は「滑らかな三次超曲面のPoisson構造の代数的量子化」。三次以外の完全交叉、非可換モジュライの分類、Ku比較を新たな目標に追加しない。中心元、同変性、PBW/AS、gerbe、二次包絡などはこの目標のための内部成果として保持する。
- 現行主原稿は `papers/cubic-quantization.tex`（本文あり、日本語LuaLaTeX、著者欄空欄）。独立入力は `poisson-cubic` の正規形。 `nc-cubic` の復元・Ku比較を量子化の存在証明へ循環参照しない。A=ambient、B=中心商という本稿の記法を保持する。
- 現行ノートは `notes/cubic_quantization.md`、監査材料は `notes/quantization_audit.md`、計算資産と証明書は `computations/quantization/`。使う文献の仮定・具体的な参照箇所を明記する。証明済み・追加仮定付き・未完成・予想・計算観察を区別し、新規性未確認は明示する。
- `python3 scripts/check_sources.py` でTeXの閉包と参照を検査し、可能な環境で `latexmk -lualatex papers/cubic-quantization.tex` と必要な計算を実施する。生成、検証、組版、GitHub反映を混同しない。PDF・SyncTeX等の生成物はGitで追跡しない。
- 正本は `uedakazushi/cubic-quantization` の `main`。必要な通常コミット・fast-forward pushを承諾なしに行う。force push、Actions追加・起動、不要な履歴・旧ZIP保存はしない。他の作業者の変更を保持し、15–30分のまとまりで保存する。Libraryへの二重保存はしない（GitHub push不能時の緊急保存を除く）。既存Library資料を無断削除しない。
- 研究方針・ノート・論文は現行知識を理解して再開できる形へ整理し、価値ある証明・反例・再現入力を削除しない。重要な方針変更は理由と残課題を現行版に簡潔に反映する。
- **研究区切りごとにresearch-hubを更新**する。先に本repoの原稿・方針・ノート・READMEを保存し、それを根拠としてhubの到達点・確実性・障害・次の一手・依存・正本を更新する。他研究・並行編集を保持し、通常コミットでmainへpushする。hub更新失敗時は本repoを保存した上で別個に報告する。
