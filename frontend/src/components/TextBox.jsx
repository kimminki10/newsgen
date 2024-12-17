import React from 'react';
import './TextBox.css';

const TextBox = ({ label, type, placeholder, value, onChange }) => {
    return (
        <div className="text-box">
        <label>{label}</label>
        <input
            type={type}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
        />
        </div>
    );
};

export default TextBox;