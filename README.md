# knl

2022년도 1학기 캡스톤 디자인 팀 프로젝트

담당 파트 : 웹 취약점 진단 도구

사용방법 : main.py 실행

- 무차별 대입 공격 점검 : brute_force.py <br>
한계점 : ID, PW 입력 폼을 특정 사이트의 기준으로 확인할 수 있도록 설계해, 다른 사이트의 경우 작동하지 않음

- 웹 서비스 메소드 점검 : scan_method.py <br>
한계점 : OPTIONS 메소드를 사용하지 않는 사이트의 경우 python 내 requests 라이브러리가 지원하는 메소드만 점검 가능

- 사용 포트 점검 : scan_port.py <br>
한계점 : TCP로 연결되는 포트만 점검, (테스트 환경에서) 작동 후 네트워크 통신이 멈춤

- 디렉토리 리스팅(인덱싱) 점검 : directory_listing.py <br>
한계점 : 치트시트를 추가, 점검 시간이 늘어나 추후 개선 예정