# TradeDatetime
한국거래소 기준 Datetime Functions 패키지



## 사용법

패키지 설치 후 최초 1회 다음을 파이썬 인터프리터 또는 쥬피터에서 실행해야 합니다.

!주의 : 데이터 수집에 시간이 꽤 걸리니 자주 실행하면 안됩니다.

    import trddt
    trddt.build_HolidaysText()

그러면 trddt 패키지가 설치된 경로에 Holidays.txt 파일이 생성됩니다.

편의상 기본적으로 다음 연도(Next Year)까지 수집됩니다.

주식시장 특성상 00시 00분 부터 05시 59분까지는 이전일(어제)로 취급합니다.

예를들어, 오늘이 2023년 8월 11일 새벽 02시 00분 이라고 가정하면

    trddt.date(day=None) # 날짜를 특정하지 않으면, 현재시각을 기준으로 자동계산됨
    >> datetime.datetime(2023, 8, 10, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), '대한민국 표준시'))







