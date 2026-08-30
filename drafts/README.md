# drafts — 발행 전 초안

브라우저·로그인 없이 작성한 초안입니다. 각 파일 상단 주석에 **발행 전 할 일**(링크 검증, [자료 설명] 채우기, 내부 링크 삽입)과 **근거**가 적혀 있습니다. 발행이 끝나면 본문을 `posts_<채널>.html`로 옮기고, 이 폴더의 파일은 삭제하거나 `발행완료_` 접두어를 붙여 둡니다.

> 2026-08-30 채널 변경: 오후의레포트(hadeslee.dothome.co.kr)가 기간 만료로 사라져 워드프레스 채널은 **에릭 자료노트(https://eric.dothome.co.kr, 관리자 /wp-admin/)** 로 바뀌었습니다. 만료로 유실된 3건의 재발행 패키지가 `2026-09-republish/`에 있습니다.

| 파일 | BACKLOG | 채널 | 발행 시점 | 상태 |
|---|---|---|---|---|
| `2026-09-republish/발행완료_R_ericdothome_3posts.html` | R1~R3 | 에릭 자료노트 (카테고리 시험자료) | 2026-08-30 발행 완료 | 라이브: https://eric.dothome.co.kr/sangsudo-gwanmang-gichul-220/ · https://eric.dothome.co.kr/cbco-gichul-210/ · https://eric.dothome.co.kr/dokhaksa-4dangye-jokbo/. 원문은 posts_ericdothome_wordpress.html로 이관 |
| `2026-09-knou/A1_hadesyi_knou_hub.html` | A1 | hadesyi 방송통신 게시판 | 즉시 (목표 9/10) | 초안 — 링크 15개 검증 필요 |
| `2026-09-knou/발행완료_A2_ericdothome_social_welfare_early_childhood.html` | A2 | 에릭 자료노트 (카테고리 방송통신대) | 2026-08-30 발행 완료 | 라이브: https://eric.dothome.co.kr/knou-social-welfare-early-childhood-2026-2/. 세일즈 링크 5개는 미검증 → 클릭 확인 후 필요 시 REST API로 교체 |
| `2026-09-knou/A3_eric_liberal_arts.html` | A3 | eric (블로거) | A2 다음 날 | 초안 — 링크 검증 필요 |
| `2026-09-dokhaksa/B1_ericdothome_patch_after_result.html` | B1 | 에릭 자료노트 독학사 글 https://eric.dothome.co.kr/dokhaksa-4dangye-jokbo/ (post 113) 패치 | 9/7 발표 직후 | 초안 — 일정 검증 완료, REST API로 content 교체 가능 |
| `2026-09-dokhaksa/B2_hadesyi_stage4_checklist.html` | B2 | hadesyi 리포트 게시판 | 9/15 전후 | 초안 — "독학사 4단계" 링크만 검증 (독학사 글 내부 링크는 반영 완료) |
| `2026-09-hospital/C1_eric_hospital_posts_enriched.html` | C1·C2 | eric 기존 글 5건 본문 교체 | 9월 중 하루 1~2건 | 초안 — [검증] 표시 4곳 확인 후 적용 |

## 표기 규칙

- `<!-- [검증] -->` : 발행 전 브라우저로 확인할 링크·사실. 확인 후 주석은 지우고 발행
- `[자료 설명]` : 세일즈 검색결과 상위 자료의 실제 구성(예: "A+ 작성 예시 6페이지")으로 교체. 없는 수치는 만들지 않음
- `[허브 글 URL]`, `[독학사 글 새 URL]`, `[에릭 자료노트 새 URL]` : 먼저 발행된 글의 라이브 URL로 교체(내부 링크)
- 본문은 `<!-- 본문 시작 -->` ~ `<!-- 본문 끝 -->` 사이만 복사. 블로거(eric)용은 한 줄 HTML
