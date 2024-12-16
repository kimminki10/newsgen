import React from "react";
import { Link } from "react-router-dom";

const HeaderButton = ({ text, link }) => {
    return (
        <Link to={link} style={{ margin: '0 10px' }}>{text}</Link>
    );
};

const Header = () => {
    return (
        <div className="header">
            <HeaderButton text="about" link="/about" />
            <HeaderButton text="login" link="/login" />
            <HeaderButton text="register" link="/register" />
        </div>
    );
};

export default Header;