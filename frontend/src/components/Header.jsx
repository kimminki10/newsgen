import React from "react";
import { Link } from "react-router-dom";
import './Header.css';

const HeaderButton = ({ text, link }) => {
    return (
        <Link to={link} className="header-button">{text}</Link>
    );
};

const Header = () => {
    return (
        <div className="header">
            <div className="header-title">Fintrend</div>
            <div className="header-content">
                <HeaderButton text="about" link="/about" />
                <HeaderButton text="login" link="/login" />
                <HeaderButton text="register" link="/register" />
            </div>
        </div>
    );
};

export default Header;