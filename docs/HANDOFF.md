# HANDOFF — 다음 세션은 여기서 시작

> 마지막 갱신: 2026-10-17 (5차 세션). 이 문서 하나로 "어디까지 했고, 지금 뭘 해야 하는지"를 5분 안에 파악할 수 있게 유지합니다. 세션이 끝나면 §1·§2를 갱신하고 [PROGRESS_LOG.md](PROGRESS_LOG.md)에 로그를 남기세요.

## 0. 먼저 확인할 것 (중요)

- **저장소 기록이 라이브보다 늦을 수 있습니다.** 10/13(Codex 브랜치 미병합)·10/17(다른 세션 12건 무기록) 두 번 연속 그랬습니다. 작업 전에 반드시 라이브 최신 상태부터 봅니다.
  - WordPress: `GET https://eric.dothome.co.kr/wp-json/wp/v2/posts?per_page=20&orderby=modified&_fields=id,slug,date,modified,title` (사이트 시간대 UTC)
  - Blogger(eric): `https://erichlee.blogspot.com/feeds/posts/summary?alt=json&max-results=15`
  - hadesyi: 리포트 게시판 `bo_table=free`, 방송통신 게시판 `bo_table=qa` 목록의 작성일
  - GitHub: `git fetch --all` 후 main 외 브랜치 확인
- 저장소 기록보다 새로운 글이 있으면 **새로 쓰기 전에 기록부터 맞춥니다.**

## 1. 현재 상태 (한눈에)

- 프로젝트: 해피레포트 세일즈코드(`redfoxkiller`, 수익 40%)로 블로그 운영. 채널: 에릭 자료노트(WP, eric.dothome.co.kr) · 하데스레포트(그누보드, hadesyi) · eric(Blogger, erichlee.blogspot.com) · 카카오레포트(Blogger, 10/14 6건, URL 미기록). 규칙은 [README.md](../README.md), 전략은 [STRATEGY.md](../STRATEGY.md)
- 실적: 캠페인 글 **49건** (8~9월 19 + 10/14 방통대 중간과제물 18 + 10/17 신규 12). 판매·수익 기록은 아직 없음 → [METRICS.md](METRICS.md)
- **10/17 신규 12건(3채널×4주제)**: 독학사 4단계 D-15(WP 145·hadesyi 419·Blogger) / 방통대 출석수업대체과제물(WP 146·hadesyi qa/48·Blogger) / 2027 전기 대학원 학업계획서(WP 151·hadesyi 420·Blogger) / 2027 수시 면접(WP 152·hadesyi 421·Blogger)
- **10월 교정 완료**: B4(post 113 3·4단계 과목 정정), B5(hadesyi 412 접수 후 체크리스트), C4(한림대 글·로드맵: 접수 10/7 마감·서류 발표 11/4·병원 선택 지원), A7(중간과제물 글 4곳 제출 종료 안내). `drafts/`에 적용 대기 초안 없음
- 세일즈 링크: '방송통신'·'레포트'·'논문'·'서식' 문자열은 리다이렉트 스크립트가 EUC-KR로 바꿔 0건이 됨 → 키워드에 넣지 말 것. 검증은 `https://sales.happyreport.co.kr/search/cook_sid.asp?sid=redfoxkiller&key=<UTF-8 인코딩 키워드>` 결과의 "검색결과 N건"으로 확인(브라우저 필요)
- 접근 방식: 사용자가 데스크톱 앱 브라우저 패널에 WP 관리자·Blogger·hadesyi 로그인을 해 둔 상태에서 작업. WP는 관리자 페이지에서 `/wp-admin/admin-ajax.php?action=rest-nonce`로 받은 nonce로 REST 수정, Blogger는 편집기 HTML 보기의 CodeMirror(`document.querySelector('.CodeMirror').CodeMirror`) 값 교체 후 업데이트, 그누보드는 글수정 화면에서 `#wr_content` 값 + SmartEditor `LOAD_CONTENTS_FIELD` 후 작성완료 클릭

## 2. 지금 할 일 (날짜순)

1. **10/23(금) 10:00 수험표 출력 시작** — 독학사 글 5건(WP 113·145, hadesyi 412·419, Blogger D-15) 문구가 맞는지 확인. **11/1 시험 직후**엔 상단에 "시험 종료·11/30 10:00 합격 발표" 안내로 교체(BACKLOG B6)
2. **11/2 중간과제물 성적 공개 ~ 11/6 출석수업대체과제물 제출 시작** — 출석수업대체 글 3건 상단에 제출 기간(11/6 09:00~11/16 18:00, 추가 11/17~11/19 수정 시 1점 감점) 안내, 중간과제물 허브 글에 성적 공개 안내(K2)
3. **11/4 14:00 한림대 서류 발표** — 한림대 성심병원 글에 면접 일정 안내 반영(H1, 지원 병원 홈페이지 공지 확인)
4. **11/19 수능 직후** — 수시 면접 글 3건에 수능 이후 면접 일정 보강(S2)
5. **기록 보완** — 카카오레포트 6건 URL·원문, hadesyi 413~418 원문을 posts_*.html에 보관. 카카오레포트를 README 채널 표에 정식 추가
6. **METRICS 첫 기록** — 세일즈코드 페이지(로그인)에서 판매 내역 확인. BEST-100 재분석으로 11~12월 클러스터(방통대 기말, 대학원·수시 면접 반응) 결정
7. 11월 말: 방통대 2학기 기말시험·기말과제 시행공고 확인 후 신규 글 기획(K3)

## 3. 세션 시작 절차

1. §0의 라이브 대조를 먼저 한다
2. 이 문서 → [ROADMAP.md](ROADMAP.md) → [BACKLOG.md](BACKLOG.md) 순으로 읽는다 (README·STRATEGY는 규칙 확인용)
3. 오늘 날짜를 ROADMAP 하단 "확인한 일정"에 대어 보고, 마감이 가장 가까운 항목부터 한다
4. 글을 발행·수정하면 **같은 세션 안에서** README 게시 이력 표, posts_*.html 원문, BACKLOG 상태, PROGRESS_LOG를 갱신하고 커밋·푸시한다

## 4. 파일 지도

| 파일 | 언제 보나 |
|---|---|
| `docs/HANDOFF.md` | 세션 시작 (이 문서) |
| `docs/ROADMAP.md` | 무엇을 할지 고를 때 (우선순위·완료 기준·확인한 일정) |
| `docs/BACKLOG.md` | 글 후보·키워드·링크·상태 |
| `docs/PUBLISHING_CHECKLIST.md` | 글 쓰고 발행할 때 (규칙·템플릿·SEO 상태표) |
| `docs/REVIEW_2026-10-13.md`, `docs/LINK_AUDIT_2026-10-13.*`, `docs/LIVE_SYNC_2026-10-13.json` | 10/13 라이브 대조 근거 |
| `docs/STATUS.md` | 8/29 분석 |
| `docs/METRICS.md` | 수익·판매 기록 |
| `docs/PROGRESS_LOG.md` | 세션별 로그 (세션 끝에 추가) |
| `drafts/` | 과거 초안·수정안 (현재 적용 대기 없음, 재발행 금지) |
| `README.md` | 수익 구조·채널·게시 이력(정본)·재개 프롬프트 |
| `STRATEGY.md` | 클러스터 분석·운영 팁·검증된 키워드 링크 |
| `posts_*.html` | 발행 원문 (재발행·수정용) |
| `tools/make_sales_links.py` | 키워드 → 인코딩 링크 |

## 5. 지켜야 할 것

- 로그인·자격증명은 사용자가 직접. 저장소에 계정·토큰·nonce 기록 금지
- 모든 글 하단 제휴 고지 문구 유지, 과제물·서류 글은 "그대로 제출 금지" 문구 유지
- 템플릿만 바꾼 복제 글 금지 — 글당 고유 정보 3가지 이상. 3채널 동시 발행 시 관점을 달리할 것(10/17 글들이 그 예)
- 공식 일정은 원 공고로 확인하고 확인일을 적는다. 예년 일정을 확정 일정처럼 쓰지 않는다
- 발행 결과는 반드시 같은 세션에서 저장소에 기록
