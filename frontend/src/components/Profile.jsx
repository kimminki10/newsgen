import React from "react";
import "./Profile.css";

const Profile = () => {
  // 사용자 정보 (나중에 상태 관리로 변경 필요)
  const userInfo = {
    email: "mememe@gmail.com",
    maxStocks: 10,
    remainingStocks: 5,
    selectedStocks: [
      "TSLA",
      "NVDA",
      "MSFT",
      "TSLA",
      "TSLA",
      "TSLA",
      "NVDA",
      "MSFT",
      "TSLA",
      "TSLA",
      "TSLA",
      "NVDA",
      "MSFT",
      "TSLA",
      "TSLA",
    ],
  };

  const emailNotificationSettings = {
    workingDay: true,
    morningTime: "아침 8시 하루 1번!",
    stockNewsCount: "중목 하나당 기사 1개씩",
  };

  return (
    <div className="profile-container">
      <div className="profile-header">
        <div className="profile-title">Mypage1</div>
        <div className="user-info">
          <span className="emoji">😀</span>
          <span className="email">{userInfo.email}</span>
        </div>
      </div>

      <div className="stock-section">
        <h2>구독 중이에요!</h2>
        <div className="stock-info">
          <span>최대 {userInfo.maxStocks}개를 추천해요! </span>
          <span className="remaining">
            (🤗 {userInfo.remainingStocks}개 까지 가능)
          </span>
        </div>
        <div className="stock-grid">
          {userInfo.selectedStocks.map((stock, index) => (
            <div key={index} className="stock-item">
              {stock}
              <button className="remove-btn">X</button>
            </div>
          ))}
        </div>
        <div className="stock-search">
          <input type="text" placeholder="티커 또는 기업명 검색" />
        </div>
      </div>

      <div className="notification-section">
        <h2>메일 발송 설정</h2>
        <table className="notification-table">
          <tbody>
            <tr>
              <td>월 화 수 목 금</td>
              <td>월 화 수 목 금 토 일</td>
            </tr>
            <tr>
              <td>Working Day만 보내줘</td>
              <td>난 주말도 볼거야</td>
            </tr>
            <tr>
              <td>{emailNotificationSettings.morningTime}</td>
              <td>아침 9시, 저녁 9시 하루 두번!</td>
            </tr>
            <tr>
              <td>{emailNotificationSettings.stockNewsCount}</td>
              <td>중목 하나당 기사 2개씩</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Profile;
