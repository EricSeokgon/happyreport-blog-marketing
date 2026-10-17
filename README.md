# 해피레포트 세일즈코드 블로그 수익화 프로젝트

해피레포트(happyreport.co.kr) 세일즈코드 제휴 프로그램으로 블로그 3곳에서 판매 수익을 올리는 프로젝트의 진행 기록입니다. **다음 세션에서는 이 저장소의 기록과 공개 블로그 상태를 대조한 뒤 이어서 작업합니다.**

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
| [drafts/](drafts/README.md) | 10월 수정안 5개 + 발행 확인된 과거 초안. 상태 구분 후 사용 |
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
| 에릭 자료노트 | https://eric.dothome.co.kr (관리자 https://eric.dothome.co.kr/wp-admin/) | 워드프레스 (REST API 사용 가능: /wp-json/wp/v2/) | 대학 레포트·방송통신대·자소서·실습일지 허브 + 자격증·독학사·시험족보(구 오후의레포트 역할). 올레포트(sid=leesk55)·해피레포트 병행 | wp-admin → 글 → 새로 추가 → 코드 편집기에 HTML 붙여넣기. 카테고리(id): 방송통신대(3), 시험자료(47, 8/30 신설 — 자격증·독학사 글), 실습·자격증(17), 공부 팁(31), 레포트 작성법(10), 자기소개서(24). 태그: 기출문제(36) 족보(37) 시험공부(35) 자격증(48) 독학사(49). REST API 발행 시 본문은 `<!-- wp:html -->` 블록으로 |
| 하데스레포트 | http://hadesyi.dothome.co.kr | 그누보드 | 리포트·자소서·실습일지·방통대 | 리포트 게시판(bo_table=free) 글쓰기 → 에디터 HTML 탭 붙여넣기 (방통대 글은 방송통신 게시판) |
| eric | https://erichlee.blogspot.com | 블로거(Blogger) | 취업·면접·기출복기 | blogger.com → eric → 새 글 → HTML 보기 붙여넣기 |

> **채널 변경 (2026-08-30)**: 워드프레스 채널이던 오후의레포트(http://hadeslee.dothome.co.kr)는 호스팅 기간 만료로 접근 불가. 그곳에 발행했던 3건은 에릭 자료노트에 재발행한다 (`drafts/2026-09-republish/`). 문서 곳곳의 "hadeslee"는 이 만료 채널을 가리킨다.

- 로그인은 항상 사용자가 직접 (자격증명 저장·대행 입력 금지)
- 모든 글 하단에 제휴 고지 문구 필수: "※ 본 글에는 제휴 링크가 포함되어 있으며, 자료 구매 시 작성자에게 일정 수익이 발생할 수 있습니다."

## 3. 게시 이력 (2026-10-13 기록 복구: 캠페인 19건 + 에릭 자료노트 기본 글 4건)

기존 16건에 누락된 9월 발행 3건을 추가했습니다. 이번 세션의 신규 발행은 0건이며, 19개 URL의 현재 가용성을 전수 검증한 수치는 아닙니다. [재개 분석](docs/REVIEW_2026-10-13.md)과 [10월 수정안](drafts/2026-10-resume/README.md)을 먼저 확인하세요.

### 에릭 자료노트 (eric.dothome.co.kr, 워드프레스)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-10-14 | [방통대] 2026 2학기 방송통신대 중간과제물, 학과별 자료로 빠르게 끝내는 법 | https://eric.dothome.co.kr/?p=131 | 학과별 중간과제물 6링크(검증 착지) |
| 2026-10-14 | 방송통신대 사회복지학과 중간과제물 과목별 접근법 | https://eric.dothome.co.kr/?p=132 | 사회복지 중간과제물(815) |
| 2026-10-14 | 방송통신대 유아교육과 중간과제물, 관찰기록·활동계획안 | https://eric.dothome.co.kr/?p=133 | 유아교육과 중간과제물(427) |
| 2026-10-14 | 방송통신대 간호학과(RN-BSN) 중간과제물 | https://eric.dothome.co.kr/?p=134 | 간호학과 중간과제물(368) |
| 2026-10-14 | 방송통신대 교육학과 중간과제물, 이론 비교·이슈 분석 | https://eric.dothome.co.kr/?p=135 | 교육학과 중간과제물(256) |
| 2026-10-14 | 방송통신대 경영학과 중간과제물, 기업 사례로 이론 적용 | https://eric.dothome.co.kr/?p=136 | 경영학과 중간과제물(59) |
| 2026-08-19 | 방송통신대 중간과제물, 참고자료 어디서 찾을까? (2026 최신 가이드) | https://eric.dothome.co.kr/knou-gwajemul/ | 기본 홍보코드(redfoxkiller) + 올레포트 검색(sid=leesk55). 2026-10-13 공개 REST rendered 본문 복구. A1·A3·과목 링크 보강 확인. **8/30 보강(A6)**: 2학기 확정 일정 섹션 + '함께 보면 좋은 글' 추가 |
| 2026-08-30 | 방통대 사회복지학과·유아교육과 2학기 중간과제물 준비 — 과목별 참고자료와 작성 포인트 (2026) | https://eric.dothome.co.kr/knou-social-welfare-early-childhood-2026-2/ | 사회복지실천론·조사론·정책론 과제물 / 아동관찰및행동연구 과제물 / 유아교육 과제물 (5개, **2026-10-13 검색결과 존재 확인**; 학과·학기 적합성은 개별 확인) |
| 2026-08-17 | 대학 레포트 A+ 받는 5가지 원칙 (+ 참고자료 찾는 곳) | https://eric.dothome.co.kr/report-aplus/ | (저장소 밖 발행, 사이트 기본 글. 카테고리 레포트 작성법) |
| 2026-08-14 | 간호·사회복지 실습일지 작성 예시와 참고자료 활용법 | https://eric.dothome.co.kr/siljib-ilji/ | (저장소 밖 발행. 카테고리 실습·자격증) |
| 2026-08-11 | 막막한 자기소개서, 합격 예시로 시작하는 법 | https://eric.dothome.co.kr/jaso-yeje/ | (저장소 밖 발행. 카테고리 자기소개서) |
| 2026-08-08 | 기출·족보로 벼락치기 효율 200% 올리는 법 | https://eric.dothome.co.kr/siheom-jokbo/ | (저장소 밖 발행. 자격증 재발행 글의 내부 링크 대상) |
| 2026-08-30 | 상수도관망시설운영관리사 1급·2급 필기, 기출 220문항 족보로 준비하는 법 (2026) | https://eric.dothome.co.kr/sangsudo-gwanmang-gichul-220/ | 상수도관망시설운영관리사 (재발행, 카테고리 시험자료) |
| 2026-08-30 | 컴플라이언스 오피서(은행) CBCO 필기, 기출 210문항으로 합격하는 법 | https://eric.dothome.co.kr/cbco-gichul-210/ | 컴플라이언스 오피서 (재발행) |
| 2026-08-30 | 독학사 4단계 학위취득 종합시험 대비 - 전공별 기출 족보 총정리 | https://eric.dothome.co.kr/dokhaksa-4dangye-jokbo/ | 독학사+과목명 8종 + 전공 3종 (재발행, D-day 일정표 추가) |

### 구 오후의레포트 (hadeslee, 워드프레스) — 2026-08-30 기간 만료, 접근 불가

| 발행일 | 제목 | 구 URL (만료) | 처리 |
|---|---|---|---|
| 2026-08-17 | 상수도관망시설운영관리사 1급·2급 필기 기출 220문항 (2026) | http://hadeslee.dothome.co.kr/?p=14791 | 2026-08-30 재발행 완료 → https://eric.dothome.co.kr/sangsudo-gwanmang-gichul-220/ |
| 2026-08-17 | 컴플라이언스 오피서(은행) CBCO 필기 기출 210문항 | http://hadeslee.dothome.co.kr/?p=14793 | 2026-08-30 재발행 완료 → https://eric.dothome.co.kr/cbco-gichul-210/ |
| 2026-08-17 | 독학사 4단계 대비 전공별 기출 족보 총정리 | http://hadeslee.dothome.co.kr/?p=14795 | 2026-08-30 재발행 완료 → https://eric.dothome.co.kr/dokhaksa-4dangye-jokbo/ |

### 하데스레포트 (hadesyi, 그누보드 리포트 게시판)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-10-14 | [방통대] 2026 2학기 방송통신대 중간과제물, 학과별 자료로 빠르게 끝내는 법 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=413 | 학과별 중간과제물 6링크 |
| 2026-10-14 | [방통대] 사회복지학과 중간과제물, 과목별 접근법 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=414 | 사회복지 중간과제물 |
| 2026-10-14 | [방통대] 유아교육과 중간과제물, 관찰기록·활동계획안 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=415 | 유아교육과 중간과제물 |
| 2026-10-14 | [방통대] 간호학과(RN-BSN) 중간과제물 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=416 | 간호학과 중간과제물 |
| 2026-10-14 | [방통대] 교육학과 중간과제물, 이론 비교·이슈 분석 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=417 | 교육학과 중간과제물 |
| 2026-10-14 | [방통대] 경영학과 중간과제물, 기업 사례로 이론 적용 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=418 | 경영학과 중간과제물 |
| 2026-08-17 | [시험자료] 보험심사관리사 기출 160문항 (2026) | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=409 | 보험심사관리사 |
| 2026-08-17 | [면접자료] 2026 하반기 공공기관 체험형 인턴 면접 준비법 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=410 | 한국남동발전 체험형 / 주택금융공사 청년인턴 / 국세청 체납관리단 |
| 2026-08-17 | [면접자료] 2026 지방직·군무원 면접 직렬별 총정리 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=411 | 지방직 면접 / 군무원 면접 |
| 2026-09-02 | [방통대] 2026학년도 2학기 중간과제물 일정·작성 순서·과목별 참고자료 모음 | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=qa&wr_id=47 | A1, 방송통신 게시판. 10/13 발행 이력 복구 |
| 2026-09-06 | [시험자료] 독학사 4단계 접수·시험 대비 체크리스트 — 전공별 기출 문제집·모의고사로 8주 완성 (2026) | http://hadesyi.dothome.co.kr/bbs/board.php?bo_table=free&wr_id=412 | B2, 10/13 이력 복구. 10월 교정안 B5 반영 대기 |

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
| 2026-09-02 | 2026 2학기 방통대 교양과목 중간과제물 작성법 — 인간과 사회·경제학의 이해·열린사회와 21세기 (제출 10/2~10/12) | https://erichlee.blogspot.com/2026/09/2026-2-21-1021012.html | A3, 교양 5개 링크. 10/13 발행 이력 복구 |

> `posts_*.html`은 발행 본문 보관본입니다. 2026-10-13 공개 본문 14건을 복구했으며, WordPress rendered HTML은 관리자 raw 원본과 다를 수 있습니다. 복구는 사실 교정 완료를 뜻하지 않습니다. 새 수정안은 `drafts/2026-10-resume/`에 있습니다.

### 카카오레포트 (카카오레포트 Blogger, blogID 5194575870278207119)

| 발행일 | 제목 | URL | 세일즈 키워드 |
|---|---|---|---|
| 2026-10-14 | 2026 2학기 방송통신대 중간과제물, 학과별 자료로 빠르게 끝내는 법 | (카카오레포트 블로그) | 학과별 중간과제물 6링크 |
| 2026-10-14 | 방송통신대 사회복지학과 중간과제물 과목별 접근법 | (카카오레포트 블로그) | 사회복지 중간과제물 |
| 2026-10-14 | 방송통신대 유아교육과 중간과제물 | (카카오레포트 블로그) | 유아교육과 중간과제물 |
| 2026-10-14 | 방송통신대 간호학과(RN-BSN) 중간과제물 | (카카오레포트 블로그) | 간호학과 중간과제물 |
| 2026-10-14 | 방송통신대 교육학과 중간과제물 | (카카오레포트 블로그) | 교육학과 중간과제물 |
| 2026-10-14 | 방송통신대 경영학과 중간과제물 | (카카오레포트 블로그) | 경영학과 중간과제물 |

## 4. 다음 작업 (2026-10-13 기준)

1. 방통대 추가 제출(10/15 18시 마감) 안내 A7을 기존 글 4곳에 삽입.
2. 독학사 post 113·hadesyi free/412에 B4·B5 교정안 적용: 접수 종료 안내, 3·4단계 과목 혼동 정정.
3. 한림대 채용 안내 C4 적용: 실제 접수는 10/7 종료, 병원 선택 지원이며 통합채용 아님.
4. 기존 글 교정 후 B3 시험 직전 점검 글 발행. 날짜는 실제 발행일에 맞춤.
5. BEST-100·실제 판매수익·SEO 관리 상태 확인. 미확인 값을 0으로 채우지 않음.

[수정안 5개](drafts/2026-10-resume/README.md) · [공식 출처·분석](docs/REVIEW_2026-10-13.md) · [키워드 점검 19개](docs/LINK_AUDIT_2026-10-13.md). 이번 세션에서 블로그 관리자 변경은 실행하지 않았습니다.

## 5. 작업 로그

세션별 로그는 [docs/PROGRESS_LOG.md](docs/PROGRESS_LOG.md)에 있습니다. 최근 항목:

- **2026-10-13**: 9월 발행 3건·수정 내역 누락 복구, 공개 본문 14건 보관, 키워드 19개 검색결과 확인. 10월 수정안 5개 작성. 블로그 변경 없음.
- **2026-08-30 (3차, 5부)**: 에릭 자료노트에 방통대 A2 글 발행(https://eric.dothome.co.kr/knou-social-welfare-early-childhood-2026-2/) + 8/19 가이드 글에 확정 일정 섹션·관련 글 링크 추가(A6). 세일즈 링크 5개는 검색결과 미검증(사용자 클릭 확인 대기)
- **2026-08-30 (3차, 4부)**: 에릭 자료노트에 REST API로 만료분 3건 재발행 완료 (상수도관망·CBCO·독학사, 카테고리 시험자료 신설, 상호 링크 + 8/8 기출·족보 글 링크). 라이브 확인 완료
- **2026-08-30 (3차, 3부)**: 오후의레포트(hadeslee) 호스팅 만료 확인 → 워드프레스 채널을 에릭 자료노트(eric.dothome.co.kr)로 교체, 유실 3건 재발행 패키지 작성, 문서·초안 전체 채널 교체
- **2026-08-29 (3차)**: 저장소 전체 분석·기록 체계 정비(docs/ 신설), 누락된 원문 HTML 5건 복원, 링크 생성기 추가. 방통대 2학기 일정 확정(제출 10/2~10/12) 후 `drafts/`에 방통대 글 3건·독학사 2건·병원 보강 5건 초안 작성. 발행 없음
- **2026-08-18~19 (2차)**: eric에 병원 간호사 면접 글 5건 발행
- **2026-08-17 (1차)**: 세일즈코드 분석, 클러스터 4개 도출, 9건 발행
