# HANDOFF — 다음 세션은 여기서 시작

> 마지막 갱신: 2026-08-29 (3차 세션). 이 문서 하나로 "어디까지 했고, 지금 뭘 해야 하는지"를 5분 안에 파악할 수 있게 유지합니다. 세션이 끝나면 이 문서의 §1·§2를 갱신하고 [PROGRESS_LOG.md](PROGRESS_LOG.md)에 로그를 남기세요.

## 1. 현재 상태 (한눈에)

- 프로젝트: 해피레포트 세일즈코드(`redfoxkiller`, 수익 40%)로 블로그 3곳에서 자료 판매 수익화. 구조·규칙은 [README.md](../README.md), 전략·키워드 링크는 [STRATEGY.md](../STRATEGY.md)
- 실적: 8/17~19에 **14건 발행** (hadeslee 3 · hadesyi 3 · eric 8), 이후 신규 발행 없음. 매출 데이터는 아직 기록 없음 → [METRICS.md](METRICS.md)
- 3차 세션(8/29): 발행 없이 **기록 체계 정비 + 초안 작성** — 상태 분석([STATUS.md](STATUS.md)), 로드맵([ROADMAP.md](ROADMAP.md)), 백로그([BACKLOG.md](BACKLOG.md)), 체크리스트([PUBLISHING_CHECKLIST.md](PUBLISHING_CHECKLIST.md)), 누락됐던 원문 HTML 5건 복원, 링크 생성기(`tools/make_sales_links.py`), 그리고 **`drafts/`에 초안 6파일**(방통대 글 3건, 독학사 패치 1·신규 글 1, 병원 글 보강 5건)
- 시즌 위치: **방통대 2학기 중간과제물 이미 공개(8/24), 제출 10/2~10/12. 독학사 3단계 발표 9/7.** 방통대 글은 9/10까지 라이브가 목표

## 2. 지금 바로 할 일 (우선순위 순)

1. **방통대 키워드 검증** — [BACKLOG.md](BACKLOG.md) A-2 1순위 링크 15개를 브라우저로 열어 검색결과 건수 기록, 0건은 2순위 표기로 교체하고 초안의 링크도 함께 교체. (브라우저 필요, 로그인 불필요)
2. **BEST-100 재분석** — salescode.asp?mode=b1 최근다운 BEST-100에서 방통대·과목명 반복 키워드 추출 → BACKLOG A와 초안 과목 목록에 반영. (로그인은 사용자가 직접)
3. **방통대 글 3건 발행** — `drafts/2026-09-knou/` A1(hadesyi 방송통신 게시판) → A2(hadeslee) → A3(eric) 순으로 하루 1건. 각 파일 상단 "발행 전 할 일" 수행([자료 설명] 채우기, 허브 글 내부 링크). 목표 9/10
4. **9/7 이후**: `drafts/2026-09-dokhaksa/B1` 패치를 hadeslee 독학사 글(?p=14795)에 적용, 9/15 전후 `B2` 신규 글 발행
5. **METRICS 첫 기록** — 세일즈코드 페이지 수익 내역을 [METRICS.md](METRICS.md) 주간 표에 옮겨 적기
6. 발행 사이사이: `drafts/2026-09-hospital/C1`로 병원 간호사 글 5건 본문 교체([검증] 4곳 확인), SEO 등록 상태 확인(체크리스트 §5)

## 3. 세션 시작 절차

1. 이 문서 → [ROADMAP.md](ROADMAP.md) → [BACKLOG.md](BACKLOG.md) 순으로 읽는다 (README·STRATEGY는 규칙 확인용)
2. 오늘 날짜를 시즌 캘린더(ROADMAP 하단)에 대어 보고, 마감이 가장 가까운 항목부터 한다
3. 브라우저·로그인이 필요한 작업인지 먼저 구분한다 (ROADMAP 맨 아래 "세션 환경별 가능 작업")
4. 글을 발행하면 **같은 세션 안에서** README 게시 이력 표, posts_*.html 원문, BACKLOG 상태, PROGRESS_LOG를 갱신하고 커밋한다 (2차 세션처럼 원문이 빠지는 일이 없도록)

## 4. 파일 지도

| 파일 | 언제 보나 |
|---|---|
| `docs/HANDOFF.md` | 세션 시작 (이 문서) |
| `docs/ROADMAP.md` | 무엇을 할지 고를 때 (우선순위·완료 기준·시즌 캘린더) |
| `docs/BACKLOG.md` | 글 후보·키워드·링크·상태 |
| `docs/PUBLISHING_CHECKLIST.md` | 글 쓰고 발행할 때 (규칙·템플릿·SEO 상태표) |
| `docs/STATUS.md` | 현재 상태의 근거·발견된 문제 (3차 세션 분석) |
| `docs/METRICS.md` | 수익·판매 기록 |
| `docs/PROGRESS_LOG.md` | 세션별 로그 (세션 끝에 추가) |
| `drafts/` | 발행 전 초안 (상태표는 `drafts/README.md`). 발행 후 posts_*.html로 이관 |
| `README.md` | 수익 구조·채널·게시 이력(정본)·재개 프롬프트 |
| `STRATEGY.md` | 클러스터 분석·운영 팁·검증된 키워드 링크 24개 |
| `posts_*.html` | 발행 원문 (재발행·수정용) |
| `tools/make_sales_links.py` | 키워드 → 인코딩 링크 |

## 5. 지켜야 할 것

- 로그인·자격증명은 사용자가 직접. 저장소에 계정·토큰 기록 금지
- 모든 글 하단 제휴 고지 문구 유지
- 템플릿만 바꾼 복제 글 금지 — 글당 고유 정보 3가지 이상
- 발행 결과는 반드시 같은 세션에서 저장소에 기록
