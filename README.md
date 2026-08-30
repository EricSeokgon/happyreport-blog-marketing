# 해피레포트 세일즈코드 블로그 수익화 프로젝트

해피레포트(happyreport.co.kr) 세일즈코드 제휴 프로그램으로 블로그 3곳에서 판매 수익을 올리는 프로젝트의 진행 기록입니다. **다음 세션에서는 이 저장소만 읽으면 이어서 작업할 수 있습니다.**

> **다음 세션은 [docs/HANDOFF.md](docs/HANDOFF.md)부터 읽으세요.** 현재 상태 요약, 지금 바로 할 일, 세션 시작 절차가 있습니다.

## 재개 방법 (다음 세션용 프롬프트)

> 이 저장소의 docs/HANDOFF.md → docs/ROADMAP.md → docs/BACKLOG.md 순으로 읽고 프로젝트 상황을 파악한 뒤, 오늘 날짜 기준으로 마감이 가장 가까운 작업부터 이어서 진행해줘. 글 작성·발행 규칙은 docs/PUBLISHING_CHECKLIST.md를 따르고, 새 글을 발행하면 README 게시 이력 표, posts_*.html 원문, docs/BACKLOG.md 상태, docs/PROGRESS_LOG.md 로그를 같은 세션에서 갱신하고 커밋해줘. 세션이 끝나면 docs/HANDOFF.md의 현재 상태와 할 일도 갱신해줘.

## 문서 지도

| 파일 | 내용 |
|---|---|
| [docs/HANDOFF.md](docs/HANDOFF.md) | 세션 시작 문서: 현재 상태, 지금 할 일, 절차 |
| [docs/ROADMAP.md](docs/ROADMAP.md) | 다음 단계(P1~P6), 완료 기준, 시즌 캘린더 |
| [docs/BACKLOG.md](docs/BACKLOG.md) | 후보 글·키워드·세일즈 링크·상태 |
| [docs/PUBLISHING_CHECKLIST.md](docs/PUBLISHING_CHECKLIST.md) | 작성·발행 체크리스트, 채널별 HTML 템플릿, SEO 상태표 |
| [docs/STATUS.md](docs/STATUS.md) | 2026-08-29 전체 분석: 완료/미완/누락, 리스크 |
| [docs/METRICS.md](docs/METRICS.md) | 판매·수익 기록 (주간) |
| [docs/PROGRESS_LOG.md](docs/PROGRESS_LOG.md) | 세션별 작업 로그 |
| [drafts/](drafts/README.md) | 발행 전 초안 (재발행 3건, 방통대 3건, 독학사 2건, 병원 보강 5건) — 발행 후 posts_*.html로 이관 |
| [STRATEGY.md](STRATEGY.md) | 수익 구조 분석, BEST-100 클러스터, 운영 팁, 검증된 키워드 링크 |
| `posts_*.html` | 채널별 발행 원문 HTML (재발행·수정용) |
| `tools/make_sales_links.py` | 키워드 → 인코딩 세일즈 링크 생성기 |

## 1. 수익 구조 (핵심)

- 세일즈코드 페이지: https://www.happyreport.co.kr/sales/salescode.asp?mode=b1 (로그인 필요)
- 세일즈 ID: `redfoxkiller` / 자료 판매 시 판매수익의 40% 지급 (예: 5,000원 자료 → 2,000원)
- 링크 형식:
  - 기본: `https://sales.happyreport.co.kr/redfoxkiller/`
  - 키워드(주력): `https://sales.happyreport.co.kr/redfoxkiller/키워드/` → 키워드 검색결과로 연결(한글은 URL 인코딩). 검색결과의 어떤 자료를 사도 수익 발생
  - 카테고리: `https://sales.happyreport.co.kr/아이디/검색어/카테고리/`
- 검색은 공백 기준 AND 매칭 (예: "독학사 가족관계" → 두 단어 모두 제목에 포함)
- 링크 생성: `python3 tools/make_sales_links.py "키워드"` (여러 개 가능, `--md`로 목록 출력)
- 참고: erichlee 블로그 기존 글은 올레포트(allreport.co.kr, sid=leesk55)도 병행 사용 중

## 2. 운영 채널 3곳

| 블로그 | 주소 | 플랫폼 | 성격 | 게시 방법 |
|---|---|---|---|---|
| 에릭 자료노트 | https://eric.dothome.co.kr (관리자 https://eric.dothome.co.kr/wp-admin/) | 워드프레스 | 대학 레포트·방송통신대·자소서·실습일지 허브 + 자격증·독학사·시험족보(구 오후의레포트 역할). 올레포트(sid=leesk55)·해피레포트 병행 | wp-admin → 글 → 새로 추가 → 코드 편집기에 HTML 붙여넣기. 글 카테고리: 방송통신대(기존), 시험자료(신설 예정) |
| 하데스레포트 | http://hadesyi.dothome.co.kr | 그누보드 | 리포트·자소서·실습일지·방통대 | 리포트 게시판(bo_table=free) 글쓰기 → 에디터 HTML 탭 붙여넣기 (방통대 글은 방송통신 게시판) |
| eric | https://erichlee.blogspot.com | 블로거(Blogger) | 취업·면접·기출복기 | blogger.com → eric → 새 글 → HTML 보기 붙여넣기 |

> **채널 변경 (2026-08-30)**: 워드프레스 채널이던 오후의레포트(http://hadeslee.dothome.co.kr)는 호스팅 기간 만료로 접근 불가. 그곳에 발행했던 3건은 에릭 자료노트에 재발행한다 (`drafts/2026-09-republish/`). 문서 곳곳의 "hadeslee"는 이 만료 채널을 가리킨다.

- 로그인은 항상 사용자가 직접 (자격증명 저장·대행 입력 금지)
- 모든 글 하단에 제휴 고지 문구 필수: "※ 본 글에는 제휴 링크가 포함되어 있으며, 자료 구매 시 작성자에게 일정 수익이 발생할 수 있습니다."

## 3. 게시 이력 (2026-08-30 기준: 라이브 12건, 만료 3건 재발행 대기)

### 에릭 자료노트 (eric.dothome.co.kr, 워드프레스)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-08-19 | 방송통신대 중간과제물, 참고자료 어디서 찾을까? (2026 최신 가이드) | https://eric.dothome.co.kr/knou-gwajemul/ | 기본 홍보코드(redfoxkiller) + 올레포트 검색(sid=leesk55). 원문 미보관, 이 저장소 세션 밖에서 발행됨 |
| (재발행 대기) | 상수도관망시설운영관리사 1급·2급 필기 기출 220문항 (2026) | [재발행 후 기록] | 상수도관망시설운영관리사 |
| (재발행 대기) | 컴플라이언스 오피서(은행) CBCO 필기 기출 210문항 | [재발행 후 기록] | 컴플라이언스 오피서 |
| (재발행 대기) | 독학사 4단계 대비 전공별 기출 족보 총정리 | [재발행 후 기록] | 독학사+과목명 8종 |

### 구 오후의레포트 (hadeslee, 워드프레스) — 2026-08-30 기간 만료, 접근 불가

| 발행일 | 제목 | 구 URL (만료) | 처리 |
|---|---|---|---|
| 2026-08-17 | 상수도관망시설운영관리사 1급·2급 필기 기출 220문항 (2026) | http://hadeslee.dothome.co.kr/?p=14791 | 에릭 자료노트에 재발행 (R1) |
| 2026-08-17 | 컴플라이언스 오피서(은행) CBCO 필기 기출 210문항 | http://hadeslee.dothome.co.kr/?p=14793 | 에릭 자료노트에 재발행 (R2) |
| 2026-08-17 | 독학사 4단계 대비 전공별 기출 족보 총정리 | http://hadeslee.dothome.co.kr/?p=14795 | 에릭 자료노트에 재발행 (R3, D-day 표 추가본) |

### 하데스레포트 (hadesyi, 그누보드 리포트 게시판)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-08-17 | [시험자료] 보험심사관리사 기출 160문항 (2026) | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=409 | 보험심사관리사 |
| 2026-08-17 | [면접자료] 2026 하반기 공공기관 체험형 인턴 면접 준비법 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=410 | 한국남동발전 체험형 / 주택금융공사 청년인턴 / 국세청 체납관리단 |
| 2026-08-17 | [면접자료] 2026 지방직·군무원 면접 직렬별 총정리 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=411 | 지방직 면접 / 군무원 면접 |

### eric (erichlee.blogspot.com, 블로거)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-08-17 | 2026 하반기 신용보증기금 청년인턴 면접 기출 50선 | https://erichlee.blogspot.com/2026/08/2026-50.html | 신용보증기금 청년인턴 |
| 2026-08-17 | 2026 대한항공 기술훈련생(엔진정비) 면접 총정리 | https://erichlee.blogspot.com/2026/08/2026.html | 대한항공 기술훈련생 |
| 2026-08-17 | 2026 하반기 간호사 채용 병원별 필기·면접 로드맵 | https://erichlee.blogspot.com/2026/08/2026_0922196324.html | 병원명 6종 |
| 2026-08-18 | 2026 하반기 전북대학교병원 간호사 면접 기출·후기 총정리 | https://erichlee.blogspot.com/2026/08/2026_0498363062.html | 전북대학교병원 간호사 |
| 2026-08-18 | 2026 하반기 전남대학교병원 간호사 면접 기출·후기 총정리 | https://erichlee.blogspot.com/2026/08/2026_01589132194.html | 전남대학교병원 간호사 |
| 2026-08-18 | 2026 하반기 한림대 성심병원 간호사 면접 기출·후기 총정리 | https://erichlee.blogspot.com/2026/08/2026_0950180615.html | 한림대 성심병원 |
| 2026-08-19 | 2026 하반기 가천대 길병원 간호사 면접 기출·후기 총정리 | https://erichlee.blogspot.com/2026/08/2026_01404080200.html | 가천대길병원 간호사 |
| 2026-08-19 | 2026 하반기 의정부성모병원 간호사 면접 기출·후기 총정리 | https://erichlee.blogspot.com/2026/08/2026_02066044816.html | 의정부성모병원 간호사 |

> 원문 HTML은 posts_*.html 파일 참조 (재발행·수정 시 복사용). eric 8/18~19 발행분 5건은 2026-08-29에 라이브 게시글에서 복원한 것. 구 오후의레포트 3건 원문은 `posts_ericdothome_wordpress.html`에 보관.

## 4. 다음 작업 (요약 — 상세는 [docs/ROADMAP.md](docs/ROADMAP.md))

- **P0 (즉시)**: 만료된 오후의레포트 글 3건을 에릭 자료노트에 재발행 (`drafts/2026-09-republish/`, 링크 검증 불필요) → 새 URL을 게시 이력에 기록
- **P1 (지금~9/10)**: 방통대 2학기 중간과제물 시즌(제출 10/2~10/12) — 키워드 검증 → BEST-100 재분석 → `drafts/2026-09-knou/` 초안 3건 발행 (hadesyi 방송통신 게시판·에릭 자료노트·eric). 후보·링크는 [docs/BACKLOG.md](docs/BACKLOG.md) A
- **P2 (9/7 → 9/22~29 → 11/1)**: 독학사 3단계 발표 직후 에릭 자료노트 재발행 독학사 글 패치(`drafts/2026-09-dokhaksa/B1`), 4단계 접수 D-7 신규 글(`B2`), 시험 D-15 리마인드
- **P3 (9월 중)**: 병원 간호사 글 5건 본문 교체(`drafts/2026-09-hospital/C1`, 복제 템플릿 탈피 + 내부 링크), 서치콘솔·서치어드바이저 등록 상태 확인
- **P4 (매주)**: 세일즈코드 수익 내역을 [docs/METRICS.md](docs/METRICS.md)에 기록 → 4주 후 전환되는 클러스터 판단
- **P5 (10~11월)**: CBCO·보험심사관리사 등 시험 직전 보강, BEST-100 신규 자격증 발굴
- **P6 (장기)**: 매 세션 BEST-100 재분석, 2027년 1월 제목 연도 갱신 재발행, 분기 1회 링크 전수 점검

## 5. 작업 로그

세션별 로그는 [docs/PROGRESS_LOG.md](docs/PROGRESS_LOG.md)에 있습니다. 최근 항목:

- **2026-08-30 (3차, 3부)**: 오후의레포트(hadeslee) 호스팅 만료 확인 → 워드프레스 채널을 에릭 자료노트(eric.dothome.co.kr)로 교체, 유실 3건 재발행 패키지(`drafts/2026-09-republish/`) 작성, 문서·초안 전체 채널 교체. 발행 없음
- **2026-08-29 (3차)**: 저장소 전체 분석·기록 체계 정비(docs/ 신설), 누락된 원문 HTML 5건 복원, 링크 생성기 추가. 방통대 2학기 일정 확정(제출 10/2~10/12) 후 `drafts/`에 방통대 글 3건·독학사 2건·병원 보강 5건 초안 작성. 발행 없음
- **2026-08-18~19 (2차)**: eric에 병원 간호사 면접 글 5건 발행
- **2026-08-17 (1차)**: 세일즈코드 분석, 클러스터 4개 도출, 9건 발행
