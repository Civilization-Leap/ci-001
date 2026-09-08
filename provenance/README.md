# Public verification subset / 公开核验子包

This is a deliberately scoped derivative of the V1.4 complete verification
archive. It is **not that complete archive**. Its own manifest lists every included
source and every upstream omission. Do not run the upstream SHA256SUMS against
this subset and interpret missing publication drafts as accidental omissions.

Included originals: S1 Renxin V1.3, S2 Meaning Symbiosis historical v1.1 terminology
alignment, S3 the historical V1.1 long-text candidate. Their exact bytes and
SHA-256 values are retained. See SOURCE_RIGHTS.md; these books are excluded from
the CI-001 CC BY grant.

Excluded: current M1 master, L1 long-text V1.2 candidate, S4/S5 production branches.
Their hashes and original status remain in the upstream manifest. A hash alone
does not let a reader verify a file they do not possess. CI-001's Appendix C still
describes the full original audit package; this public subset does not imply
that all those files are now available here. Current M1 citations can be compared
with shared S2 passages, but this does not independently verify all M1 bytes.

Preserved unchanged: upstream-v1.4/manifest.json and upstream-v1.4/SHA256SUMS.txt.
They describe the historical full audit delivery. The original archive remains
a separate author-held artifact; it is not nested inside this public repository.

To verify the actual repository, run from its root: `sha256sum -c SHA256SUMS`.
The checksum list covers files, excluding itself and .git. It verifies byte
consistency, not truth, authorship, independent review or absence of harm.
Git object IDs use their own object format and are not interchangeable with
the raw-file SHA-256 values recorded here.

中文：这一子包保留三份历史原件及原上游清单；当前母本、长文修订稿与制作分支不
公开。已列明的排除项目不能被误读成“生成了却漏装”。上游记录与公开子包分别
核验，不能用“供核验”推定原件尚未公开，也不能用哈希代替对原文件的读取。
