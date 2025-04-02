# Test
앱 백엔드 공부용

업로드 사항
1. Naver Map API 연결
  - MapView 사용해서 메인화면 상에 띄우기'
  - 레이어 추가 내용    
    - naverMap.setLayerGroupEnabled(NaverMap.LAYER_GROUP_TRANSIT, true) → 교통수단 표시    
    - naverMap.isNightModeEnabled = true → 야간모드 On
   

 shuttle-bus-backend/
│── config/
│   ├── db.js             # ✅데이터베이스 연결 설정 - 25/04/01
│── models/
│   ├── User.js           #✅ 유저 모델 - 25/04/02
│   ├── Notification.js   # 알림 모델
│   ├── BusStop.js        # 정류장 모델
│   ├── Announcement.js   # 공지사항 모델
│── routes/
│   ├── authRoutes.js     #✅ 로그인 및 회원가입 라우트 - 25/04/02
│   ├── busStopRoutes.js  # 셔틀버스 정류장 관련 라우트
│   ├── notificationRoutes.js # 알림 관련 라우트
│   ├── announcementRoutes.js # 공지사항 관련 라우트
│── middleware/
│   ├── authMiddleware.js # JWT 인증 미들웨어
│── server.js             # ✅메인 서버 파일 - 25/04/01
│── .env                  # ✅환경 변수 설정 -  25/04/01
