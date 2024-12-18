import React, { forwardRef } from 'react';
import './TextBox.css';

const TextBox = forwardRef(({ label, type, placeholder, value, onChange }, ref) => {
    TextBox.displayName = 'TextBox';

    return (
        <div className="text-box">
        <label>{label}</label>
        <input
            ref={ref}
            type={type}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
        />
        </div>
    );
});

export default TextBox;