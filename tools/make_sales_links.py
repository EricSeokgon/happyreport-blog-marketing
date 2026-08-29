#!/usr/bin/env python3
"""해피레포트 세일즈코드 키워드 링크 생성기.

사용법:
    python3 tools/make_sales_links.py "방송통신대 중간과제물" "독학사 가족관계"
    python3 tools/make_sales_links.py -f docs/keywords.txt      # 한 줄에 키워드 하나
    python3 tools/make_sales_links.py --md "지방직 면접"          # 마크다운 목록으로 출력

규칙 (README.md §1 참고):
  - 키워드 링크: https://sales.happyreport.co.kr/redfoxkiller/<키워드>/
  - 한글·공백은 URL 인코딩 (공백 = %20). 검색은 공백 기준 AND 매칭.
  - 세일즈 ID는 --sid 로 바꿀 수 있음 (기본 redfoxkiller).
표준 라이브러리만 사용하므로 별도 설치 없이 실행됩니다.
"""
import argparse
import sys
from urllib.parse import quote

BASE = "https://sales.happyreport.co.kr"


def make_link(keyword: str, sid: str = "redfoxkiller") -> str:
    kw = " ".join(keyword.split())  # 연속 공백 정리
    return f"{BASE}/{sid}/{quote(kw, safe='')}/"


def main() -> int:
    ap = argparse.ArgumentParser(description="세일즈코드 키워드 링크 생성")
    ap.add_argument("keywords", nargs="*", help="키워드 (따옴표로 묶어 공백 포함 가능)")
    ap.add_argument("-f", "--file", help="키워드 목록 파일 (한 줄에 하나, # 주석 가능)")
    ap.add_argument("--sid", default="redfoxkiller", help="세일즈 ID (기본 redfoxkiller)")
    ap.add_argument("--md", action="store_true", help="마크다운 '- 키워드: 링크' 형식으로 출력")
    ap.add_argument("--html", action="store_true", help="<a> 태그 형식으로 출력")
    args = ap.parse_args()

    keywords = list(args.keywords)
    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#"):
                    keywords.append(line)
    if not keywords:
        ap.print_help()
        return 1

    for kw in keywords:
        link = make_link(kw, args.sid)
        if args.md:
            print(f"- {kw}: {link}")
        elif args.html:
            print(f'<a href="{link}" target="_blank" rel="noopener">{kw} 자료 모아보기</a>')
        else:
            print(f"{kw}\t{link}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
