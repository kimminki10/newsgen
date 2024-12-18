import React from "react";
import { Link } from "react-router-dom";
import SearchTextBox from "./SearchTextBox";
import "./Header.css";

const HeaderButton = ({ text, link }) => {
  return (
    <Link to={link} className="header-button">
      {text}
    </Link>
  );
};

const Header = () => {
  return (
    <div>
      <div className="header">
        <Link to="/" className="header-title">
          Fintrend
        </Link>
        <div className="header-content">
          <HeaderButton text="about" link="/about" />
          <HeaderButton text="login" link="/login" />
          <HeaderButton text="register" link="/register" />
        </div>
      </div>
      <SearchTextBox />
    </div>
  );
};

export default Header;
