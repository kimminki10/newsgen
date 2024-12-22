import React, { useState, useEffect } from "react";
import "./Profile.css";
import TextBox from "./TextBox";
import { useNavigate } from "react-router-dom";
import SubscriptionManagement from "./SubscriptionManagement";
import { useAuth } from "./AuthContext";
import axios from "axios";
import { useTicker } from "./TickerContext";


const Profile = () => {
  const {logout} = useAuth();
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState("");
  const [userEmail, setUserEmail] = useState("");
  const [selectedStocks, setSelectedStocks] = useState([]);
  const { tickerList } = useTicker();


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
  

  const requestUserInfo = async () => {
    try {
      const email = localStorage.getItem("userEmail");
      const header = {
        Authorization: `Bearer ${localStorage.getItem("fintrend_access_token")}`,
      }
      const response = await axios.get(`/api/user/${email}/`, { headers: header });
      const user = response.data;
      setMailSettings({
        frequency: user.mail_frequency,
        timeSlot: user.mail_timeSlot,
        newsCount: user.mail_newsCount,
      });
      setSelectedStocks(user.tickers.map((stock) => stock.ticker_name));
      console.log(response.data);
    } catch (error) {
      console.error(error);
      logout();
      navigate("/login");
    }
  }

  // 이메일 가져오기
  useEffect(() => {
    const email = localStorage.getItem("userEmail");
    if (email) {
      setUserEmail(email);
      requestUserInfo();
    } else {
      navigate("/login");
    }
  }, []);

  const [searchResults, setSearchResults] = useState([]);
  const maxStocks = 10;

  const requestUserUpdate = async () => {
    try {
      const data = { 
        tickers: selectedStocks,
        mail_frequency: mailSettings.frequency,
        mail_timeSlot: mailSettings.timeSlot,
        mail_newsCount: mailSettings.newsCount,
      };
      const header = {
        Authorization: `Bearer ${localStorage.getItem("fintrend_access_token")}`,
      }
      const response = await axios.put("/api/user/update/", data, { headers: header });
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  }

  // 로그아웃 핸들러
  const handleLogout = () => {
    localStorage.removeItem("fintrend_access_token");
    localStorage.removeItem("fintrend_refresh_token");
    localStorage.removeItem("userEmail");
    logout();
    navigate("/login");
  };

  // 검색 핸들러
  const handleSearch = (e) => {
    if (searchTerm === "") {
      setSearchResults([]);
      return;
    }
    if (e.key === 'Enter') {
      console.log('Enter');
      searchResults[0] && addStock(searchResults[0]);
      setSearchResults([]);
      setSearchTerm("");
      return;
    }
    const results = tickerList.filter((ticker) =>
      ticker.ticker_name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    const tickerNames = results.map((stock) => stock.ticker_name);
    setSearchResults(tickerNames);
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
      await requestUserUpdate();
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
      const header = {
        Authorization: `Bearer ${localStorage.getItem("fintrend_access_token")}`,
      }
      const response = await axios.post("/api/user/mail/send/", {}, { headers: header });
      console.log(response);
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
          </div>
          {searchResults.length > 0 && (
            <div className="search-results">
              {searchResults.map((ticker, index) => (
                <div
                  key={index}
                  className="search-result-item"
                  onClick={() => addStock(ticker)}
                >
                  <span className="ticker">{ticker}</span>
                </div>
              ))}
            </div>
          )}
        </div>
        <div className="stock-buttons">
          <button
            className={`save-button active`}
            onClick={handleSaveSettings}
          >
            {isSaving ? "저장 중..." : "설정 저장하기"}
          </button>
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
