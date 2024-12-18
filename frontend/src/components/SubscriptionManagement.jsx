import React, { useState } from "react";
import "./SubscriptionManagement.css";

const SubscriptionManagement = () => {
  const [inviteEmail, setInviteEmail] = useState("");
  const [showMessage, setShowMessage] = useState(false);
  const [selectedDuration, setSelectedDuration] = useState(null);

  const handleInvite = () => {
    if (inviteEmail) {
      setShowMessage(true);
      setInviteEmail("");
      setTimeout(() => setShowMessage(false), 3000);
    }
  };

  const handleSubscriptionChange = (duration) => {
    setSelectedDuration(duration);
  };

  return (
    <div className="subscription-container">
      {/* 친구 초대 섹션 */}
      <div className="section-box">
        <h2>친구 초대하기</h2>
        <div className="section-content">
          <p className="description">
            이메일을 입력해주시면 핀트렌드 초대 메일을 송부 드려요. 친구에게도
            핀트렌드를 소개해 주세요!
          </p>
          <div className="input-container">
            <input
              type="email"
              value={inviteEmail}
              onChange={(e) => setInviteEmail(e.target.value)}
              placeholder="example@gmail.com"
              className="email-input"
            />
            <button onClick={handleInvite} className="send-button">
              발송하기
            </button>
          </div>
          {showMessage && (
            <p className="success-message">초대장이 발송되었습니다!</p>
          )}
        </div>
      </div>

      {/* 구독 관리 섹션 */}
      <div className="section-box">
        <h2>구독 관리하기</h2>
        <div className="section-content">
          <p className="description">
            잠시 쉬어가고 싶으신가요? 원하시는 기간을 선택해주세요. 기간이
            지나면 다시 찾아뵙겠습니다! 😊
          </p>
          <div className="subscription-buttons">
            <button
              className={`duration-button ${
                selectedDuration === "oneMonth" ? "selected" : ""
              }`}
              onClick={() => handleSubscriptionChange("oneMonth")}
            >
              생각할 시간을 갖자 (1개월 후 다시 발송)
            </button>
            <button
              className={`duration-button ${
                selectedDuration === "twoMonths" ? "selected" : ""
              }`}
              onClick={() => handleSubscriptionChange("twoMonths")}
            >
              좀 길게 생각하자 (2개월 후 다시 발송)
            </button>
            <button
              className="unsubscribe-button"
              onClick={() => handleSubscriptionChange("unsubscribe")}
            >
              우리 그만 해여자 (구독 해지) 😭
            </button>
            <p className="unsubscribe-note">
              * 구독 해지 시 저장된 모든 설정이 초기화됩니다
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SubscriptionManagement;
