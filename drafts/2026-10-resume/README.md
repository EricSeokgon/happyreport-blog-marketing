# 2026-10-13 재개 패키지 — 블로그 반영 대기

공식 일정과 공개된 기존 글을 대조해 만든 수정안입니다. **이번 세션에서 블로그를 발행·수정하지 않았습니다.** 공개 글 보관본은 루트의 `posts_*.html`, 새 수정안은 이 폴더에 있습니다.

| 우선순위 | 파일 | 적용 대상 | 적용 방법 |
|---|---|---|---|
| 1 | [A7_knou_additional_submission_banner.html](A7_knou_additional_submission_banner.html) | WordPress post 26·117, hadesyi qa/47, Blogger 방통대 글 | 기존 본문 맨 위에 블록 1회 삽입. 10/15 18시 이후 종료 안내로 교체 |
| 2 | [B4_wordpress_stage4_corrected.html](B4_wordpress_stage4_corrected.html) | WordPress post 113 | 본문 교체, 제목 교정, URL 유지. 3·4단계 혼동 정정 |
| 2 | [B5_gnuboard_stage4_checklist.html](B5_gnuboard_stage4_checklist.html) | hadesyi free/412 | B4와 함께 본문·제목 교체. 신규 글로 중복 발행하지 않음 |
| 3 | [C4_blogger_hallym_corrected.html](C4_blogger_hallym_corrected.html) | Blogger 한림대 글 | 본문·제목 교체, 기존 URL 유지. 로드맵의 ‘통합 공채’ 문구도 수정 |
| 4 | [B3_blogger_final_review.html](B3_blogger_final_review.html) | Blogger 신규 글 | B4·B5 반영 후 발행. 10/13 기준 날짜 문구를 실제 발행일에 맞춤 |

제휴 링크는 2026-10-13 공개 검색결과 존재를 확인했습니다. 개별 상품의 최신성·정확성·수익 전환은 확인한 것이 아닙니다. 모든 글의 고지 문구를 유지하세요.

반영 전 관리자 화면의 최신 본문을 백업하고 변경점과 비교합니다. WordPress 공개 API의 `content.rendered`는 편집기 `content.raw`와 같지 않으므로 기존 Gutenberg 글 전체를 보관본으로 덮어쓰지 않습니다. A7은 삽입 블록이며 단독 글이 아닙니다.

반영 후에는 실제 페이지를 열어 확인하고, `posts_*.html`·README·BACKLOG·PROGRESS_LOG·HANDOFF를 같은 세션에 갱신합니다. 예약 발행·자동화는 설정하지 않았습니다.
