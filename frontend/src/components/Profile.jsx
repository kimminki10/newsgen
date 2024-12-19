import React, { useState, useEffect } from "react";
import "./Profile.css";
import TextBox from "./TextBox";
import { useNavigate } from "react-router-dom";
import SubscriptionManagement from "./SubscriptionManagement";
import { useAuth } from "./AuthContext";

const Profile = () => {
  const {logout} = useAuth();
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState("");
  const [userEmail, setUserEmail] = useState("");
  const [selectedStocks, setSelectedStocks] = useState([
    "TSLA",
    "NVDA",
    "MSFT",
    "TSLA",
    "TSLA",
  ]);

  // 메일 발송 설정 상태
  const [mailSettings, setMailSettings] = useState({
    frequency: "workingDay", // workingDay 또는 everyday
    timeSlot: "onceDay", // onceDay 또는 twiceDay
    newsCount: "oneNews", // oneNews 또는 twoNews
  });

  // 설정 변경 및 저장/발송 상태
  const [isSettingsChanged, setIsSettingsChanged] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [isSending, setIsSending] = useState(false);

  // 이메일 가져오기
  useEffect(() => {
    const email = localStorage.getItem("userEmail");
    if (email) {
      setUserEmail(email);
    }
  }, []);

  // 샘플 티커 데이터
  const sampleTickers = [
    { ticker: "AAPL", name: "Apple Inc." },
    { ticker: "GOOGL", name: "Alphabet Inc." },
    { ticker: "AMZN", name: "Amazon.com Inc." },
    { ticker: "TSLA", name: "Tesla Inc." },
    { ticker: "NVDA", name: "NVIDIA Corporation" },
    { ticker: "MSFT", name: "Microsoft Corporation" },
  ];

  const [searchResults, setSearchResults] = useState([]);
  const maxStocks = 10;

  // 로그아웃 핸들러
  const handleLogout = () => {
    localStorage.removeItem("fintrend_access_token");
    localStorage.removeItem("fintrend_refresh_token");
    logout();
    navigate("/login");
  };

  // 검색 핸들러
  const handleSearch = (e) => {
    if (e.key === "Enter" || e.type === "click") {
      const results = sampleTickers.filter(
        (stock) =>
          stock.ticker.toLowerCase().includes(searchTerm.toLowerCase()) ||
          stock.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setSearchResults(results);
    }
  };

  // 주식 추가 핸들러
  const addStock = (ticker) => {
    if (selectedStocks.length < maxStocks && !selectedStocks.includes(ticker)) {
      setSelectedStocks([...selectedStocks, ticker]);
      setSearchResults([]);
      setSearchTerm("");
    }
  };

  // 주식 제거 핸들러
  const removeStock = (indexToRemove) => {
    setSelectedStocks(
      selectedStocks.filter((_, index) => index !== indexToRemove)
    );
  };

  // 메일 설정 변경 핸들러
  const handleMailSettingChange = (setting, value) => {
    setMailSettings((prev) => ({
      ...prev,
      [setting]: value,
    }));
    setIsSettingsChanged(true);
  };

  // 설정 저장 핸들러
  const handleSaveSettings = async () => {
    try {
      setIsSaving(true);
      // TODO: API 호출하여 설정 저장
      await new Promise((resolve) => setTimeout(resolve, 1000)); // 임시 딜레이
      setIsSettingsChanged(false);
      alert("설정이 저장되었습니다.");
    } catch (error) {
      alert("설정 저장에 실패했습니다.");
    } finally {
      setIsSaving(false);
    }
  };

  // 메일 발송 핸들러
  const handleSendMail = async () => {
    try {
      setIsSending(true);
      // TODO: API 호출하여 메일 발송
      await new Promise((resolve) => setTimeout(resolve, 1000)); // 임시 딜레이
      alert("메일이 발송되었습니다.");
    } catch (error) {
      alert("메일 발송에 실패했습니다.");
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className="profile-container">
      {/* 프로필 헤더 섹션 */}
      <div className="profile-header">
        <div className="user-info">
          <span className="emoji">😊</span>
          <span className="email">{userEmail}</span>
          <button onClick={handleLogout} className="logout-btn">
            로그아웃
          </button>
        </div>
      </div>

      {/* 주식 구독 섹션 */}
      <div className="stock-section">
        <h2>구독 중이에요!</h2>
        <div className="stock-info">
          <span>최대 {maxStocks}개를 추천해요! </span>
          <span className="remaining">
            (추가로 🤗 {maxStocks - selectedStocks.length}개 까지 가능)
          </span>
        </div>
        <div className="stock-grid">
          {selectedStocks.map((stock, index) => (
            <div key={index} className="stock-item">
              {stock}
              <button className="remove-btn" onClick={() => removeStock(index)}>
                X
              </button>
            </div>
          ))}
        </div>
        <div className="stock-search">
          <div className="search-container">
            <TextBox
              type="text"
              placeholder="티커 또는 기업명 검색"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyPress={handleSearch}
            />
            <button className="search-button" onClick={handleSearch}>
              🔍
            </button>
          </div>
          {searchResults.length > 0 && (
            <div className="search-results">
              {searchResults.map((result, index) => (
                <div
                  key={index}
                  className="search-result-item"
                  onClick={() => addStock(result.ticker)}
                >
                  <span className="ticker">{result.ticker}</span>
                  <span className="company-name">{result.name}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* 메일 발송 설정 섹션 */}
      <div className="notification-section">
        <h2>메일 발송 설정</h2>
        <table className="notification-table">
          <tbody>
            <tr>
              <td
                className={
                  mailSettings.frequency === "workingDay" ? "selected" : ""
                }
                onClick={() =>
                  handleMailSettingChange("frequency", "workingDay")
                }
              >
                Working Day만 받기 (월-금)
              </td>
              <td
                className={
                  mailSettings.frequency === "everyday" ? "selected" : ""
                }
                onClick={() => handleMailSettingChange("frequency", "everyday")}
              >
                매일 받기 (월-일)
              </td>
            </tr>
            <tr>
              <td
                className={
                  mailSettings.timeSlot === "onceDay" ? "selected" : ""
                }
                onClick={() => handleMailSettingChange("timeSlot", "onceDay")}
              >
                아침 8시 하루 1번!
              </td>
              <td
                className={
                  mailSettings.timeSlot === "twiceDay" ? "selected" : ""
                }
                onClick={() => handleMailSettingChange("timeSlot", "twiceDay")}
              >
                아침 9시, 저녁 9시 하루 두번!
              </td>
            </tr>
            <tr>
              <td
                className={
                  mailSettings.newsCount === "oneNews" ? "selected" : ""
                }
                onClick={() => handleMailSettingChange("newsCount", "oneNews")}
              >
                종목 하나당 기사 1개씩
              </td>
              <td
                className={
                  mailSettings.newsCount === "twoNews" ? "selected" : ""
                }
                onClick={() => handleMailSettingChange("newsCount", "twoNews")}
              >
                종목 하나당 기사 2개씩
              </td>
            </tr>
          </tbody>
        </table>
        <div className="notification-buttons">
          <button
            className={`save-button ${isSettingsChanged ? "active" : ""}`}
            onClick={handleSaveSettings}
            disabled={!isSettingsChanged || isSaving}
          >
            {isSaving ? "저장 중..." : "설정 저장하기"}
          </button>
          <button
            className="send-button"
            onClick={handleSendMail}
            disabled={isSending || isSettingsChanged}
          >
            {isSending ? "발송 중..." : "지금 메일 보내기"} 📨
          </button>
        </div>
      </div>

      {/* 구독 관리 섹션 */}
      <SubscriptionManagement />
    </div>
  );
};

export default Profile;
