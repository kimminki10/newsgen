import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "./AuthContext";
import SearchTextBox from "./SearchTextBox";
import "./Header.css";

const HeaderButton = ({ text, link, onClick }) => {
  if (onClick) {
    return (
      <button onClick={onClick} className="header-button">
        {text}
      </button>
    );
  }
  return (
    <Link to={link} className="header-button">
      {text}
    </Link>
  );
};

const Header = () => {
  const { isLoggedIn, userEmail, logout } = useAuth();

  return (
    <div>
      <div className="header">
        <Link to="/" className="header-title">
          Fintrend
        </Link>
        <div className="header-content">
          <HeaderButton text="about" link="/about" />
          {isLoggedIn ? (
            <>
              <Link to="/profile" className="user-profile">
                <span className="user-icon">😊</span>
                <span className="user-email">{userEmail}</span>
              </Link>
              <HeaderButton text="logout" onClick={logout} />
            </>
          ) : (
            <>
              <HeaderButton text="login" link="/login" />
              <HeaderButton text="register" link="/register" />
            </>
          )}
        </div>
      </div>
      <SearchTextBox />
    </div>
  );
};

export default Header;
