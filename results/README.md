# results/
サーバーの runs/ から回収した成果物（Git管理外）。サーバー側では runs/ がこれに対応する。
構造: results/<server>/<run_id>/{output,logs,meta}
run_id: YYYYMMDD-HHMM_<tag>_<git short hash>[-dirty]
古いrunは results/<server>/_archive/ へ退避。
