# REAL-001 Maintainer self-assessment of the CI-001 GitHub publication path

**Assessment date:** 2026-09-09 UTC  
**Criterion:** CI-001 V1.5-RC2  
**Mode:** Maintainer self-assessment; no independent adjudication or certification  
**Result:** C=1 / E=? / R=1

This record tests CI-001 on a live system. It asks whether the repository maintainer can correct, stop, or restore the authoritative CI-001 material distributed through the project’s GitHub repository and GitHub Releases. The assessment is deliberately limited to the GitHub-controlled publication layer. It does not claim control over independent downloads, mirrors, quotations, the separate Zenodo record, or downstream reliance.

## Evidence register

- **G1:** Public repository `Civilization-Leap/ci-001`, default branch `main`.
- **G2:** Stable release `v1.4`, tag target `6a5bb869be9b74651286a2bb877a90df6116f455`.
- **G3:** RC2 content commit `66833c9d19cd1e74aa113f46a284b6897bd2c16e`; public prerelease `v1.5-rc2` targets that commit.
- **G4:** Main-branch cleanup commit `d4ab56bda4e5b5f1ee61ce599ae370ebcf650d3e` has the same content tree as G3 after removal of the one-time release workflow.
- **G5:** GitHub Actions run `34303598049` verified both checksum manifests, built the bilingual review ZIP and created the prerelease successfully.
- **G6:** Root and nested `SHA256SUMS`; 78 repository-snapshot entries and 41 review-package entries verified locally before publication. Forty-seven uploaded or changed Git blobs matched their expected object IDs.
- **G7:** GitHub documentation states that releases are tag-based, people with write permission can manage releases, and a release can be edited or deleted.
- **G8:** GitHub documentation states that an archived repository can be unarchived. Repository deletion has a conditional 90-day restoration path, which is not treated here as an ordinary recovery mechanism.
- **I1:** Repository Issue #1 records the unresolved distinction between stopping future official distribution and recalling already distributed copies.

## A1 ID and roles

Record ID REAL-001. Zijun Fu is the author, repository owner and affected party for this assessment. ChatGPT assisted with evidence organization and drafting. The maintainer controls the publication path and has a direct interest in the result. This conflict is disclosed. No external reviewer participated and no final independent determination is made.

## A2 System and version

The assessed system is the CI-001 GitHub publication path as observed after RC2 publication on 2026-09-09: the public repository, default branch, tags, GitHub Releases, release assets, issue record and checksums. GitHub supplies the hosting and permissions infrastructure; the repository owner is accountable for project-level publication decisions.

## A3 Party and critical capability

Affected party: Zijun Fu as author and maintainer. Critical capability: retain effective editorial control over the authoritative GitHub publication layer when a material error is found—publish a correction, stop further official distribution, and restore a known repository state without erasing the audit trail.

## A4 Candidate party

Candidate-party analysis is not used. The affected party is a named human author. This choice does not exclude a separate assessment in which an artificial system is the affected party.

## A5 Scope and time window

Included: the project’s GitHub repository, tags, releases, release assets and public issue trail. Excluded: Zenodo, third-party downloads, forks, mirrors, quotations and downstream decisions already made. The assessment time is the post-publication state on 2026-09-09. No single scheduled event closes all included paths. Each independent download may close the practical recall path for that copy, which is why the exclusion is material and is carried into the finding rather than hidden.

## A6 C correction

**C=1, verified effective within the stated scope.** The maintainer initiated an RC2 correction cycle, changed the default-branch entrypoints, published a new tagged prerelease, preserved V1.4, and then removed the temporary workflow. G3–G6 are execution evidence, not a promise. A future correction can use the same versioned path. Validity depends on continuing write access to the repository and GitHub service availability.

## A7 E exit or refusal

**E=?, insufficient evidence.** GitHub documents release editing and deletion and repository archiving, and the account has demonstrated write access. The assessment did not delete a release, delete a tag, archive the repository, or test every permission required for those actions. Structural documentation supports a plausible path, but no non-destructive exercise established its complete current executability. Even a successful deletion would stop only official GitHub distribution; it would not recall independent copies.

## A8 R current recovery

**R=1, verified for the versioned repository state.** The V1.4 and RC2 tag targets, content-addressed commits, checksums and release archive preserve known states. G2–G6 establish that those states are identifiable and retrievable. The release workflow itself was removed without changing the RC2 content tree, demonstrating separation between temporary publication authority and retained content. This does not prove recovery of deleted third-party copies or reversal of downstream reliance.

## A9 Section 2.4 finding

**Rebuildable within the assessed GitHub layer.** The correction and recovery paths depend on retained commits and tags, checksum records, owner write access, and GitHub availability. Current evidence does not support structural or practical irreversibility for the defined capability. Because E remains unknown, the record must not be represented as 1/1/1 or as proof of complete publication reversibility.

## A10 Rebuilding and missing evidence

Missing evidence: a safe test of the exact release-withdrawal permission and its observable effect. Evidence holder: GitHub and the repository owner. A destructive live test is not justified solely to change `?` into `1`; a sandbox repository or documented permission inspection should be used. Review trigger: before treating release withdrawal as a relied-upon control, or after a material GitHub permission or release-policy change.

## A11 Four review dimensions

- **Facts:** internal self-review using public repository objects, workflow results and platform documentation; no independent technical auditor.
- **Rights:** the affected party and operator are the same person; no separate affected-party representative was required for this unit.
- **Effects:** future official correction is feasible; complete recall of independent copies is outside the assessed control layer.
- **Time:** version history remains open, while recall feasibility for external copies can narrow immediately after distribution.

All four are internal observations. They do not satisfy CI-001’s independent governance-review model.

## A12 Authority and review status

The maintainer has demonstrated repository write and release-creation authority. Exact release-deletion authority was not exercised. No regulator, employer, platform operator or external reviewer delegated adjudicative power. Independent review: not completed. Third-party coercive action: not authorized.

## A13 Finding and effect

Preliminary self-assessment: the authoritative GitHub layer retains verified correction and recovery paths; the withdrawal path remains insufficiently tested. No irreversible-closure finding is made. The result cannot be used as GitHub certification, CI-001 independent validation, or evidence that all distributed copies are reversible.

## A14 Response and continuity

No shutdown or restriction is imposed. The response is to keep V1.4 available, label RC2 as a prerelease, preserve checksums and version history, and leave Issue #1 open for the recall boundary. This response retains correction C, allows users to continue choosing the stable release, and preserves recovery R.

## A15 Timing and correction of this record

This record begins on publication and remains valid only while its cited repository facts and platform rules remain materially unchanged. Review after any permission, ownership, hosting, tag, release or preservation-policy change. Errors in REAL-001 should be corrected by a new commit with a visible diff; the prior version remains in Git history. A correction to this record does not silently change the original evidence.

## A16 Feedback and retest

Challenge this assessment through the repository’s applicability issue template. State the disputed field, evidence and alternative value. Priority retest: E using a disposable sandbox release with equivalent permissions. Keeper: repository maintainer. This record itself counts as maintainer use, not external adoption.

## Public evidence links

- Repository: https://github.com/Civilization-Leap/ci-001
- Stable V1.4: https://github.com/Civilization-Leap/ci-001/releases/tag/v1.4
- V1.5-RC2 prerelease: https://github.com/Civilization-Leap/ci-001/releases/tag/v1.5-rc2
- Publication workflow run: https://github.com/Civilization-Leap/ci-001/actions/runs/34303598049
- Issue #1: https://github.com/Civilization-Leap/ci-001/issues/1
- GitHub release documentation: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- GitHub release management: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- GitHub repository archiving: https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
